from service import Service


class Youla(Service):
    async def run(self):
        await self.client.post('https://youla.ru/web-api/auth/request_code', data={'phone': self.formatted_phone})
