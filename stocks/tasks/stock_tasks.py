import click

from main.helpers import tables

from stocks.queries.stock_queries import StockQueries
from stocks.services.stock import StockFactory


def stock_tasks(stock_code, task):
    if task:
        if task == "buy":
            buy_stock(stock_code=stock_code)
        elif task == "sell":
            sell_stock(stock_code=stock_code)
        elif task == "purchases" or task == "sales":
            if task == "purchases":
                stock_transaction = get_stock_purchases(stock_code=stock_code)
            elif task == "sales":
                stock_transaction = get_stock_sales(stock_code=stock_code)
            show_stock_transaction(stock_transaction=stock_transaction)
            
    else:
        if stock_code:
            show_stock_information(stock_code=stock_code, stock_crawled=None)
        else:
            pass


def get_stock_object_information(stock_code):
    stock_factory = StockFactory(code=stock_code)
    stock = stock_factory.create()
    stock_information = build_stock_object_information(stock=stock)
    return stock_information


def build_stock_object_information(stock):
    if stock:
        stock_information = {
            'code': stock.code,
            'price': stock.price,
            'description': stock.description,
        }
        return stock_information


def get_amount_stocks_from_user():
    amount = click.prompt("Inform the quantity (sale or purchase)", type=int)
    return amount


def buy_stock(stock_code):
    amount = get_amount_stocks_from_user()
    stock_information = get_stock_object_information(stock_code=stock_code)
    stock = StockQueries(amount=amount, **stock_information)
    stock.buy()


def sell_stock(stock_code):
    amount = get_amount_stocks_from_user()
    stock_information = get_stock_object_information(stock_code=stock_code)
    stock = StockQueries(amount=amount, **stock_information)
    stock.sell()


def get_stock_purchases(stock_code):
    stock = StockQueries(code=stock_code, price=None, description=None)
    purchases = stock.purchases()
    return purchases


def get_stock_sales(stock_code):
    stock = StockQueries(code=stock_code, price=None, description=None)
    sales = stock.sales()
    return sales


def show_stock_information(stock_code=None, stock_crawled=None):
    if not stock_crawled:
        stock_crawled = get_stock_object_information(stock_code=stock_code)
    table = tables.create_stock_table(stock_crawled)
    print(table)


def show_stock_transaction(stock_transaction):
    if not stock_transaction:
        return
    table = tables.create_stock_transaction_table(stock_transaction=stock_transaction)
    print(table)