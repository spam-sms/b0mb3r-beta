from service import Service


class DeliveryClub(Service):
    async def run(self):
        await self.client.post('https://www.delivery-club.ru/ajax/user_otp', data={"phone": self.formatted_phone})