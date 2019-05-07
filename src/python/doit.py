from models import Asset
from transform import usaa


date = '2019-03-13'
folder = 'data/' + date

assets = [Asset(**row) for row in usaa.normalize(folder)]

with open('portfolio.csv', 'w') as folio:
    for asset in assets:
        folio.write(asset.to_csv() + "\n")

total = sum([asset.price * asset.quantity for asset in assets])
print(total)

with open('data/doit.csv', 'a') as out:
    out.write("{}, {}".format(date, total))

