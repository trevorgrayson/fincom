import util


class TestUtil(object):

    def test_portfolio(self):
        portfolio = util.portfolio()

        assert portfolio[0].symbol == 'GPC'
        
