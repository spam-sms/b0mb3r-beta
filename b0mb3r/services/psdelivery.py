from service import Service


class Psdelivery(Service):
    async def run(self):
        phone = f'+{self.formatted_phone[0]} ({self.formatted_phone[1:4]}) {self.formatted_phone[4:7]}-{self.formatted_phone[7:9]}-{self.formatted_phone[9:11]}'
        cookies = self.client.get('https://ps.delivery/').cookies
        self.client.post('https://ps.delivery/wp-admin/admin-ajax.php', cookies=cookies, data={'tel': phone, 'redirect_to': '', 'rememberme': 'forever', 'undefined': '', 'action': 'login'})
