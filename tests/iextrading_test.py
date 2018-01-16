from services.iextrading import get_stock_values, query_s


class TestiExtrading(object):

    def test_params(self):
        tickers = ['aapl', 'amzn']
        query = {
            'symbols': ",".join(tickers),
            'types': 'quote,news,chart',
            'range': '1m',
            'last': 5
        }

        assert query_s(query) == "symbols=aapl,amzn&range=1m&last=5&types=quote,news,chart" 

    def test(self):
        results = get_stock_values(['aapl', 'amzn', 'gpc'])

        assert results[0].symbol == 'AAPL'
        # assert isinstance(results[0].value, double)
