import plotly.graph_objects as go
from plotly import io
from lumi import get_lumi_series

import pandas as pd
from datetime import datetime
import pytz

def convert(t):
    tz = pytz.timezone('Asia/Bangkok')
    return datetime.fromtimestamp(t, tz)

def plot():
    data = get_lumi_series()
    if not data:
    	return 0
    df = pd.DataFrame(data)
    df['time'] = df.apply(lambda row: convert(row['t']), axis=1)
    fig = go.Figure(data=[go.Candlestick(x=df['time'],
                open=df['o'],
                high=df['h'],
                low=df['l'],
                close=df['c'])])

    png = io.to_image(fig)
    return png


if __name__ == "__main__":
	plot()


