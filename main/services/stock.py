from googlesearch import search

from main.helpers.requests import Requests
from main.services.infomoney import StockInformationInfoMoney


class StockFactory:

    def __init__(self, code):
        self.code = code

    def create(self):
        urls = self.get_urls_with_action_code()
        return self.select_valid_website_to_extract(urls)
        
    def get_urls_with_action_code(self):
        urls = search(self.code, num_results=50)
        return urls

    def select_valid_website_to_extract(self, urls):
        for url in urls:
            try:
                if url.startswith('https://www.infomoney'):
                    stock = StockInformationInfoMoney(url=url)
                    if stock.valid_response_content():
                        return stock
            except Exception:
                pass
