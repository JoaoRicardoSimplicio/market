import click


@click.command()
@click.argument(
    'stock',
    type=str,
    default=None,
    required=False
)
@click.option('--buy', 'action')
@click.option('--sale', 'action')
def main(stock, action):
    if stock:
        pass

    if action:
        pass

if __name__=='__main__':
    main()
