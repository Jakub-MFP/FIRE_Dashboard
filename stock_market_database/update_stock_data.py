from alpha_vantage.timeseries import TimeSeries
import pandas as pd
import time
import random
import numpy as np
import math
import datetime as dt
import requests
import os
import json
import sqlite3
from datatime import date


### CONNECTING TO DATABASE ###
conn = sqlite3.connect('stockmarket.db')
c = conn.cursor()



### IMPORT STOCK TICKERS FROM DATABASE ###
    # Import stock_id and stock_tickers from stocks table into a list?
stock_list = []
api_key = 'S1CBJQPC92YX01S8'



### ITERATE TROUGH STOCK TICKERS ###
for stock_ticker, stock_id in stock_list:
    stock_ticker = stock_ticker
    stock_id = stock_id


    ### UPDATING TABLE avData_daily ###
    time.sleep(15) # due to API requests per min constraints
    ts = TimeSeries (key=api_key, output_format = "pandas")
    data_daily, meta_data = ts.get_daily_adjusted(symbol=stock_ticker, outputsize ='full')

    for index, row in date_daily.iterrows():
        daily_date = row['index']
        daily_openPrice = row['1. open']
        daily_highPrice = row['2. high']
        daily_lowPrice = row['3. low']
        daily_adjustedClosingPrice = row['5. adjusted close']
        daily_tradingVolume = row['6. volume']
        daily_lastDividendAmount = row['7. dividend amount']
        daily_updateTime = date.today()

        # I want to update the table with 5000 rows to populate it initially
        # Than the next time it runs I will set date range filters so it only updates the current day
    update_table_avData_daily = """
        INSERT INTO avData_daily (stock_id,
                            daily_date,
                            daily_openPrice,
                            daily_highPrice,
                            daily_lowPrice,
                            daily_adjustedClosingPrice,
                            daily_lastDividendAmount,
                            daily_updateTime
                            )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT (daily_date) DO UPDATE SET 
                stock_id = EXCLUDED.stock_id,
                daily_openPrice = EXCLUDED.daily_openPrice,
                daily_highPrice = EXCLUDED.daily_highPrice ,
                daily_lowPrice = EXCLUDED.daily_lowPrice,
                daily_adjustedClosingPrice = EXCLUDED.daily_adjustedClosingPrice,
                daily_lastDividendAmount = EXCLUDED.daily_lastDividendAmount,
                daily_updateTime = EXCLUDED.daily_updateTime
        """
    c.execute(update_table_avData_daily)


    ### UPDATING TABLE avData_overview ###
    time.sleep(15)
    base_url = 'https://www.alphavantage.co/query?'
    params = {'function': 'OVERVIEW',
            'symbol': stock_ticker,
            'apikey': api_key}
    response_data_overview = requests.get(base_url, params=params)

    overview_assetType = response_data_overview.json()['AssetType']
    overview_marketCapitalization = response_data_overview.json()['MarketCapitalization']
    overview_updateTime = date.today()

    update_table_avData_overview = """
        INSERT INTO avData_overview (stock_id,
                                    overview_assetType,
                                    overview_marketCapitalization,
                                    overview_updateTime        
                            )
        VALUES (?, ?, ?)
            ON CONFLICT (stock_id) DO UPDATE SET 
                overview_assetType = EXCLUDED.overview_assetType,
                overview_marketCapitalization = EXCLUDED.overview_marketCapitalization,
                overview_updateTime = EXCLUDED.overview_updateTime
        """
    c.execute(update_table_avData_overview)

    ### UPDATING TABLE avData_income ###
        # https://www.alphavantage.co/query?function=INCOME_STATEMENT&symbol=IBM&apikey=demo
        # We can have data be <annual> or <quarterly> 
        # date is "fiscalDateEnding"
    time.sleep(15)
    base_url = 'https://www.alphavantage.co/query?'
    params = {'function': 'INCOME_STATEMENT',
            'symbol': stock_ticker,
            'apikey': keys}
    response_data_income = requests.get(base_url, params=params)

        # No idea on how to interact with this JSON in a meaningful way. 
        # To get more recent information it would be
            #data_income_annual_last_fiscalDateEnding = response_data_income.json()['annualReports'][0]['fiscalDateEnding']

        # idk if there is a way to create this into a dataframe or something

    income_reportType = 1 #This could be (1,5) if its an 'quarterlyReport' than its a 1, if its 'annualReports' than its a 5
    income_reportId = 1 # This could be (1,2,3,4,5) if Report Type is 5, than this will also be 5. Otherwise I want to set which quarter the report is for. Might need to set ranges if the fiscalDateNeding falls between  Jan 1 to March 31  than tis report id is 1. 
    income_reportYear = 2020 #this will be the year from the fiscalDateEnding

        #idk how to set these, i just know how to make it the most recent one
    income_fiscalDateEnding = response_data_income.json()['annualReports'][0]['fiscalDateEnding']
    income_totalRevenue = response_data_income.json()['annualReports'][0]['totalRevenue']
    income_updateTime = date.today()


    update_table_avData_income = """
        INSERT INTO avData_income (income_fiscalDateEnding,
                                stock_id,
                                income_reportType,
                                income_reportId,
                                income_reportYear,
                                income_totalRevenue,
                                income_updateTime
                            )
        VALUES (?, ?, ?, ?, ?, ?)
            ON CONFLICT (income_fiscalDateEnding) DO UPDATE SET 
                stock_id = EXCLUDED.stock_id,
                income_reportType = EXCLUDED.income_reportType,
                income_reportId = EXCLUDED.income_reportId,
                income_reportYear = EXCLUDED.income_report_Year,
                income_totalRevenue = EXCLUDED.income_totalRevenue,
                income_updateTime = EXCLUDED.income_updateTime
        """
    c.execute(update_table_avData_income)


c.close()
conn.close()