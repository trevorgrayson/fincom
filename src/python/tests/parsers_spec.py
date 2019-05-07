from parsers import USAAParser


class TestUSAAParser(object):

    def test_init(self):
        assets =  USAAParser.parse('im_positions.csv')

        print(sum(assets))
