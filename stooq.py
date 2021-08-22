from urllib.request import urlretrieve
from datetime import datetime
import pandas as pd
import numpy as np
import mplfinance as mpl
import time
from statsmodels.tsa.seasonal import seasonal_decompose

# Download daily historical data for DAX
ticker = '^dax'
interval = 'd'
url = f'https://stooq.com/q/d/l/?s={ticker}&i={interval}'
csv_file = ticker + '.csv'

urlretrieve(url, csv_file)

# Read the data
data = pd.read_csv(csv_file, index_col='Date', parse_dates=['Date'], date_parser=lambda x: datetime.strptime(x, '%Y-%m-%d'))

data.dropna()

data = data.tail(1000)

#mpl.plot(data.tail(100), type='candle', volume=False)

# Descriptive statistics
print(data.describe())

data['OC'] = data['Close']-data['Open']

print(data.describe())

data['OCa'] = data['OC'] - data['OC'].min() + 1
analysis = data[['OCa']].copy()

decompose_result_mult = seasonal_decompose(analysis, model="multiplicative", period=365)

trend = decompose_result_mult.trend
seasonal = decompose_result_mult.seasonal
residual = decompose_result_mult.resid

fig = decompose_result_mult.plot()
fig.savefig('result.png')
