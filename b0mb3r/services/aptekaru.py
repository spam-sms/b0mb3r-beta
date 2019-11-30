# -*- coding: utf-8 -*-
from service import Service


class AptekaRu(Service):
    async def run(self):
        phone = f'+7 ({self.formatted_phone[1:4]}) {self.formatted_phone[4:7]}-{self.formatted_phone[7:9]}-{self.formatted_phone[9:11]}'
        await self.session.post('https://apteka.ru/_action/auth/getForm/', data={'form[LOGIN]': phone, 'get-new-password': 'Получите пароль по SMS', 'formType': 'simple', 'utc_offset': '180'})
