from service import Service


class RuTube(Service):
    async def run(self):
        await self.client.post('https://rutube.ru/api/accounts/sendpass/phone', data={'phone': '+' + self.formatted_phone})
