import pandas as pd
import numpy as np
from statsmodels.tsa.arima.model import ARIMA

df = pd.read_csv('2019.csv', parse_dates=['Date'], index_col='Date')

model = ARIMA(df, order=(2, 1, 2))
model_fit = model.fit()

forecast = model_fit.forecast(steps=1)

print(forecast)
