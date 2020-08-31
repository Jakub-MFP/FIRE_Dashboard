from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.cryptocurrencies import CryptoCurrencies
from alpha_vantage.techindicators import TechIndicators
from alpha_vantage.sectorperformance import SectorPerformances
from alpha_vantage.alphavantage import AlphaVantage
import pandas as pd
import time
import random
import numpy as np
import math
import datetime as dt
import requests
import os
import json

stock_ticker = input("Enter a stock ticker symbol: ")

### IMPORTS KEY FROM KEYS FILE ###
lines = open('keys').read().splitlines()
keys=random.choice(lines)

ts = TimeSeries (key=keys, output_format = "pandas")
cs = CryptoCurrencies (key=keys, output_format = "pandas")
ti = TechIndicators (key=keys, output_format = "pandas")
sp = SectorPerformances (key=keys, output_format = "pandas")
av = AlphaVantage (key=keys, output_format = "pandas")

base_url = 'https://www.alphavantage.co/query?'
params = {'function': 'OVERVIEW',
		 'symbol': stock_ticker,
		 'apikey': keys}
response_data_overview = requests.get(base_url, params=params)

data_overview_MarketCapitalization = response_data_overview.json()['MarketCapitalization']
print(data_overview_MarketCapitalization)

