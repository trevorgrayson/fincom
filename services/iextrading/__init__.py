import requests
from models import Portfolio, Position

hostname = 'https://api.iextrading.com/1.0'


def query_s(params):
    return "&".join(["{}={}".format(k, v) for k, v in params.iteritems()])

def get_stock_values(portfolio):
    query = {
        'symbols': ",".join(portfolio.tickers),
        'types': 'quote,news,chart',
        'range': '1m',
        'last': 5
    }

    url = hostname +\
    '/stock/market/batch?' +\
    query_s(query)

    resp = requests.get(url)
    params = resp.json()

    return Portfolio([Position(
        symbol=vals['quote']['symbol'],
        price=vals["quote"]["latestPrice"],
        quantity=portfolio[ticker].quantity
    ) for ticker, vals in params.iteritems()])

def get_quote(ticker):
    url = '/stock/%s/quote' % ticker
    resp = requests.get(url)
    params = resp.json()

    return params['latestPrice']

# {
#     "symbol": "AAPL",
#     "companyName": "Apple Inc.",
#     "primaryExchange": "Nasdaq Global Select",
#     "sector": "Technology",
#     "calculationPrice": "tops",
#     "open": 154,
#     "openTime": 1506605400394,
#     "close": 153.28,
#     "closeTime": 1506605400394,
#     "latestPrice": 158.73,
#     "latestSource": "Previous close",
#     "latestTime": "September 19, 2017",
#     "latestUpdate": 1505779200000,
#     "latestVolume": 20567140,
#     "iexRealtimePrice": 158.71,
#     "iexRealtimeSize": 100,
#     "iexLastUpdated": 1505851198059,
#     "delayedPrice": 158.71,
#     "delayedPriceTime": 1505854782437,
#     "previousClose": 158.73,
#     "change": -1.67,
#     "changePercent": -0.01158,
#     "iexMarketPercent": 0.00948,
#     "iexVolume": 82451,
#     "avgTotalVolume": 29623234,
#     "iexBidPrice": 153.01,
#     "iexBidSize": 100,
#     "iexAskPrice": 158.66,
#     "iexAskSize": 100,
#     "marketCap": 751627174400,
#     "peRatio": 16.86,
#     "week52High": 159.65,
#     "week52Low": 93.63,
#     "ytdChange": 0.3665,
# }
