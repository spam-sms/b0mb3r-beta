from service import Service


class Tinder(Service):
    async def run(self):
        await self.client.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',
                          data={'phone_number': self.formatted_phone})
