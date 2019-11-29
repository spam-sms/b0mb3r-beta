from service import Service


class Lenta(Service):
    async def run(self):
        await self.client.post('https://lenta.com/api/v1/authentication/requestValidationCode',
                          json={'phone': '+' + self.formatted_phone})
