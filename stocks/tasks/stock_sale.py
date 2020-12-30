from stocks.queries.stock_queries import StockQueries
from stocks.tasks.stock_information import get_user_information


def sell_stock(stock_code):
    data = get_user_information(stock_code=stock_code)
    stock = StockQueries(**data)
    stock.sell()


def get_stock_sales(stock_code):
    stock = StockQueries(code=stock_code, price=None, description=None)
    sales = stock.sales()
    return sales
