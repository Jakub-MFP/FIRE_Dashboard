import pandas as pd
import time
import random
import numpy as np
import math
import datetime as dt
import requests
import os
import json
from tabulate import tabulate

############################ STOCK TICKER TO BE ANALYZED ############################ 

stock_ticker = "TSLA"

#stock_ticker = input("PICK OPTION > ")

############################ API ACCESS ############################ 
lines = open('keys').read().splitlines()
keys=random.choice(lines)

    # NEED TO ADD STIRING API FOR CURRENT STOCK PRICES #

base_url = 'https://www.alphavantage.co/query?'
params = {'function': 'OVERVIEW',
		 'symbol': stock_ticker,
		 'apikey': keys}
response_data_overview = requests.get(base_url, params=params)


base_url = 'https://www.alphavantage.co/query?'
params = {'function': 'INCOME_STATEMENT',
		 'symbol': stock_ticker,
		 'apikey': keys}
response_data_income = requests.get(base_url, params=params)


base_url = 'https://www.alphavantage.co/query?'
params = {'function': 'BALANCE_SHEET',
		 'symbol': stock_ticker,
		 'apikey': keys}
response_data_balance = requests.get(base_url, params=params)


base_url = 'https://www.alphavantage.co/query?'
params = {'function': 'CASH_FLOW',
		 'symbol': stock_ticker,
		 'apikey': keys}
response_data_cashflow = requests.get(base_url, params=params)

####################################################################################  

data_custom_current_expectedValue = float(response_data_overview.json()['RevenueTTM']) * 4




print(data_custom_current_expectedValue)
