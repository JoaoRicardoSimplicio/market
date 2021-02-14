Market
===========

Track and store the value of your stocks and transactions

## Installation

**NOTE**: For this to run properly you must have `docker` installed because of `postgres`. If you don't, please refer to [docker-docs](https://docs.docker.com).  If you don't fell familiar with docker, install `postgres` in your machine.

Run the following commands:

```bash
    $ sudo docker-compose up -d --build     # To start containers
    $ virtualenv env --python=python3.8     # Create a virtual environment called env
    $ source env/bin/activate               # Activate the environment
    $ bash setup.sh                         # setup python
```

## Running

### Stocks

Get information about stock by passing the stock code.

You can run the package as follows:

```bash
    (env) $ market STOCK_CODE       # Replace STOCK_CODE by the desired code
```

#### Buy Stock

You can run this command to buy stock:

```bash
    (env) $ market STOCK_CODE --buy
```

Enter the desired quantity when requested

```bash
    Inform the quantity (sale or purchase):
```

#### See your purchases 

You can see all your purchases:

```bash
    (env) $ market STOCK_CODE --purchases
```

#### Sell Stock 

You can run this command to sell stock:

```bash
    (env) $ market STOCK_CODE --sell
```

#### See your sales 

You can see all your sales:

```bash
    (env) $ market STOCK_CODE --sales
```

