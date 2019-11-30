from service import Service


class CarSmile(Service):
    async def run(self):
        await self.client.post("https://api.carsmile.com/",
                               json={"operationName": "enterPhone", "variables": {"phone": self.formatted_phone},
                                     "query": "mutation enterPhone($phone: String!) {\n  enterPhone(phone: $phone)\n}\n"})
