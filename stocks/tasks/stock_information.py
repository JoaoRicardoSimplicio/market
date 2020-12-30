import click

from main.helpers import tables

from stocks.services.stock import StockFactory
from stocks.queries.wallet_queries import WalletQueries


def get_stock_code_from_user():
	stock_code = click.prompt("Enter code stock", type=str)
	return stock_code


def get_amount_stock_from_user():
    amount = click.prompt("Inform the quantity (sale or purchase)", type=int)
    return amount


def get_price_stock_from_user():
	price = click.prompt("Inform the price of stock", type=str)
	return price


def get_date_from_user():
	date = click.prompt("Inform the date", type=str)
	return date


def get_user_information(stock_code):
	if not stock_code:
		stock_code = get_stock_code_from_user()
	amount = get_amount_stock_from_user()
	price = get_price_stock_from_user()
	date = get_date_from_user()
	return {"code": stock_code, "amount": amount, "price": price, "date": date}


def build_stock_object_information(stock):
    if stock:
        stock_information = {
            'code': stock.code,
            'price': stock.price,
            'description': stock.description,
        }
        return stock_information


def get_stock_object_information(stock_code):
    stock_factory = StockFactory(code=stock_code)
    stock = stock_factory.create()
    stock_information = build_stock_object_information(stock=stock)
    return stock_information


def show_stock_information(stock_code=None, stock_crawled=None):
    if not stock_crawled:
        stock_crawled = get_stock_object_information(stock_code=stock_code)
    table = tables.create_stock_table(stock_crawled)
    print(table)


def show_all_stocks_saved():
    wallet = WalletQueries()
    wallet.fill_stocks_informations()
    table = tables.create_wallet_table(wallet.stocks)
    print(table)


def show_stock_transaction(stock_transaction):
    if not stock_transaction:
        return
    table = tables.create_stock_transaction_table(stock_transaction=stock_transaction)
    print(table)
