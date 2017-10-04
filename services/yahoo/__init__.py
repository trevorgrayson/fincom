import requests
import csv

FINANCE_URL = "http://finance.yahoo.com/d/quotes.csv?f=snbaopl1&s="
PATH = 'data/%s.val'

def get_stock_values(tickers):
    url = FINANCE_URL + "+".join(tickers)

    response = requests.get(url)

    if response.status_code == 200:
        return response.text
    else:
        raise StandardError("HTTP %s whoops!" % response.status_code)

def write(body, day):
    fp = open(PATH%day, 'w')
    fp.write(body)
    fp.close()

def read(day):
    with open(PATH%day, 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        return dict([(row[0], row[6]) for row in reader])
