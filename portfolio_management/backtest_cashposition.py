import pandas as pd
from pandas import DataFrame
import json
import requests
import sqlite3
import time
import datetime
from datetime import datetime as dt
from alpha_vantage.timeseries import TimeSeries


###########################################################################
### CONNECT TO SQLITE DATABASE ############################################
conn = sqlite3.connect('backtest.db')
c = conn.cursor()



###########################################################################
### CREATE DATABASE TABLES ################################################
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
            stock_purchase_value INT,
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



###########################################################################
### ALPHA VANTAGE API #####################################################
    # https://www.alphavantage.co/documentation/
stock_ticker = 'SPY'
api_key = 'OKEQLECOMW6HJ7R0'

    # daily stock price using pandas data frame
ts = TimeSeries (key=api_key, output_format = "pandas")

    # Date / Open / High / Low / Close / Adjusted Close / Volume / Dividend / Split
data_daily, meta_data = ts.get_daily_adjusted(symbol=stock_ticker, outputsize ='full')
    
    # data_daily['column name'][row number]
stock_price_open = data_daily['1. open'][0]
stock_price_close = data_daily['5. adjusted close'][0]
dividend_amount = data_daily['7. dividend amount'][0]



###########################################################################
### CASH POSITION CONDITIONAL STATEMENTS ##################################
    # Need to keep stock all time high and the diffence from it daily in database
        # If the stock keeps going up, than there is a new recent high
        # if the stock drops from $100 to $90 than it is a drop of 10% from ATH
            # If stock goes to $95 , than it is -5% from ATH

    # If current_market greater than  0%+ 
        # Than investment_req  = 30%

    
    # If current_market down 5%
        # Than investment_req  = 25%


    # If current_market down 10% 
        # Than investment_req  = 20%


    # If current_market down 15% 
        # Than investment_req  = 15%


    # If current_market down 25% 
        # Than investment_req  = 10%
    
    # If ccurrent_market down 30%+ 
        # Than investment_req  = 5%
    
    # If current_market down 35%+ 
        # Than investment_req = 0%



###########################################################################
### STARTING DATES ########################################################
start_year= 2000
start_month= 1
start_day= 1

start=dt.datetime(start_year, start_month, start_day)

current_date=dt.datetime.now()



###########################################################################
### STARTING AMOUNTS AND DEPOSITS #########################################
start_amount = 10000
monthly_deposit = 1000 #total amount of money deposited into portfolio each month

dca_weekly = monthly_deposit / 4
dca_biweekly = monthly_deposit / 2
dca_monthly = monthly_deposit

dca_freq = dca_biweekly #how often we deposit money into portfolio

deposit_amount = 0 #Check if today is the day we are suppoed to deposit cash, if it is than deposit the amount based on dca_freq.



###########################################################################
### CURRENT PORTFOLIO VALUE ###############################################
current_shares = 17.533 #from database
current_position_value = float(current_stock_price) * float(current_shares) #total value of SPY shares (fractional shares allowed in simulation)

current_cash_value = 3500 # total amount of cash that hasn't been invested
current_portfolio_value = float(current_position_value + current_cash_value)


cash_req = float(investment_req * current_portfolio_value)
current_cash_equity = float(current_cash_value / current_portfolio_value)
cash_to_invest_next_day = float((current_cash_equity - cash_req) * current_portfolio_value) # the amount of cash that will be spent on shares next day



###########################################################################
### SENDING UPDATES TO DATABASE ###########################################
insert_statement = """
INSERT INTO stocks (current_date,
                    deposit_amount,
                    dividend_amount,
                    current_market,
                    investment_req,
                    cash_req,
                    current_cash_equity,
                    stock_price_open,
                    stock_purchase_value,
                    stock_price_close,
                    stock_position,
                    stock_value,
                    cash_position,
                    portfolio_value,
                    total_dividend,
                    current_porit,
                    current_roi,
                    current_CAGR
                   

                    )
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
DO UPDATE SET 
        current_date = current_date,
        deposit_amount = deposit_amount,
        dividend_amount = dividend_amount,
        current_market = current_market,
        investment_req = investment_req,
        current_cash_req = current_cash_req,
        cash_equity = cash_equity,
        stock_price_open = stock_price_open,
        stock_purchase_value = stock_purchase_value,
        stock_price_close = stock_price_close,
        stock_position = stock_position,
        stock_value = stock_value,
        cash_position = cash_position,
        portfolio_value = portfolio_value,
        total_dividend = total_dividend,
        current_profit = current_profit,
        current_roi = current_roi,
        current_CAGR = current_CAGR,

    """



c.execute(insert_statement, values)
conn.commit()


###########################################################################
### CLOSE CONNECTION TO DATABASE ##########################################
c.close()
conn.close()