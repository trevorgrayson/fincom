import csv
from models import Portfolio, Position

def portfolio():
    """ Stock market portfolio """

    try:
        with open('portfolio.csv', 'rb') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            positions = [Position(symbol=row[0], quantity=row[2]) 
                for row in reader ]

            return Portfolio(positions)

    except IOError:
        return Portfolio()

def crypto_tokens():
    """ Crypto currency tokens """
    try:
        with open('crypto.csv', 'rb') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            positions = [Position(symbol=row[0], quantity=row[1]) 
                for row in reader]

            return Portfolio(positions)

    except IOError:
        return Portfolio()

def cash_accounts():
    """ Crypto currency tokens """
    try:
        with open('cash.csv', 'rb') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            tokens = dict([(row[0], row[1]) for row in reader])

            return tokens
    except IOError:
        return {}

def checking_records():
    """ Crypto currency tokens """
    with open('bk_download.csv', 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        transactions = dict([(row[0], row[1]) for row in reader])

        return transactions
