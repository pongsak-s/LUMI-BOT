import requests
import json
import time
from datetime import datetime
import pytz


def get_lumi_price():
    currency = 'USD'
    url = 'https://api.bkc.loremboard.finance/charts/history?symbol=LUMI&resolution=5&to='+str(int(time.time()))+'&countback=2&currencyCode='+currency
    response = requests.get(url,
                            headers={'Cache-Control': 'no-cache'})

    try:
        data = json.loads(response.text)
        tz = pytz.timezone('Asia/Bangkok')
        format_time = datetime.fromtimestamp(data['t'][-1], tz)
        format_result = "{:.4f} {} at {}".format(data['c'][-1], currency, format_time)
        return format_result
    except requests.exceptions.Timeout:
        return "no data"
    except requests.exceptions.TooManyRedirects:
        return "no data"
    except requests.exceptions.RequestException as e:
        return "error"


if __name__ == "__main__":
	print(get_lumi_price())