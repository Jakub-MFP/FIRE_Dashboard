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

no_info="No Information Available"

### Number seperated by commas ex 1,000,000
def number_commas(number):
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


print("")
print("/// QUICK ANALYSIS REPORT ///")
print(("{} , {}").format((stock.info["shortName"]),stock_ticker))
print(("Market Sector : {}").format(stock.info["sector"]))
print(("Investment Type : {}").format(no_info))
print("")

print("/// DATE RANGE ///")
print(("Starting Date is : {}").format(start_date))
print(("Ending Date is : {}").format(end_date))
print("")

print("/// CURRENT VALUATION ///")
print(("Stock Price : $ {} ").format(number_commas(stock.info["regularMarketPrice"])))
print(("Market Cap : $ {} ").format(number_commas(stock.info["marketCap"])))
print(("Trailing PS Ratio : {}").format(round(stock.info["priceToSalesTrailing12Months"],2)))
print(("Current Growth Rate : {}").format(no_info))
print("")

print("/// INTRINSIC VALUE METRICS ///")
print(("Stock Price : {}").format(no_info))
print(("Market Cap : {}").format(no_info))
print(("Price To Sales Metric : {}").format(no_info))
print("")

print("/// HYPE METRICS ///")
print(("Stock Price : {}").format(no_info))
print(("Market Cap  : {}").format(no_info))
print(("Hype Ratio  : {}").format(no_info))
print(("Hype Years  : {}").format(no_info))
print("")

print("/// 5 YEAR PROJECTIONS BASED ON PRICE TO SALES RATIO ///")
print(("Bad Hype Outlook (2x)       | Stock Price : $ {} , Total ROI {}% , CAGR {}%").format(no_info, no_info, no_info))
print(("Below Avg Hype Outlook (3x) | Stock Price : $ {} , Total ROI {}% , CAGR {}%").format(no_info, no_info, no_info))
print(("Average Outlook (4x)        | Stock Price : $ {} , Total ROI {}% , CAGR {}%").format(no_info, no_info, no_info))
print(("Above Average Outlook (5x)  | Stock Price : $ {} , Total ROI {}% , CAGR {}%").format(no_info, no_info, no_info))
print(("Exceptional Outlook (6x)    | Stock Price : $ {} , Total ROI {}% , CAGR {}%").format(no_info, no_info, no_info))
print("")
