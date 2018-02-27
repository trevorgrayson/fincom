import csv

def portfolio():
    """ Stock market portfolio """
    with open('portfolio.csv', 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        tickers = dict([(row[0].replace(' ', '-'), row[2]) for row in reader])

        return tickers

def crypto_tokens():
    """ Crypto currency tokens """
    with open('crypto.csv', 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        tokens = dict([(row[0], row[1]) for row in reader])

        return tokens

def cash_accounts():
    """ Crypto currency tokens """
    with open('cash.csv', 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        tokens = dict([(row[0], row[1]) for row in reader])

        return tokens

def checking_records():
    """ Crypto currency tokens """
    with open('bk_download.csv', 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        transactions = dict([(row[0], row[1]) for row in reader])

        return transactions
