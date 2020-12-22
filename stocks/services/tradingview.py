from bs4 import BeautifulSoup

from main.helpers.requests import Requests


TRADINGVIEW = 'https://br.tradingview.com'


class StockInformationTradingView(Requests):

    def __init__(self, url, code):
        if not url.startswith(TRADINGVIEW):
            raise Exception(f'{url} is not valid url')
        super().__init__(url=url)
        self.code = code

    @property
    def content(self):
        if not hasattr(self, '_content'):
            self._content = BeautifulSoup(self.get(), 'html.parser')
        return self._content

    @property
    def price(self):
        pass

    def valid_response_content(self):
        if self.content.find_all(attrs={'class': 'tv-http-error-page__message-wrap'}):
            return False
        return True
