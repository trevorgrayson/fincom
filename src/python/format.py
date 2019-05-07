def format_row(row):
    return ",".join([str(v) for v in row]) + "\n"

def price_scrub(price):
    try:
        if isinstance(price, str):
            return float(price.replace('$', '').replace(',', ''))
        else:
            return price
    except ValueError:
        return 0.0

def ticker_scrub(ticker):
    return ticker.replace(' ', '-')

def is_header(row):
    if row[0] == 'Symbol':
        return True
