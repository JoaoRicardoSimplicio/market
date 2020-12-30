import json
import unittest

from datetime import datetime

from django.test import TestCase
from model_mommy import mommy
from unittest import mock

from stocks.tasks import stock_tasks, stock_purchase, stock_sale
from stocks.models import Stock, StockBuy, StockSale


def open_stock_json():
    fixtures_path = 'stocks/tests/fixtures/'
    with open(f'{fixtures_path}stock.json') as f:
        return json.loads(f.read())


def open_stock_purchases_json():
    fixtures_path = 'stocks/tests/fixtures/'
    with open(f'{fixtures_path}stock_purchases.json') as f:
        return json.loads(f.read())


def open_stock_sales_json():
    fixtures_path = 'stocks/tests/fixtures/'
    with open(f'{fixtures_path}stock_sales.json') as f:
        return json.loads(f.read())


PATH_STOCK_CODE_INPUT = 'stocks.tasks.stock_information.get_stock_code_from_user'
PATH_STOCK_AMOUNT_INPUT = 'stocks.tasks.stock_information.get_amount_stock_from_user'
PATH_STOCK_PRICE_INPUT = 'stocks.tasks.stock_information.get_price_stock_from_user'
PATH_STOCK_DATE_INPUT = 'stocks.tasks.stock_information.get_date_from_user'


@mock.patch(PATH_STOCK_CODE_INPUT, return_value='hbor3f')
@mock.patch(PATH_STOCK_AMOUNT_INPUT, return_value=10)
@mock.patch(PATH_STOCK_PRICE_INPUT, return_value='11,92')
@mock.patch(PATH_STOCK_DATE_INPUT, return_value='01/12/2020')
class TestStockCli(TestCase):

    def setUp(self):
        self.stock = mommy.make(
            Stock,
            code='hbor3f',
            amount=0,
        )

    def test_stock_tasks_buy(self, mock_stock_date, mock_stock_price,
                             mock_stock_amount, mock_stock_code):
        stock_purchase.buy_stock(stock_code='hbor3f')
        stock = Stock.objects.get(code='hbor3f')
        self.assertEqual(stock.amount, 10)

    def test_stock_tasks_purchases(self, mock_stock_date, mock_stock_price,
                                   mock_stock_amount, mock_stock_code):
        stock_purchase.buy_stock(stock_code='hbor3f')
        stock_purchases = StockBuy.objects.get(stock__code='hbor3f')
        self.assertEqual(float(stock_purchases.price), 11.92)

    def test_stock_raise_exception_sell_more_than_exists(self, mock_stock_date, mock_stock_price,
                                                         mock_stock_amount, mock_stock_code):
        self.assertRaises(Exception, stock_sale.sell_stock, 'hbor3f')

    def test_stock_tasks_two_buys(self, mock_stock_date, mock_stock_price,
                                  mock_stock_amount, mock_stock_code):
        stock_purchase.buy_stock(stock_code='hbor3f')
        stock_purchase.buy_stock(stock_code='hbor3f')
        stock = Stock.objects.get(code='hbor3f')
        self.assertEqual(stock.amount, 20)

    def test_stock_tasks_purchases(self, mock_stock_date, mock_stock_price,
                                   mock_stock_amount, mock_stock_code):
        stock_purchase.buy_stock(stock_code='hbor3f')
        purchases = stock_purchase.get_stock_purchases(stock_code='hbor3f')
        stock = Stock.objects.get(code='hbor3f')
        self.assertEqual(float(purchases[0].price), 11.92)
        self.assertEqual(stock.amount, 10)


    def test_stocks_tasks_sales(self, mock_stock_date, mock_stock_price,
                                mock_stock_amount, mock_stock_code):
        self.stock.amount += 20
        self.stock.save()
        stock_sale.sell_stock(stock_code='hbor3f')
        sales = stock_sale.get_stock_sales(stock_code='hbor3f')
        self.assertEqual(float(sales[0].price), 11.92)
        self.assertEqual(sales[0].amount, 10)
        self.assertEqual(Stock.objects.get(code='hbor3f').amount, 10)
