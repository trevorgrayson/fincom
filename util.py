import csv

def portfolio():
    """ Stock market portfolio """

    try:
        with open('portfolio.csv', 'rb') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            tickers = dict([(row[0].replace(' ', '-'), row[2]) 
                for row in reader]
            )

            return tickers
    except IOError:
        return {}

def crypto_tokens():
    """ Crypto currency tokens """
    try:
        with open('crypto.csv', 'rb') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            tokens = dict([(row[0], row[1]) for row in reader])

            return tokens
    except IOError:
        return {}

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
