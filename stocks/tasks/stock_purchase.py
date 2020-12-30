from stocks.queries.stock_queries import StockQueries
from stocks.tasks.stock_information import get_user_information


def buy_stock(stock_code):
    data = get_user_information(stock_code=stock_code)
    stock = StockQueries(**data)
    stock.buy()


def get_stock_purchases(stock_code):
    stock = StockQueries(code=stock_code, price=None, description=None)
    purchases = stock.purchases()
    return purchases
