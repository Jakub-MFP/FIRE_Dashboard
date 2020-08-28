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
import math

yf.pdr_override()

no_info="No Information Available"

### Number seperated by commas ex 1,000,000
def number_commas(number):
    return ("{:,}".format(number))

### ASK FOR STOCK TICKER ###
stock_ticker = input("Enter a stock ticker symbol: ")
stock = yf.Ticker(str(stock_ticker))
stock.info



### STARTING DATE AND TIME ###
default_date_setting = str((input("Do you want to use default date settings? Y / N :  ")))

    # Default date settings
if default_date_setting == 'Y':
    start_year = 2020
    start_month = 1
    start_day = 1
    end_date = dt.datetime.now()

    # Will ask user to enter start / end date. Along with setting the string for end date
else:
    start_year, start_month, start_day = input("Enter Start DATE YYYY-MM-DD.  ").split('-')
    end_year, end_month, end_day = input("Enter End DATE YYYY-MM-DD.  ").split('-')
    end_date = dt.datetime(int(end_year), int(end_month), int(end_day))
   
   # Sets the string for start date
start_date = dt.datetime(int(start_year), int(start_month), int(start_day))



### CURRENT VALUATION ###
    # User submits the growth rate for the stock
submit_growth_rate = input("What is the current growth rate? (ex 20.50)  ")
submit_growth_rate = int(submit_growth_rate)

    # Converts the submitted growth rate into a decimal
current_growth_rate = submit_growth_rate / 100



### INTRINSIC VAUE METRICS ###
intrinsic_market_cap = 0
intrinsic_stock_price = 0
intrinsic_price_to_sales_ratio = 0


### HYPE VALUE METRICS ###
hype_ratio = 0
hype_stock_price = 0
hype_market_cap = 0
hype_market_years = 0


### FIVE YEAR PROJECTIONS BASED ON PRICE TO SALES RATIO ###
    # NO FAITH IN MARKET OUTLOOK (2x) 
five_year_no_faith_price = 0
five_year_no_faith_total_roi = 0
five_year_no_faith_cagr = 0

    # BELOW MARKET VALUE OUTLOOK (3x) 
five_year_below_market_price = 0
five_year_below_market_total_roi = 0
five_year_below_market_cagr = 0

    # STANDARD MARKET VALUE OUTLOOK (4x) 
five_year_standard_market_price = 0
five_year_standard_market_total_roi = 0
five_year_standard_market_cagr = 0

    # SOME HYPE OUTLOOK (5x) 
five_year_some_hype_price = 0
five_year_some_hype_total_roi = 0
five_year_some_hype_cagr = 0

    # EXEPTIONAL HYPE OUTLOOK (6x) 
five_year_exeptional_hype_price = 0
five_year_exeptional_hype_total_roi = 0
five_year_exeptional_hype_cagr = 0



### PRINT RESULTS ###
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
print(("Current Growth Rate : {} %").format(submit_growth_rate))
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
print(("No Faith In Market Outlook (2x)    | Stock Price : $ {} , Total ROI {}% , CAGR {}%").format(no_info, no_info, no_info))
print(("Below Market Value Outlook (3x)    | Stock Price : $ {} , Total ROI {}% , CAGR {}%").format(no_info, no_info, no_info))
print(("Standard Market Value Outlook (4x) | Stock Price : $ {} , Total ROI {}% , CAGR {}%").format(no_info, no_info, no_info))
print(("Some Hype Outlook (5x)             | Stock Price : $ {} , Total ROI {}% , CAGR {}%").format(no_info, no_info, no_info))
print(("Exceptional Hype Outlook (6x)      | Stock Price : $ {} , Total ROI {}% , CAGR {}%").format(no_info, no_info, no_info))
print("")
