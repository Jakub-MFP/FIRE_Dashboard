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
            cash_req INT,
            current_cash_equity INT,
            cash_investment_req INT,
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
### START OF THE LOOP #####################################################
    # Need to keep stock all time high and the diffence from it daily in database
        # If the stock keeps going up, than there is a new recent high
        # if the stock drops from $100 to $90 than it is a drop of 10% from ATH
            # If stock goes to $95 , than it is -5% from ATH

current_market = 0 #if the market is down or up how much
cash_req = 0 # how much cash do we need to keep on hand
starting_cash_options = [0.50, 0.45, 0.40, 0.35, 0.30, 0.25, 0.20, 0.15, 0.10, 0.05]

for i in starting_cash_options:
    starting_cash_req = i

    while True:
        if starting_cash_req == 0.50:
            while True:
                

                

        elif starting_cash_req == 0.45:

            continue

        elif starting_cash_req == 0.40:

            continue

        elif starting_cash_req == 0.35:

            continue

        elif starting_cash_req == 0.30:

            continue

        elif starting_cash_req == 0.25:

            continue

        elif starting_cash_req == 0.20:

            continue

        elif starting_cash_req == 0.15:

            continue

        elif starting_cash_req == 0.10:

            continue

        elif starting_cash_req == 0.05:

            continue
    break


        # Current Market is 0 or higher than loop trough cash options
            #cash_options
        
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
    start_year = 2000
    start_month = 1
    start_day = 1

    start=dt.datetime(start_year, start_month, start_day)

    current_date=dt.datetime.now()



    ###########################################################################
    ### STARTING AMOUNTS AND DEPOSITS #########################################
    start_amount = 10000 #starting deposit amount
    monthly_deposit = 1000 #amount of money deposited each month

    dca_weekly = monthly_deposit / 4 # how much money we deposit each week
    dca_biweekly = monthly_deposit / 2 # how much money we deposit bi-weekly
    dca_monthly = monthly_deposit # how much money we deposit on a monthly basis

    dca_freq = dca_biweekly #how often we deposit money into portfolio, this is a setting

    deposit_amount = 0 #Check if today is the day we are suppoed to deposit cash, if it is than deposit the amount based on dca_freq.



    ###########################################################################
    ### CURRENT PORTFOLIO VALUE ###############################################
    current_shares = 17.533 #get this number from database
    current_position_value = float(stock_price_open) * float(current_shares) #total value of SPY shares (fractional shares allowed in simulation)

    cash_position = 3500 # total amount of cash that hasn't been invested
    current_portfolio_value = float(current_position_value + cash_position)



    ###########################################################################
    ### INVESTMENT REQ ########################################################
    cash_investment_req = float(cash_req * current_portfolio_value) # how much cash $ we need to invest in the next period
    current_cash_equity = float(cash_position / current_portfolio_value)
    cash_to_invest_next_day = float((current_cash_equity - cash_investment_req) * current_portfolio_value) # the amount of cash that will be spent on shares next day



    ###########################################################################
    ### SENDING UPDATES TO DATABASE ###########################################
    insert_statement = """
    INSERT INTO stocks (current_date,
                        deposit_amount,
                        dividend_amount,
                        current_market,
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