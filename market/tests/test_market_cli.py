import json
import pytest
import unittest

from click.testing import CliRunner

from market.market import main

from unittest import mock


def open_stock_json():
    fixtures_path = 'stocks/tests/fixtures/'
    with open(f'{fixtures_path}stock.json') as f:
        return json.loads(f.read())


def open_stock_information_output():
    fixtures_path = 'market/tests/fixtures/'
    with open(f'{fixtures_path}output_stock_information.txt') as f:
        return f.read()


def open_stock_purchases_json():
    fixtures_path = 'stocks/tests/fixtures/'
    with open(f'{fixtures_path}stock_purchases.json') as f:
        return json.loads(f.read())


def open_stock_purchases_output():
    fixtures_path = 'market/tests/fixtures/'
    with open(f'{fixtures_path}output_stock_buy_transactions.txt') as f:
        return f.read()


def open_stock_sales_json():
    fixtures_path = 'stocks/tests/fixtures/'
    with open(f'{fixtures_path}stock_sales.json') as f:
        return json.loads(f.read())


def open_stock_sales_output():
    fixtures_path = 'market/tests/fixtures/'
    with open(f'{fixtures_path}output_stock_sell_transactions.txt') as f:
        return f.read()


def open_stock_user_input():
    return {
        'code': 'hbor3f',
        'price': '11.92',
        'amount': 50,
        'date': '01/12/2020'
    }


PATH_STOCK = 'stocks.tasks.stock_information.get_stock_object_information'
PATH_STOCK_USER_INPUT = 'stocks.tasks.stock_information.get_user_information'


@mock.patch(PATH_STOCK, return_value=open_stock_json())
@mock.patch(PATH_STOCK_USER_INPUT, return_value=open_stock_user_input())
class TestMarketClie(unittest.TestCase):

    def setUp(self):
        self.runner = CliRunner()

    def test_get_current_stock_information(self, mock_stock_user_input, mock_stock):
        result = self.runner.invoke(main, ['hbor3f'])
        self.assertEqual(result.output, open_stock_information_output())
