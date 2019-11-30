from service import Service


class Dostavista(Service):
    async def run(self):
        phone = f'{self.formatted_phone[1:4]} {self.formatted_phone[4:7]}-{self.formatted_phone[7:9]}-{self.formatted_phone[9:11]}'
        cookies = self.client.get('https://dostavista.ru/').cookies
        await self.client.post('https://dostavista.ru/backend/send-verification-sms', cookies=cookies, data={'phone': phone})
