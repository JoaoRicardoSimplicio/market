import json
import unittest

from django.test import TestCase
from model_mommy import mommy
from unittest import mock

from stocks.tasks import stock_tasks
from stocks.models import Stock


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


PATH_STOCK = 'stocks.tasks.stock_tasks.get_stock_object_information'
PATH_STOCK_AMOUNT = 'stocks.tasks.stock_tasks.get_amount_stocks_from_user'
PATH_STOCK_PURCHASES = 'stocks.tasks.stock_tasks.get_stock_purchases'
PATH_STOCK_SALES = 'stocks.tasks.stock_tasks.get_stock_sales'


@mock.patch(PATH_STOCK, return_value=open_stock_json())
class TestStockTasks(TestCase):
    
    def setUp(self):
        self.stock = mommy.make(
            Stock,
            code='hbor3f',
            amount=10,
        )

    @mock.patch(PATH_STOCK_AMOUNT, return_value=10)
    def test_stock_tasks_buy(self, mock_stock, mock_stock_amount):
        stock_tasks.buy_stock(stock_code='hbor3f')
        stock = Stock.objects.get(code='hbor3f')
        self.assertEqual(stock.amount, 20)

    @mock.patch(PATH_STOCK_AMOUNT, return_value=10)
    def test_stock_tasks_sale(self, mock_stock, mock_stock_amount):
        stock_tasks.sell_stock(stock_code='hbor3f')
        stock = Stock.objects.get(code='hbor3f')
        self.assertEqual(stock.amount, 0)

    @mock.patch(PATH_STOCK_AMOUNT, return_value=15)
    def test_stock_raise_exception_sell_more_than_exists(self, mock_stock, mock_stock_amount):
        self.assertRaises(Exception, stock_tasks.sell_stock, 'hbor3f')

    @mock.patch(PATH_STOCK_AMOUNT, return_value=10)
    def test_stock_tasks_two_buys(self, mock_stock, mock_stock_amount):
        stock_tasks.buy_stock(stock_code='hbor3f')
        stock_tasks.buy_stock(stock_code='hbor3f')
        stock = Stock.objects.get(code='hbor3f')
        self.assertEqual(stock.amount, 30)

    @mock.patch(PATH_STOCK_AMOUNT, return_value=None)
    def test_stock_raise_exception_buy_whitout_amount(self, mock_stock, mock_stock_amount):
        self.assertRaises(Exception, stock_tasks.buy_stock, 'hbor3f')

    @mock.patch(PATH_STOCK_PURCHASES, return_value=open_stock_purchases_json())
    def test_stock_tasks_purchases(self, mock_stock, mock_stock_purchases):
        purchases = stock_tasks.get_stock_purchases(stock_code='hbor3f')
        self.assertEqual(purchases[0]['price'], 11.72)
        self.assertEqual(purchases[0]['date'], '2020-12-22')
        self.assertEqual(purchases[0]['amount'], 20)

    @mock.patch(PATH_STOCK_SALES, return_value=open_stock_sales_json())
    def test_stock_tasks_sales(self, mock_stock, mock_stock_sales):
        sales = stock_tasks.get_stock_sales(stock_code='hbor3f')
        self.assertEqual(sales[0]['price'], 11.92)
        self.assertEqual(sales[0]['date'], '2020-12-25')
        self.assertEqual(sales[0]['amount'], 7)
