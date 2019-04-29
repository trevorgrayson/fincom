class Asset(object):

    def __init__(self, **kwargs):
        self.title = kwargs.get('title')
        self.symbol = kwargs.get('symbol')
        self.price  = kwargs.get('price')
        self.quantity = kwargs.get('quantity')
        
    
    def __add__(self, b):
        return b + self.price

    def to_csv(self):
        return ",".join([self.symbol, str(self.quantity)])

    def __repr__(self):
        return "<Asset symbol={symbol} price={price}>".format(
            symbol=self.symbol,
            price=self.price
        )


class Portfolio(object):
    def __init__(self, positions):
        self.positions = positions

    def keys(self):
        return [pos.symbol for pos in self.positions]

    @property
    def tickers(self):
        return self.keys()

    def __getitem__(self, key):
        return filter(lambda p: p.symbol, self.positions)[0]

class Position(object):
    def __init__(self, **kwargs):
        self.symbol = kwargs.get('symbol')
        self.price = kwargs.get('price')
        self.quantity = kwargs.get('quantity')
