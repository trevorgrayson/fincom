import logging
import re
import pandas
import csv
from glob import glob

SCHWAB = 'data/ingress/schwab.csv'


def collect(symbol, desc, quantity, price,
            change, change_perc, value, *args):
    """
    cash amount is in row[6]
    """
    price = re.sub("[^\d\.]", "", price) 
    quantity = re.sub("[^\d\.]", "", quantity) 
    value = re.sub("[^\d\.]", "", value) 
    try:
        return symbol, float(price), float(quantity)
    except Exception:
        if "Cash" in symbol:
            return "CASH", 1.0, float(value)



def is_record(record):
    return len(record) > 3

def schwab():
    assets = {}
    with open(SCHWAB, 'r') as fp:
        reader = csv.reader(fp, delimiter=',') # , quotechar='|')
        for row in reader:
            if is_record(row):
                try:
                    record = collect(*row)
                    l = assets.get(record[0], [])
                    l.append(record)
                    assets[record[0]] = l
                except Exception as ex:
                    logging.error("failed record {}: {} {}".format(type(ex),
                        "\t".join(row), ex))
    return assets


class MLF:
    def execute(self):
        data = self.load()
        feats = self.features(*data)
        return feats[0]

    def console(self):
        pass


class Schwab(MLF):
    def load(self):
        return schwab(),

    def features(self, df, *args):
        return (df,)

def display(*args):
    print("\t".join(map(str, args)))
        
if __name__ == '__main__':
    ing = Schwab()
    results = ing.execute()

    total = 0
    for symbol, l in results.items():
        for record in l:
            amount = record[1]*record[2]
            total += amount
            display(*record, amount)

    print(total)
