import bs4
from django.test import TestCase
from unittest import mock

from stocks.services.infomoney import StockInformationInfoMoney


def open_infomoney_page():
    fixtures_path = 'stocks/tests/services/fixtures/'
    with open(f'{fixtures_path}infomoney_page_hbor3f.html') as f:
        return f.read()


PATH_INFO_MONEY_CONTENT_PAGE = 'stocks.services.infomoney.StockInformationInfoMoney.get'


@mock.patch(PATH_INFO_MONEY_CONTENT_PAGE, return_value=open_infomoney_page())
class TestInfoMoney(TestCase):

    def setUp(self):
        self.stock_information_info_money = StockInformationInfoMoney(
            url='https://www.infomoney.com.br/cotacoes/helbor-hbor3f/grafico/',
            code='hbor3f'
        )

    def test_initialize_with_wrong_url(self, mock_info_money_content_page):
        with self.assertRaises(Exception) as context:
            StockInformationInfoMoney(url='https://wwww.google.com', code='hbor3f')
        self.assertTrue('https://wwww.google.com is not valid url' in str(context.exception))

    def test_get_infomoney_content(self, mock_info_money_content_page):
        self.assertIsInstance(self.stock_information_info_money.content, bs4.BeautifulSoup)

    def test_get_infomoney_price(self, mock_info_money_content_page):
        self.assertEqual(self.stock_information_info_money.price, '11,75')

    def test_get_infomoney_highest_price_day(self, mock_info_money_content_page):
        self.assertEqual(self.stock_information_info_money.highest_price_day, '11,75')

    def test_get_infomoney_lowest_price_day(self, mock_info_money_content_page):
        self.assertEqual(self.stock_information_info_money.lowest_price_day, '11,75')

    def test_get_infomoney_day_variation(self, mock_info_money_content_page):
        self.assertEqual(self.stock_information_info_money.day_variation, None)
