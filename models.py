class Asset(object):

    def __init__(self, **kwargs):
        self.title = kwargs.get('title')
        self.symbol = kwargs.get('symbol')
        self.price  = kwargs.get('price')
        self.quantity = kwargs.get('quantity')
        
    
    def __add__(self, b):
        return b + self.price

    def __repr__(self):
        return "<Asset symbol={symbol} price={price}>".format(
            symbol=self.symbol,
            price=self.price
        )
