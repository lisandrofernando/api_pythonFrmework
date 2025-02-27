import requests
from utilities.headers_utils import HederBuilder

class APIRequest:
    def __init__(self, base_url):
        self.base_url = base_url
        self.headers =  HederBuilder().get_headers()
    
    def get(self, endpoint, params=None):
        return requests.get(
            f"{self.base_url}{endpoint}",
            headers=self.headers,
            params=params
        )
    
    def post(self, endpoint, payload):
        return requests.post(
            f"{self.base_url}{endpoint}",
            headers=self.headers,
            json=payload
        )