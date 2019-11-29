#!/usr/bin/env python
# -*- coding: utf-8 -*-
import inspect
import os
import sys
import click
import traceback
import webbrowser
import pkgutil
import pkg_resources
import uvicorn
from httpx.exceptions import HTTPError
from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

country_codes = {'7': 'ru', '375': 'by', '380': 'ua'}
os.chdir(os.path.join(pkg_resources.get_distribution('b0mb3r').location, 'b0mb3r'))

templates = Jinja2Templates(directory="templates")

app = Starlette(debug=True)
app.mount('/static', StaticFiles(directory="static"), name='static')


@click.command()
def main():
    webbrowser.open('http://127.0.0.1:8080/', new=2, autoraise=True)
    print(
        "Интерфейс был запущен по этой ссылке: http://127.0.0.1:8080/. Если она не открылась автоматически - скопируйте и вставьте её в браузер.")
    uvicorn.run(app, host='127.0.0.1', port=8080)


def load_services():
    services = os.listdir("services")
    service_classes = {}
    sys.path.insert(0, "services")

    for service in services:
        if service.endswith('.py') and service != 'service.py':
            module = __import__(service[:-3])
            for member in inspect.getmembers(module, inspect.isclass):
                if member[1].__module__ == module.__name__:
                    service_classes[module] = member[0]

    return service_classes


@app.route('/', methods=['GET'])
async def server_index(request):
    return templates.TemplateResponse('index.html', {'request': request, 'services_count': len(load_services())})


@app.route('/attack/start', methods=['POST'])
async def server_start_attack(request):
    try:
        data = await request.form()
        phone = data['phone'].replace("-", "").replace(" ", "")

        number_of_cycles = int(data['number_of_cycles'])
        if int(number_of_cycles) < 1:
            return JSONResponse(
                {'success': False, 'error_code': 400,
                 'error_description': 'The minimum value for number_of_cycles is 1.'})

        phone_code = data['phone_code']
        if phone_code not in country_codes.keys():
            return JSONResponse(
                {'success': False, 'error_code': 400, 'error_description': 'This phone_code is not supported.'},
                status_code=400)

        for _ in range(number_of_cycles):
            for module, service in load_services().items():
                try:
                    await getattr(module, service)(phone, phone_code).run()
                except HTTPError:
                    pass

        return JSONResponse({'success': True})
    except (ValueError, KeyError):
        return JSONResponse({'success': False, 'error_code': 400, 'error_description': 'Missing or invalid values.'},
                            status_code=400)
    except Exception as error:
        formatted_error = f"{type(error).__name__}: {error}"
        return JSONResponse({'success': False, 'error_code': 500, 'error_description': formatted_error,
                             "traceback": traceback.format_exc()}, status_code=500)


if __name__ == '__main__':
    main()
