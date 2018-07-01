#!/usr/bin/env python

import StringIO
import csv
from datetime import date, timedelta
import os.path
from util import portfolio, crypto_tokens, cash_accounts
from format import price_scrub

from services import crypto
from services import yahoo
from services import iextrading
import view

FINANCE_URL = "http://finance.yahoo.com/d/quotes.csv?f=snbaopl1&s="
PATH = 'data/%s.val'

today = date.today()
today = today.strftime("%Y-%m-%d")


if __name__ == "__main__":
    portfolio = portfolio()
    stocks = iextrading.get_stock_values(portfolio)
    # yahoo.write(yahoo_body, today)

    stocks = stocks.value

    tokens = crypto_tokens()

    crypto = sum([crypto.get_price(sym) * float(tokens[sym]) 
                  for sym in tokens.keys()])

    cash = sum([float(val) for k, val in cash_accounts().iteritems()])

    nut = stocks + crypto + cash

    view.total("Stocks", stocks)
    view.total("Crypto", crypto)
    view.total("Cash", cash)
    view.total('NUT', nut)

    with open('data/total.hist', 'ab') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow([today, "%7.2f"%nut])
