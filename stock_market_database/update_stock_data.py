import pandas as pd
import numpy as np
import datetime as dt
from datetime import datetime 
from datetime import date

import time
import random
import math
import requests
import os
import json
import sqlite3

from tabulate import tabulate
from alpha_vantage.timeseries import TimeSeries



### CONNECTING TO DATABASE ###
conn = sqlite3.connect('stockmarket.db')
c = conn.cursor()
api_key = 'S1CBJQPC92YX01S8'

    # Grabs the stock_id and stock_ticker from table called stocks
c.execute('''  
SELECT stock_id, stock_ticker, stock_type FROM stocks
          ''')


    # For each stock_ticker it will connect to each library and update database
for stock_id, stock_ticker, stock_type in c.fetchall():

    stock_id = stock_id
    stock_ticker = stock_ticker
    stock_type = stock_type

    # ### UPDATING TABLE avData_daily ###
    # ts = TimeSeries (key=api_key, output_format = "pandas")
    # data_daily, meta_data = ts.get_daily_adjusted(symbol=stock_ticker, outputsize ='full')

    # for index, row in data_daily.iterrows():
    #     daily_date = str(index)
    #     daily_adjustedClosingPrice = row['5. adjusted close']
    #     daily_tradingVolume = row['6. volume']
    #     daily_lastDividendAmount = row['7. dividend amount']

    #     now = datetime.now()
    #     daily_updateTime = now.strftime('%Y-%m-%d %H:%M:%S')

        # c.execute("SELECT * FROM avData_daily where stock_id=? and daily_date=?", (stock_id, daily_date))
        # if (len(c.fetchall())) == 0: #it mean it dont exist
        #     c.execute("INSERT INTO avData_daily (stock_id, daily_date, daily_adjustedClosingPrice, daily_tradingVolume, daily_lastDividendAmount, daily_updateTime) VALUES(?,?,?,?,?,?)", (stock_id, daily_date, daily_adjustedClosingPrice, daily_tradingVolume, daily_lastDividendAmount, daily_updateTime))
    
    # conn.commit()
    # time.sleep(15)



    ## UPDATING TABLE avData_overview ###
    stock_check = "Stock"
    if (stock_type) == "Stock": #checking if it's a stock or ETF

        base_url = 'https://www.alphavantage.co/query?'
        params = {'function': 'OVERVIEW',
                'symbol': stock_ticker,
                'apikey': api_key}
        response_data_overview = requests.get(base_url, params=params)

        overview_assetType = response_data_overview.json()['AssetType']
        overview_marketCapitalization = response_data_overview.json()['MarketCapitalization']
        now = datetime.now()
        overview_updateTime = now.strftime('%Y-%m-%d %H:%M:%S')

    # c.execute("SELECT * FROM avData_daily where stock_id=?", (stock_id))
    # if (len(c.fetchall())) == 0: #it mean it dont exist
    #     c.execute("INSERT INTO avData_daily (stock_id, daily_date, daily_adjustedClosingPrice, daily_tradingVolume, daily_lastDividendAmount, daily_updateTime) VALUES(?,?,?,?,?,?)", (stock_id, daily_date, daily_adjustedClosingPrice, daily_tradingVolume, daily_lastDividendAmount, daily_updateTime))

    
        c.execute("INSERT INTO avData_overview (stock_id, overview_assetType, overview_marketCapitalization, overview_updateTime) VALUES (?, ?, ?, ?) ON CONFLICT (stock_id) DO UPDATE SET overview_assetType = EXCLUDED.overview_assetType, overview_marketCapitalization = EXCLUDED.overview_marketCapitalization, overview_updateTime = EXCLUDED.overview_updateTime",(stock_id, overview_assetType, overview_marketCapitalization, overview_updateTime))
        conn.commit()
    # update_table_avData_overview = """
    #     INSERT INTO avData_overview (stock_id,
    #                                 overview_assetType,
    #                                 overview_marketCapitalization,
    #                                 overview_updateTime        
    #                         )
    #     VALUES (?, ?, ?, ?)
    #         ON CONFLICT (stock_id) DO UPDATE SET 
    #             overview_assetType = EXCLUDED.overview_assetType,
    #             overview_marketCapitalization = EXCLUDED.overview_marketCapitalization,
    #             overview_updateTime = EXCLUDED.overview_updateTime
    #     """
    # c.execute(update_table_avData_overview)
        print(stock_id, stock_ticker, overview_marketCapitalization, overview_updateTime)
        time.sleep(15)









    # ### UPDATING TABLE avData_income ###
    #     # https://www.alphavantage.co/query?function=INCOME_STATEMENT&symbol=IBM&apikey=demo
    #     # We can have data be <annual> or <quarterly> 
    #     # date is "fiscalDateEnding"
    # time.sleep(15)
    # base_url = 'https://www.alphavantage.co/query?'
    # params = {'function': 'INCOME_STATEMENT',
    #         'symbol': stock_ticker,
    #         'apikey': keys}
    # response_data_income = requests.get(base_url, params=params)

    #     # No idea on how to interact with this JSON in a meaningful way. 
    #     # To get more recent information it would be
    #         #data_income_annual_last_fiscalDateEnding = response_data_income.json()['annualReports'][0]['fiscalDateEnding']

    #     # idk if there is a way to create this into a dataframe or something

    # income_reportType = 1 #This could be (1,5) if its an 'quarterlyReport' than its a 1, if its 'annualReports' than its a 5
    # income_reportId = 1 # This could be (1,2,3,4,5) if Report Type is 5, than this will also be 5. Otherwise I want to set which quarter the report is for. Might need to set ranges if the fiscalDateNeding falls between  Jan 1 to March 31  than tis report id is 1. 
    # income_reportYear = 2020 #this will be the year from the fiscalDateEnding

    #     #idk how to set these, i just know how to make it the most recent one
    # income_fiscalDateEnding = response_data_income.json()['annualReports'][0]['fiscalDateEnding']
    # income_totalRevenue = response_data_income.json()['annualReports'][0]['totalRevenue']
    # income_updateTime = date.today()


    # update_table_avData_income = """
    #     INSERT INTO avData_income (income_fiscalDateEnding,
    #                             stock_id,
    #                             income_reportType,
    #                             income_reportId,
    #                             income_reportYear,
    #                             income_totalRevenue,
    #                             income_updateTime
    #                         )
    #     VALUES (?, ?, ?, ?, ?, ?)
    #         ON CONFLICT (income_fiscalDateEnding) DO UPDATE SET 
    #             stock_id = EXCLUDED.stock_id,
    #             income_reportType = EXCLUDED.income_reportType,
    #             income_reportId = EXCLUDED.income_reportId,
    #             income_reportYear = EXCLUDED.income_report_Year,
    #             income_totalRevenue = EXCLUDED.income_totalRevenue,
    #             income_updateTime = EXCLUDED.income_updateTime
    #     """
    # c.execute(update_table_avData_income)


c.close()
conn.close()