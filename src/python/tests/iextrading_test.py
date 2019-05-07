from services import iextrading as iex # import get_stock_values, query_s
from models import Portfolio, Position


class TestiExtrading(object):

    def test_params(self):
        tickers = ['aapl', 'amzn']
        query = {
            'symbols': ",".join(tickers),
            'types': 'quote,news,chart',
            'range': '1m',
            'last': 5
        }

        assert iex.query_s(query) == "symbols=aapl,amzn&range=1m&last=5&types=quote,news,chart" 

    def test(self):
        results = iex.get_stock_values(Portfolio(map(lambda ticker: Position(symbol=ticker, quantity=1), ['aapl', 'amzn', 'gpc'])))

        assert results[0].symbol == 'AAPL'
        # assert isinstance(results[0].value, double)
