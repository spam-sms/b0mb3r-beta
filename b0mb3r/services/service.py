import httpx
from fake_useragent import UserAgent


class Service:
    user_agent = UserAgent()

    def __init__(self, phone, phone_code):
        self.phone = phone
        self.phone_code = phone_code
        self.formatted_phone = self.phone_code + self.phone
        self.client = httpx.AsyncClient()

        self.client.headers = {'User-Agent': self.generate_random_user_agent()}

    @staticmethod
    def generate_random_user_agent():
        return Service.user_agent.random
