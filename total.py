#!/usr/bin/env python -s

import StringIO
import csv
from datetime import date, timedelta
import os.path
from util import crypto_tokens, cash_accounts
# from util import portfolio
from services.google import sheets
from format import price_scrub

from services import crypto
from services import yahoo
from services import iextrading
import view

# FINANCE_URL = "http://finance.yahoo.com/d/quotes.csv?f=snbaopl1&s="
# PATH = 'data/%s.val'

today = date.today()
today = today.strftime("%Y-%m-%d")


if __name__ == "__main__":
    portfolio = sheets.portfolio()

    portfolio = iextrading.get_stock_values(portfolio)

    stocks = portfolio.value

    tokens = crypto_tokens()
    tokens = crypto.price_portfolio(tokens)

    crypto = tokens.value

    cash = sum([float(val) for k, val in cash_accounts().iteritems()])

    nut = stocks + crypto + cash

    view.total("Stocks", stocks)
    view.total("Crypto", crypto)
    view.total("Cash", cash)
    view.total('NUT', nut)

    with open('data/total.hist', 'ab') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow([today, "%7.2f"%nut])

