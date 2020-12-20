import requests
import validators


HEADERS = {
    'User-Agent': (
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36'
        '(KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
    )
}


class Requests:

    def __init__(self, url):
        if not validators.url(url):
            raise Exception(f'{url} is not valid url')
        self.url = url

    def get(self):
        try:
            response = requests.get(self.url, headers=HEADERS)
            return response.content
        except Exception:
            return None
    
    def post(self):
        pass
