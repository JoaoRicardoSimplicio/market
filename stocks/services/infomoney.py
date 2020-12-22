from bs4 import BeautifulSoup

from main.helpers.requests import Requests


INFO_MONEY = 'https://www.infomoney.com'


class StockInformationInfoMoney(Requests):

    def __init__(self, url, code):
        if not url.startswith(INFO_MONEY):
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
        if not hasattr(self, '_price'):
            try:
                price = self.content.find_all(attrs={'class': 'value'})[0].p.string
                if price:
                    price = price.strip()
                self._price = price
            except IndexError:
                self._price = None
        return self._price

    @property
    def highest_price_day(self):
        if not hasattr(self, '_highest_price_day'):
            try:
                highest_price_day = self.content.find_all(attrs={'class': 'maximo'})[0].p.string
                if highest_price_day:
                    highest_price_day = highest_price_day.strip()
                self._highest_price_day = highest_price_day
            except IndexError:
                self._highest_price_day = None
        return self._highest_price_day

    @property
    def lowest_price_day(self):
        if not hasattr(self, '_lowest_price_day'):
            try:
                lowest_price_day = self.content.find_all(attrs={'class': 'minimo'})[0].p.string
                if lowest_price_day:
                    lowest_price_day = lowest_price_day.strip()
                self._lowest_price_day = lowest_price_day
            except IndexError:
                self._lowest_price_day = None
        return self._lowest_price_day

    @property
    def description(self):
        if not hasattr(self, '_description'):
            try:
                description = self.content.find_all(attrs={'class': 'description'})[0].get_text()
                if description:
                    description = description.strip()
                self._description = description
            except IndexError:
                self._description = None
        return self._description

    @property
    def day_variation(self):
        if not hasattr(self, '_day_variation'):
            try:
                day_variation = self.content.find_all(attrs={'class': 'percentage'})[0].p.string
                if day_variation:
                    day_variation = day_variation.strip()
                self._day_variation = day_variation
            except IndexError:
                self._day_variation = None
        return self._day_variation

    @property
    def latest_news(self):
        if not hasattr(self, '_latest_news'):
            latest_news = self.get_lastest_news()

    def valid_response_content(self):
        if self.content.find_all(attrs={'class': 'error404'}):
            return False
        return True

    def get_lastest_news(self):
        pass