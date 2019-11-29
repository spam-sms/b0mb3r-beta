from service import Service


class FindClone(Service):
    async def run(self):
        await self.client.get('https://findclone.ru/register', params={'phone': '+' + self.formatted_phone})
