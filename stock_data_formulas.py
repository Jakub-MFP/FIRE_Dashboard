# ENTER OBJECTS TO GET CERTAIN STOCK DATA HERE
    # This file will have all the formulas to find the various stock metrics 
    # like daily price, PS , PE , balance sheet info ect. 
    # Any metric anyone wants they can create a class for it here. 

import pandas as pd
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.cryptocurrencies import CryptoCurrencies
from alpha_vantage.techindicators import TechIndicators
from alpha_vantage.sectorperformance import SectorPerformances
from alpha_vantage.alphavantage import AlphaVantage

import time
import random
import numpy as np
import math
import datetime as dt
    # Import stock ticker to be used from quick_stock_analysis.py
from quick_stock_analysis import stock_ticker



### IMPORTS KEY FROM KEYS FILE ###
lines = open('keys').read().splitlines()
keys=random.choice(lines)

ts = TimeSeries (key=keys, output_format = "pandas")



cs = CryptoCurrencies (key=keys, output_format = "pandas")
ti = TechIndicators (key=keys, output_format = "pandas")
sp = SectorPerformances (key=keys, output_format = "pandas")
av = AlphaVantage (key=keys, output_format = "pandas")

demo = "N/A"
### DO NOT EEDIT THIS ###



### CALLING APIs FROM ALPHA VANTAGE TO ORGANIZE INTO INDIVIDUAL DATA POINTS ###
    # https://www.alphavantage.co/documentation/

    ### STOCK TIME SERIES > DAILY ADJUSTED ###
        # Date / Open / High / Low / Close / Adjusted Close / Volume / Dividend / Split
data_daily, meta_data = ts.get_daily_adjusted(symbol=stock_ticker, outputsize ='compact')
    #data_daily['column name'][row number]
data_daily_last_open_price = data_daily['1. open'][0]
data_daily_high_price = data_daily['2. high'][0]
data_daily_low_price = data_daily['3. low'][0]
data_daily_last_adjusted_price = data_daily['5. adjusted close'][0]
data_daily_trading_volume = data_daily['6. volume'][0]
data_daily_divident_amount = data_daily['7. divident amount'][0]






    ### FUNADMENTAL DATA > COMPANY OVERVIEW ###
    # https://www.alphavantage.co/query?function=OVERVIEW&symbol=IBM&apikey=demo
    # NEED TO FIGURE THIS OUT
#data_company_overview, meta_data = av.overview(symbol=stock_ticker, outputsize ='full')



    ### FUNDAMENTAL DATA > INCOME STATEMENT ###
    # https://www.alphavantage.co/query?function=INCOME_STATEMENT&symbol=IBM&apikey=demo
#data_income_statement, meta_data = fd.get_INCOME_STATEMENT(symbol=stock_ticker, outputsize ='compact')



# #Testing Ground




# print(("demo : {}").format(demo))
# print(("demo : {}").format(demo))
# print(("demo : {}").format(demo))
# print(("demo : {}").format(demo))
# print(("demo : {}").format(demo))
# print(("demo : {}").format(demo))