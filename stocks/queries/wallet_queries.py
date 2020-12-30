from stocks.models import Stock, StockBuy, StockSale
from stocks.services.stock import StockFactory


class WalletQueries:

	def __init__(self, wallet_name=None):
		self.wallet_name = wallet_name

	@property
	def stocks(self):
		if not hasattr(self, '_stocks'):
			self._stocks = Stock.objects.filter(amount__gt=0)
		return self._stocks

	def get_current_price(self, stock):
		current_price = self.extract_current_price(stock_code=stock.code)
		stock.current_price = current_price

	def get_price_last_buy(self, stock):
		price_last_buy = float(stock.buys.last().price)
		stock.price_last_buy = price_last_buy

	def extract_current_price(self, stock_code):
		stock_factory = StockFactory(code=stock_code)
		stock = stock_factory.create()
		if stock:
			return stock.price

	def fill_stocks_informations(self):
		for stock in self.stocks:
			self.get_current_price(stock)
			self.get_price_last_buy(stock)

		