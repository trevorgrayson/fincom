class Portfolio(object):

    def __init__(self, positions=None):
        if not positions:
            positions = {}

        self.positions = dict([(pos.symbol, pos)
            for pos in positions])

    def __getitem__(self, symbol):
        results = filter(lambda sym: sym == symbol, self.tickers)

        if results:
            return self.positions[results[0]]

    @property
    def tickers(self):
        return self.positions.keys()

    @property
    def value(self):
        return sum(map(lambda pos: pos.value,
            self.positions.values()
        ))


class Position(object):
    
    def __init__(self, **kwargs):
        self.quantity = kwargs.get('quantity', 0.0)
        self.price  = kwargs.get('price', 0.0)
        self.symbol = kwargs.get('symbol')
        
        if isinstance(self.symbol, str):
            self.symbol = self.symbol.replace(' ', '-')

        if isinstance(self.quantity, str):
            self.quantity = float(self.quantity.replace(',', ''))

    @property
    def value(self):
        return float(self.quantity) * float(self.price)

    def __str__(self):
        return "<Position sym={} qty={} price={}>".format(self.symbol, self.quantity, self.price)


    def __repr__(self):
        return str(self)
