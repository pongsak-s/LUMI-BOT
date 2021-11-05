import requests
import json
import time
from datetime import datetime
import pytz


CONST_CURRENCY = 'USD'


def get_lumi_series():
    url = 'https://api.bkc.loremboard.finance/charts/history?symbol=LUMI&resolution=5&to='+str(int(time.time()))+'&countback=2&currencyCode='+CONST_CURRENCY
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


def get_lumi_price():
    series = get_lumi_series()
    if(not series):
        return "error"

    try:
        data = series
        tz = pytz.timezone('Asia/Bangkok')
        format_time = datetime.fromtimestamp(data['t'][-1], tz)
        format_result = "{:.4f} {} at {}".format(data['c'][-1], CONST_CURRENCY, format_time)
        return format_result
    except requests.exceptions.Timeout:
        return "no data"
    except requests.exceptions.TooManyRedirects:
        return "no data"
    except requests.exceptions.RequestException as e:
        return "error"


if __name__ == "__main__":
    print(get_lumi_price())
    print(get_lumi_series())