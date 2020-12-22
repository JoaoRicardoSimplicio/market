from systemtools.number import *

from stocks.models import Stock, StockBuy, StockSale
from stocks.queries import validators


class StockQueries:

    def __init__(self, amount=None, *args, **kwargs):
        if not kwargs["code"]:
            raise Exception("You need to enter the stock code")
        self.code = kwargs["code"]
        self.amount = amount
        self.price = kwargs["price"]
        self.description = kwargs["description"]
        self.stock = self.get_stock_from_db()
        self._convert_string_fields_to_float()

    def get_stock_from_db(self):
        if self.code:
            stock, _ = Stock.objects.get_or_create(
                code=self.code
            )
            if _ is True:
                stock.amount = 0
                stock.save()
            return stock

    def buy(self):
        self._stock_buy_validate()
        StockBuy.objects.create(
            stock=self.stock,
            price=self.price,
            amount=self.amount
        )
        self.stock.amount += self.amount
        self.stock.save()

    def sell(self):
        self._stock_sale_validate()
        StockSale.objects.create(
            stock=self.stock,
            price=self.price,
            amount=self.amount
        )
        self.stock.amount -= self.amount
        self.stock.save()

    def purchases(self):
        stock_purchase = StockBuy.objects.filter(stock=self.stock)
        return stock_purchase

    def sales(self):
        stock_sales = StockSale.objects.filter(stock=self.stock)
        return stock_sales

    def _stock_validate(self):
        if not self.price:
            raise Exception("You need to enter the stock price")
        if not self.amount:
            raise Exception("You need to enter the stock amount")

    def _stock_buy_validate(self):
        self._stock_validate()

    def _stock_sale_validate(self):
        self._stock_validate()
        if self.amount > self.stock.amount:
            raise Exception("you're trying to sell a quantity that you don't own")

    def _convert_string_fields_to_float(self):
        if self.price:
            self.price = parseNumber(self.price)



