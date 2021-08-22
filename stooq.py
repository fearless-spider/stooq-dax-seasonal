from urllib.request import urlretrieve
from datetime import datetime
import pandas as pd
import mplfinance as mpl

# Download daily historical data for DAX
ticker = '^dax'
interval = 'd'
url = f'https://stooq.com/q/d/l/?s={ticker}&i={interval}'
csv_file = ticker + '.csv'

urlretrieve(url, csv_file)

# Read the data
data = pd.read_csv(csv_file, index_col='Date', parse_dates=['Date'], date_parser=lambda x: datetime.strptime(x, '%Y-%m-%d'))

data.tail()

mpl.plot(data.tail(100), type='candle', volume=False)

