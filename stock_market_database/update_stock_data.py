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
SELECT stock_id, stock_ticker, stock_type FROM stocks WHERE stock_id BETWEEN 1,5
          ''')


    # For each stock_ticker it will connect to each library and update database
for stock_id, stock_ticker, stock_type in c.fetchall():

    stock_id = stock_id
    stock_ticker = stock_ticker
    stock_type = stock_type


    ### UPDATING TABLE avData_daily ###
    ts = TimeSeries (key=api_key, output_format = "pandas")
    data_daily, meta_data = ts.get_daily_adjusted(symbol=stock_ticker, outputsize ='full')

    for index, row in data_daily.iterrows():
        daily_date = str(index)
        daily_adjustedClosingPrice = row['5. adjusted close']
        daily_tradingVolume = row['6. volume']
        daily_lastDividendAmount = row['7. dividend amount']

        now = datetime.now()
        daily_updateTime = now.strftime('%Y-%m-%d %H:%M:%S')

        c.execute("SELECT * FROM avData_daily where stock_id=? and daily_date=?", (stock_id, daily_date))
        if (len(c.fetchall())) == 0: #it mean it dont exist
            c.execute("INSERT INTO avData_daily (stock_id, daily_date, daily_adjustedClosingPrice, daily_tradingVolume, daily_lastDividendAmount, daily_updateTime) VALUES(?,?,?,?,?,?)", (stock_id, daily_date, daily_adjustedClosingPrice, daily_tradingVolume, daily_lastDividendAmount, daily_updateTime))

    print(stock_ticker)
    conn.commit()
    time.sleep(15)


    ### UPDATING TABLE avData_overview ###
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
    
        c.execute("INSERT INTO avData_overview (stock_id, overview_assetType, overview_marketCapitalization, overview_updateTime) VALUES (?, ?, ?, ?) ON CONFLICT (stock_id) DO UPDATE SET overview_assetType = EXCLUDED.overview_assetType, overview_marketCapitalization = EXCLUDED.overview_marketCapitalization, overview_updateTime = EXCLUDED.overview_updateTime",(stock_id, overview_assetType, overview_marketCapitalization, overview_updateTime))
        conn.commit()

        print(stock_id, stock_ticker, overview_marketCapitalization, overview_updateTime)
        time.sleep(15)


    ### UPDATING TABLE avData_income ###
        # https://www.alphavantage.co/query?function=INCOME_STATEMENT&symbol=IBM&apikey=demo
        # We can have data be <annual> or <quarterly> 
        # date is "fiscalDateEnding"
    response_range = np.arange(0,50,1) #setting possible inputs for json

    if (stock_type) == "Stock": #checking if it's a stock or ETF

        base_url = 'https://www.alphavantage.co/query?'
        params = {'function': 'INCOME_STATEMENT',
                'symbol': stock_ticker,
                'apikey': api_key}
        response = requests.get(base_url, params=params)

        try:
            for i in response_range:
                income_fiscalDateEnding = response.json()['annualReports'][i]['fiscalDateEnding']
                income_reportID  = 5
                income_reportYear = str(income_fiscalDateEnding[0:4])
                income_totalRevenue = response.json()['annualReports'][i]['totalRevenue']
                
                now = datetime.now()
                income_updateTime = now.strftime('%Y-%m-%d %H:%M:%S')

                c.execute("SELECT * FROM avData_income where stock_id=? and income_fiscalDateEnding=?", (stock_id, income_fiscalDateEnding))
                if (len(c.fetchall())) == 0: #it mean it dont exist
                    c.execute("INSERT INTO avData_income (stock_id, income_reportID , income_reportYear, income_fiscalDateEnding, income_totalRevenue, income_updateTime) VALUES (?, ?, ?, ?, ?, ?)",(stock_id, income_reportID , income_reportYear, income_fiscalDateEnding, income_totalRevenue, income_updateTime))
                conn.commit()

                #print(income_fiscalDateEnding,income_report_id, income_reportYear, income_totalRevenue, income_updateTime)
        except IndexError:
            print('No More Annual Reports')

        try:
            for i in response_range:
                income_fiscalDateEnding = str(response.json()['quarterlyReports'][i]['fiscalDateEnding'])
                fiscalDate = str(income_fiscalDateEnding[5:10])
                if (fiscalDate) == '03-31':
                    income_reportID = 1
                if (fiscalDate) == '06-30':
                    income_reportID  = 2
                if (fiscalDate) == '09-30':
                    income_reportID  = 3
                if (fiscalDate) == '12-31':
                    income_reportID  = 4
                income_reportYear = str(income_fiscalDateEnding[0:4])
                income_totalRevenue = response.json()['quarterlyReports'][i]['totalRevenue']
                
                now = datetime.now()
                income_updateTime = now.strftime('%Y-%m-%d %H:%M:%S')

                c.execute("SELECT * FROM avData_income where stock_id=? and income_fiscalDateEnding=?", (stock_id, income_fiscalDateEnding))
                if (len(c.fetchall())) == 0: #it mean it dont exist
                    c.execute("INSERT INTO avData_income (stock_id, income_reportID , income_reportYear, income_fiscalDateEnding, income_totalRevenue, income_updateTime) VALUES (?, ?, ?, ?, ?, ?)",(stock_id, income_reportID , income_reportYear, income_fiscalDateEnding, income_totalRevenue, income_updateTime))
                conn.commit()

                #print(fiscalDateEnding,income_report_id, income_reportYear, income_totalRevenue, income_updateTime)
        except IndexError:
            print('No More Quarterly Reports')

        time.sleep(15)
        print(stock_ticker)
        # c.execute("SELECT * FROM avData_daily where stock_id=? and income_fiscalDateEnding=?", (stock_id, income_fiscalDateEnding))
        # if (len(c.fetchall())) == 0: #it mean it dont exist
        #     c.execute("INSERT INTO avData_income (stock_id, income_report_id, income_reportYear, income_fiscalDateEnding, income_totalRevenue, income_updateTime) VALUES (?, ?, ?, ?, ?, ?)",(stock_id, income_report_id, income_reportYear, income_fiscalDateEnding, income_totalRevenue, income_updateTime))

        



#         update_table_avData_income = """
#             INSERT INTO avData_income (income_fiscalDateEnding,
#                                     stock_id,
#                                     income_reportType,
#                                     income_reportId,
#                                     income_reportYear,
#                                     income_totalRevenue,
#                                     income_updateTime
#                                 )
#             VALUES (?, ?, ?, ?, ?, ?)
#                 ON CONFLICT (income_fiscalDateEnding) DO UPDATE SET 
#                     stock_id = EXCLUDED.stock_id,
#                     income_reportType = EXCLUDED.income_reportType,
#                     income_reportId = EXCLUDED.income_reportId,
#                     income_reportYear = EXCLUDED.income_report_Year,
#                     income_totalRevenue = EXCLUDED.income_totalRevenue,
#                     income_updateTime = EXCLUDED.income_updateTime
#             """
#         c.execute(update_table_avData_income)
#         conn.commit()
#         time.sleep(15)

c.close()
conn.close()