import pandas as pd
from pandas import DataFrame
from pandas import ExcelWriter
import csv
import sqlite3
import time
import datetime
import random
import json
import requests
import os
from datetime import datetime 
from datetime import date
from io import StringIO


### CONNECTING TO DATABASE ###
conn = sqlite3.connect('stockmarket.db')
c = conn.cursor()


### CREATING DATAFRAME WITH STOCK TICKERS ###
    ### OPTION 1 - IMPORTING WITH CSV ###
def stock_csv():
        # Path to CSV File
    file_csv="alpha_vantage_active_stocks2.csv"
        # checking if CSV exists
    if os.path.exists(file_csv):
        stock_csv_file = pd.read_csv (r'{}'.format(file_csv))
    else:
        print ("File",file_csv,"is missing" )
        exit()

    df = pd.DataFrame(stock_csv_file)
    df = df.rename(columns = {"symbol":"stock_ticker", "name":"stock_name", "exchange":"stock_exchange", "ipoDate":"stock_ipoDate", "delistingDate":"stock_delistingDate", "status":"stock_status"})

    now = datetime.now()
    stock_updateTime = now.strftime('%y-%m-%d %H:%M:%S')

    update_table_stocks = """
        INSERT INTO stocks (stock_ticker,
                            stock_name,
                            stock_exchange,
                            stock_ipoDate,
                            stock_delistingDate,
                            stock_status,
                            stock_updateTime
                            )
        VALUES (?, ?, ?, ?, ?, ?, ?)
        ON CONFLICT (stock_ticker) DO UPDATE SET
                stock_name = EXCLUDED.stock_name,
                stock_exchange = EXCLUDED.stock_exchange,
                stock_ipoDate = EXCLUDED.stock_ipoDate,
                stock_delistingDate = EXCLUDED.stock_delistingDate,
                stock_status = EXCLUDED.stock_status,
                stock_updateTIme = EXCLUDED.stock_updateTime
            """

    for i in range(len(df)):
        values = tuple(df.iloc[i])
        #append stock_updateTime to values tuple
        new_value= (*values,stock_updateTime)
        # 6 values in df, 7 in table. missing sending stock_updateTime
        c.execute(update_table_stocks, new_value)
        conn.commit()





    ### OPTION 2 - IMPORTING FROM ALPHA VANTAGE ###
        # https://www.alphavantage.co/documentation/
            # Fundamental Data > Listing And Delisting Status
            # https://www.alphavantage.co/query?function=LISTING_STATUS&apikey=demo
def stock_api():
    base_url = 'https://www.alphavantage.co/query?'
    params = {'function': 'LISTING_STATUS',
            'apikey': '******************'}
    response = requests.get(base_url, params=params)
    
    # create dataframe from json or something
    wrapped_data = StringIO(response.content.decode("utf-8"))
    df = pd.read_csv(wrapped_data)
    df = df.rename(columns = {"symbol":"stock_ticker", "name":"stock_name", "exchange":"stock_exchange", "assetType":"stock_type", "ipoDate":"stock_ipoDate", "delistingDate":"stock_delistingDate", "status":"stock_status"})

    # append current date and time stamp to dataframe
    now = datetime.now()
    stock_updateTime = now.strftime('%y-%m-%d %H:%M:%S')
    
    update_table_stocks = """
        INSERT INTO stocks (stock_ticker,
                            stock_name,
                            stock_exchange,
                            stock_type,
                            stock_ipoDate,
                            stock_delistingDate,
                            stock_status,
                            stock_updateTime
                            )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ON CONFLICT (stock_ticker) DO UPDATE SET 
                stock_name = EXCLUDED.stock_name,
                stock_exchange = EXCLUDED.stock_exchange,
                stock_type = EXCLUDED.stock_type,
                stock_ipoDate = EXCLUDED.stock_ipoDate,
                stock_delistingDate = EXCLUDED.stock_delistingDate,
                stock_status = EXCLUDED.stock_status,
                stock_updateTIme = EXCLUDED.stock_updateTime
            """

    for i in range(len(df)):
        values = tuple(df.iloc[i])
        #append stock_updateTime to values tuple
        new_value= (*values,stock_updateTime)
        # 6 values in df, 7 in table. missing sending stock_updateTime
        c.execute(update_table_stocks, new_value)
        conn.commit() 




### UPDATING DATABASE ###
    # We can choose which option to use to update the database
#stock_csv()
stock_api()



c.close()
conn.close()