from service import Service


class SMSGorod(Service):
    async def run(self):
        await self.client.post("http://smsgorod.ru/sendsms.php",
                               data={"number": self.formatted_phone})
