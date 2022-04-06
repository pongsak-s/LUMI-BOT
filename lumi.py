import requests
import json
import time
from datetime import datetime
import pytz


CONST_CURRENCY = 'USD'


def get_lumi_series():
    url = 'https://api.bkc.loremboard.finance/charts/history?symbol=LUMI&resolution=5&to='+str(int(time.time()))+'&countback=2&currencyCode='+CONST_CURRENCY
    #print(url)
    response = requests.get(url,
                            headers={'Cache-Control': 'no-cache'})

    try:
        data = json.loads(response.text)
        return data
    except requests.exceptions.Timeout:
        return 0
    except requests.exceptions.TooManyRedirects:
        return 0
    except requests.exceptions.RequestException as e:
        return 0


def get_lumi_price_usd(series = get_lumi_series()):
    if(not series):
        return 0

    try:
        return float(series['c'][-1])
    except:
        return 0


def get_lumi_price(lumi_usd = get_lumi_price_usd()):
    if(not lumi_usd):
        return "error"

    try:
        format_result = "Current Price: {:.4f} {} ".format(lumi_usd, CONST_CURRENCY)
        return format_result
    except:
        return "no data"


if __name__ == "__main__":
    print(get_lumi_price())
    print(get_lumi_series())