import json
import requests

COINDESK = "https://api.coindesk.com/site/headerdata.json?currency=%s" #ETH, BTC

def get_price(symbol):
    url = COINDESK % symbol
    response = requests.get(url)

    if response.status_code == 200:
        data = json.loads(response.text)

        return float(data['bpi']['USD']['rate_float'])
