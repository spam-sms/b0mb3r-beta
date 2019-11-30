from service import Service


class Dostaevsky(Service):
    async def run(self):
        phone = f'{self.formatted_phone[0]} {self.formatted_phone[1:4]} {self.formatted_phone[4:7]}-{self.formatted_phone[7:9]}-{self.formatted_phone[9:11]}'
        await self.client.post('https://dostaevsky.ru/auth/send-sms', data={'phone': phone})
