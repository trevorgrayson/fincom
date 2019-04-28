from models import Asset


class TestAsset(object):

    def test_init(self):
        price = 1.23
        a = Asset(price=price)
        assert a.price == price
