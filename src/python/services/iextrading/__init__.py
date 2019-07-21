import requests
from models import Portfolio, Position

HOSTNAME = 'https://api.iextrading.com/1.0'


def query_s(params):
    return "&".join(["{}={}".format(k, v) for k, v in params.iteritems()])

def get_stock_values(portfolio):
    query = {
        'symbols': ",".join(portfolio.tickers),
        'types': 'quote,news,chart',
        'range': '1m',
        'last': 5
    }

    url = HOSTNAME +\
    '/stock/market/batch?' +\
    query_s(query)

    resp = requests.get(url)
    if resp.status_code == 200:
        params = resp.json()

        return Portfolio([Position(
            symbol=vals['quote']['symbol'],
            price=vals["quote"]["latestPrice"],
            quantity=portfolio[ticker].quantity
        ) for ticker, vals in params.iteritems()])
    else:
        raise Exception("IEXTrading, {}: {}".format(resp.status_code, resp.text))

def get_quote(ticker):
    url = '/stock/%s/quote' % ticker
    resp = requests.get(url)
    params = resp.json()

    return params['latestPrice']

