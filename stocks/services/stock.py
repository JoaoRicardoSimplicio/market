from googlesearch import search

from main.helpers.requests import Requests
from stocks.services.infomoney import StockInformationInfoMoney
from stocks.services.tradingview import StockInformationTradingView


WEB_SITES = [
    'https://www.infomoney',
    'https://br.tradingview.com'
]


WEB_SITE_CRAWLERS = [
    StockInformationInfoMoney,
    StockInformationTradingView
]


class StockFactory:

    def __init__(self, code):
        self.code = code

    def create(self):
        urls = self.get_urls_with_stock_code()
        return self.select_valid_website_to_extract(urls)
        
    def get_urls_with_stock_code(self):
        urls = search(self.code, num_results=50)
        return urls

    def select_valid_website_to_extract(self, urls):
        for site in WEB_SITES:
            website_urls = [url for url in urls if url.startswith(site)]
            for website_url in website_urls:
                for website_crawler in WEB_SITE_CRAWLERS:
                    try:
                        stock = website_crawler(url=website_url, code=self.code)
                        if stock.valid_response_content():
                            return stock
                    except Exception:
                        pass
