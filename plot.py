import plotly.graph_objects as go
import np
from plotly import io
from lumi import get_lumi_series

import pandas as pd
from datetime import datetime
import pytz


def convert(t):
    tz = pytz.timezone('Asia/Bangkok')
    return datetime.fromtimestamp(t, tz)

def plot(data = get_lumi_series()):
    if not data:
    	return 0
    df = pd.DataFrame(data)
    df.drop('v', inplace=True, axis=1)
    df.drop('s', inplace=True, axis=1)
    df = df.astype({'t':'float','o':'float','h':'float','l':'float','c':'float'})
    #print(df.tail().to_string())
    #print( (df[~df.applymap(np.isreal).all(1)]).tail().to_string() )
    df['time'] = df.apply(lambda row: convert(row['t']), axis=1)
    fig = go.Figure(data=[go.Candlestick(x=df['time'],
                open=df['o'],
                high=df['h'],
                low=df['l'],
                close=df['c'])], 
                layout=go.Layout(title=go.layout.Title(text="LUMI Chart")))

    fig.update_layout(xaxis_rangeslider_visible=False)
    png = io.to_image(fig)
    return png


if __name__ == "__main__":
	plot()


