from service import Service


class Tinkoff(Service):
    async def run(self):
        await self.client.post('https://api.tinkoff.ru/v1/sign_up', data={'phone': '+' + self.formatted_phone})
