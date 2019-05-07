import csv
from models import Asset


class USAAParser(object):

  @staticmethod
  def parse(filename):
    with open(filename, 'rb') as csvfile:
      reader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
      assets = []

      return map(lambda row: Asset(
            symbol=row.get('Symbol'),
            quantity=row.get('Quantity'),
            price=row.get('Price')
        ), reader)

  @staticmethod
  def list_files():
    return Dir.glob("downloads/im_pos*")
