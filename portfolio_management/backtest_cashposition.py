import pandas as pd
from pandas import DataFrame
import json
import requests
import sqlite3
import time
import datetime
from datetime import datetime as dt
from alpha_vantage.timeseries import TimeSeries

### CONNECT TO SQLITE DATABASE ###
conn = sqlite3.connect('backtest.db')
c = conn.cursor()



### CREATE DATABASE TABLES ###
createTable_report = """
    CREATE TABLE IF NOT EXISTS 
        report( 
            report_id INT, 
            current_date TEXT,
            deposit_amount INT,
            dividend_amount INT,
            current_market INT, 
            investment_req INT, 
            cash_req INT,
            current_cash_equity INT,
            stock_price_open INT,
        >>> stock_purchase_value INT,
            stock_price_close INT,
            stock_position INT,
            stock_value INT,
            cash_position INT,
            portfolio_value INT,
            total_dividend INT,
            current_profit INT,
            current_ROI INT,
            current_CAGR INT
    )
"""
c.execute(createTable_report)

