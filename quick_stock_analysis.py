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

### Number seperated by commas ex 1,000,000
def place_value(number):
    return ("{:,}".format(number))

### ASK FOR STOCK TICKER
stock_ticker=input("Enter a stock ticker symbol: ")
stock=yf.Ticker(str(stock_ticker))
stock.info

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

### STOCK MARKET METRICS

    # Historical data
#         # Date , Open, High, Low, Close, Volume, Dividends, Stock Split
#         # Need to add edning date variable, and interval variable
# stock_historical = stock.history(start=start_date, end=end_date, interval="1d")


    # Current Stock Price


    # Current Market Cap
stock.info["marketCap"]

    # Current Revenues From Most Recent Quarter


    # Current Projected Revenues / Maybe User Input


    # Caluclate Price to Sales Ratio


    # Calculate Price to Earnings Ratio



### PRINT OUT RESULTS
print("")
print(" ~~~ QUICK ANALYSIS RESULTS ~~~")
print(("{} , {}").format((stock.info["shortName"]),stock_ticker))
print(("Starting Date is : {}").format(start_date))
print(("Ending Date is : {}").format(end_date))
print("")

print(" /// COMPANY STATS /// ")
print(("Market Sector = {}").format(stock.info["sector"]))
# print(str(stock_historical))
print(("Price Per Share = $ {} ").format(place_value(stock.info["regularMarketPrice"])))
print(("Market Cap = $ {} ").format(place_value(stock.info["marketCap"])))
print(("Trailing Price To Sales Ratio = {}").format(round(stock.info["priceToSalesTrailing12Months"],2)))

print("")
# print(stock.financials)
