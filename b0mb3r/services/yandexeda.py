from service import Service


class YandexEda(Service):
    async def run(self):
        await self.client.post('https://eda.yandex/api/v1/user/request_authentication_code',
                               json={"phone_number": "+" + self.formatted_phone})
