from service import Service


class AtPrime(Service):
    async def run(self):
        await self.client.post("https://api-prime.anytime.global/api/v2/auth/sendVerificationCode",
                               data={"phone": self.formatted_phone})
