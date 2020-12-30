import click

from main.helpers import tables

from stocks.queries.stock_queries import StockQueries
from stocks.tasks import stock_information, stock_purchase, stock_sale
from stocks.services.stock import StockFactory


def stock_tasks(stock_code, task):
    if task:
        if task == "all":
            stock_information.show_all_stocks_saved()
        elif task == "buy":
            stock_purchase.buy_stock(stock_code=stock_code)
        elif task == "sell":
            stock_sale.sell_stock(stock_code=stock_code)
        elif task == "purchases" or task == "sales":
            if task == "purchases":
                pass
                stock_transaction = stock_purchase.get_stock_purchases(stock_code=stock_code)
            elif task == "sales":
                pass
                stock_transaction = stock_sale.get_stock_sales(stock_code=stock_code)
            stock_information.show_stock_transaction(stock_transaction=stock_transaction)
            
    else:
        if stock_code:
            stock_information.show_stock_information(stock_code=stock_code, stock_crawled=None)
        else:
            pass
