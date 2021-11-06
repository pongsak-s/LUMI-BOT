import requests
import json
import os
from datetime import date, timedelta


CONST_CURRENCY = 'USD'
CONST_CLIENTID = os.getenv('CLIENTID')

def get_yesterday():
    return (date.today() - timedelta(days=1)).strftime("%G-%m-%d")

def get_usdthb_raw():
    url = "https://apigw1.bot.or.th/bot/public/Stat-ExchangeRate/v2/DAILY_AVG_EXG_RATE/?start_period="+get_yesterday()+"&end_period="+get_yesterday()+"&currency="+CONST_CURRENCY
    response = requests.get(url,
                            headers={'Cache-Control': 'no-cache',
                                     'X-IBM-Client-Id': CONST_CLIENTID})

    try:
        data = json.loads(response.text)
        return data
    except requests.exceptions.Timeout:
        return 0
    except requests.exceptions.TooManyRedirects:
        return 0
    except requests.exceptions.RequestException as e:
        return 0


def get_usdthb():
    raw = get_usdthb_raw()
    if(not raw):
        return 0

    try:
        return float(raw['result']['data']['data_detail'][0]['mid_rate'])
    except:
        return 0


if __name__ == "__main__":
    print(get_yesterday())
    print(get_usdthb())