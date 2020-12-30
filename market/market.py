import click
import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

from stocks.tasks.stock_tasks import stock_tasks


@click.command()
@click.argument(
    'stock_code',
    type=str,
    default=None,
    required=False
)
@click.option('--all', 'task', flag_value='all', help='See all your stocks')
@click.option('--buy', 'task', flag_value='buy', help='Pass this flag with stock code to buy')
@click.option('--sell', 'task', flag_value='sell', help='Pass this flag with stock code to sell')
@click.option(
    '--purchases',
    'task',
    flag_value='purchases',
    help='Pass this flag with stock code to see all your purchases'
)
@click.option(
    '--sales',
    'task',
    flag_value='sales',
    help='Pass this flag with stock code to see all your sales'
)
def main(stock_code, task):

    """
        Track and store the value of your stocks and transactions.

        usage: market [stock]

    """

    stock_tasks(stock_code=stock_code, task=task)


if __name__ == "__main__":
    main()
