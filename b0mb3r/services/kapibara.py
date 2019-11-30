from service import Service


class Kapibaras(Service):
    async def run(self):
        phone = f'+{self.formatted_phone[0]}({self.formatted_phone[1:4]})-{self.formatted_phone[4:7]}-{self.formatted_phone[7:11]}'
        await self.client.post('https://kapibaras.ru/api/lk/sendCode', json={'phone': phone, 'city': 1})
