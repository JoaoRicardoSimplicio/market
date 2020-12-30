from django.db.models.query import QuerySet

from prettytable import PrettyTable


def create_stock_table_header(table_type):
    table = PrettyTable()
    if table_type == 'stock':
        table.field_names = ['code', 'price', 'amount', 'date']
    elif table_type == 'wallet':
        table.field_names = ['code', 'amount', 'current_price', 'price_last_buy']
    elif table_type == 'transaction':
        table.field_names = ['code', 'price', 'amount', 'date']
    return table


def format_stock_information(stock):
    if stock:
        stock_information = {}
        stock_information['code'] = stock['code']
        stock_information['price'] = stock['price']
        if 'amount' in stock:   
            stock_information['amount'] = stock['amount']
        else:
            stock_information['amount'] = None
        if 'date' in stock:
            stock_information['date'] = stock['date']
        else:
            stock_information['date'] = None
        return stock_information


def create_stock_table_row(table, stock_information):
    stock_information = format_stock_information(stock=stock_information)
    if stock_information:
        table.add_row(
            [stock_information['code'], stock_information['price'], stock_information['amount'], stock_information['date']]
        )


def create_stock_table(stock_information):
    table = create_stock_table_header(table_type='stock')
    if type(stock_information) is QuerySet:
        for stock in stock_information:
            create_stock_table_row(table=table, stock_information=stock)
    else:
        create_stock_table_row(table=table, stock_information=stock_information)
    return table


def format_stock_transaction(stock):
    stock_transaction = {}
    stock_transaction['code'] = stock.stock
    stock_transaction['price'] = stock.price
    stock_transaction['amount'] = stock.amount
    stock_transaction['date'] = stock.date
    return stock_transaction


def create_transaction_table_row(table, stock_transaction):
    stock_transaction = format_stock_transaction(stock=stock_transaction)
    table.add_row(
        [stock_transaction['code'], stock_transaction['price'], stock_transaction['amount'], stock_transaction['date']]
    )


def create_stock_transaction_table(stock_transaction):
    table = create_stock_table_header(table_type='transaction')
    if type(stock_transaction) is QuerySet or type(stock_transaction) is list:
        for transaction in stock_transaction:
            create_transaction_table_row(table=table, stock_transaction=transaction)
    else:
        create_transaction_table_row(table=table, stock_transaction=stock_transaction)
    return table


def format_stock_wallet(stock):
    stock_information = {}
    stock_information['code'] = stock.code
    stock_information['amount'] = stock.amount
    stock_information['current_price'] = stock.current_price
    stock_information['price_last_buy'] = stock.price_last_buy
    return stock_information


def create_wallet_table_row(table, stock_information):
    stock_information = format_stock_wallet(stock=stock_information)
    table.add_row(
        [
            stock_information['code'], stock_information['amount'], stock_information['current_price'],
            stock_information['price_last_buy']
        ]
    )


def create_wallet_table(stock_information):
    table = create_stock_table_header(table_type='wallet')
    if type(stock_information) is QuerySet or type(stock_information) is list:
        for stock in stock_information:
            create_wallet_table_row(table=table, stock_information=stock)
    else:
        create_wallet_table_row(table=table, stock_information=stock_information)
    return table