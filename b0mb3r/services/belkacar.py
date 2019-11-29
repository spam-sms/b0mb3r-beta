from service import Service


class BelkaCar(Service):
    async def run(self):
        await self.client.post('https://belkacar.ru/get-confirmation-code',
                          data={'phone': self.formatted_phone})
