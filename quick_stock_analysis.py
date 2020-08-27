import pandas as pd
from pandas_datareader import data as pdr
import numpy as np
import yfinance as yf
import datetime as dt
from pandas_datareader import data as pdr
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import os
from pandas import ExcelWriter

yf.pdr_override()

### ASK FOR STOCK TICKER
stock_ticker=input("Enter a stock ticker symbol: ")
stock=yf.Ticker(str(stock_ticker))

### ASK FOR STARTING AND ENDING DATE
default_date_setting = str((input("Do you want to use default date settings? Y / N :  ")))

    # Default date settings
if default_date_setting == 'Y':
    start_year=2020
    start_month=1
    start_day=1
    end_date=dt.datetime.now()

    # Will ask user to enter start / end date. Along with setting the string for end date
else:
    start_year, start_month, start_day = input("Enter Start DATE YYYY-MM-DD.  ").split('-')
    end_year, end_month, end_day = input("Enter End DATE YYYY-MM-DD.  ").split('-')
    end_date=dt.datetime(int(end_year),int(end_month),int(end_day))
   
   # Sets the string for start date
start_date=dt.datetime(int(start_year),int(start_month),int(start_day))

    # Historical data
        # Date , Open, High, Low, Close, Volume, Dividends, Stock Split
        # Need to add edning date variable, and interval variable
stock_historical = stock.history(start=start_date, end=end_date, interval="1d")


### PRINT OUT RESULTS
print("")
print(("Stock Ticker  < {} > , Starting Date is : {}").format(stock_ticker, start_date))
print(("Stock Ticker  < {} > , Ending Date is : {}").format(stock_ticker, end_date))
print("")
print(str(stock_historical))