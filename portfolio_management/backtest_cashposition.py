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
### THIS WILL CREATE A PANDAS DATAFRAME OF ALL THE HISTORICAL PRICES ######
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


    # creating pandas dataframe
df = pd.DataFrame(data_daily)



###########################################################################
### CASH POSITION CONDITIONAL STATEMENTS ##################################
### START OF THE LOOP #####################################################
start_year = 2000
start_month = 1
start_day = 1

start=dt.datetime(start_year, start_month, start_day)

current_date=dt.datetime.now()


current_cash = 10000
deposit_amount = 1000
deposit_frequency = 5 #every 7 days
deposit_dates = [] 

for index, row in df.iterrows():
    print(index)


# this list is of dates that a deposit will execute one 
    # we need to create a loop that will append 7 week to the current date and generate a list of all mondays
    # If monday is closed for trading, than we will use next avaiable trading day
    # than it resets back to original 
    # print out the generated deposit dates to test if this works 



count_trades = 0 #number of times 
count_deposits = 0#count number of deposits
count_cash_deposited = 0# count total value of cash that was depoisited 
count_profit = 0 #total profit of portfolio

current_shares_count = 0 # total number of shares owend
current_stock_price = 0 # current stock market price


# for i in df.index:
     
#     current_trading_date = 0# the next date in the loop trough the dataframe
#     current_stock_price = 0# the next stock price in  the loop troough the dataframe
#     current_market_all_time_high =0 # this needs to be an if statement
#         # if current price is above market high than set new current_market_all_time_high
#         # if its not ,t han the current one stays 
#     current_market_change = current_stock_price - current_market_all_time_high

#     # Setting market status
#     current_market_status = current_market_change - current_market_all_time_high
    
#     current_cash_required = # loop based on current marekt status
#         if current_market_status > 0 than current_cash_required = 0.30
#         elif current_market_status < 0  >=-5 than current_cash_required = 0.25
#         elif current_market_status < -5  >=-10 than current_cash_required = 0.20
#         elif current_market_status < -15  >=-15 than current_cash_required = 0.10


#     # now that we know market status, we need see if we can deposit or not
#     if current_trading_date == a date inside the lsit deposit_dates:
#         current_cash =+ deposit_amount # we deposit the amoutn set into current cash
#     elif continue 

#     current_cash_equity = current_cash / current_portfolio_value
    
#     # now we need to figure out if we need to buy shares or not
#     if current_cash_equity > required_cash_equity
#         stock_purchase_cash = current_cash_equity - required_cash_equity
#         total_shares_purchased = stock_purchase_cash / current_stock_price
#         current_shares_count =+ total_shares_purchased

#     # Now we set current portfolio value 
#     current_portfolio_value = (current_shares_count * current_stock_price) + current_cash

#     # now we add all of this data to new dataframe that will track the results for each day
#         # save date, and all the metrics that where set bc of this 

# # Now at the end print out the to tal profit, total tradess, ect 



    # ###########################################################################
    # ### SENDING UPDATES TO DATABASE ###########################################
    # insert_statement = """
    # INSERT INTO stocks (current_date,
    #                     deposit_amount,
    #                     dividend_amount,
    #                     current_market,
    #                     cash_req,
    #                     current_cash_equity,
    #                     stock_price_open,
    #                     stock_purchase_value,
    #                     stock_price_close,
    #                     stock_position,
    #                     stock_value,
    #                     cash_position,
    #                     portfolio_value,
    #                     total_dividend,
    #                     current_porit,
    #                     current_roi,
    #                     current_CAGR
                    

    #                     )
    # VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    # DO UPDATE SET 
    #         current_date = current_date,
    #         deposit_amount = deposit_amount,
    #         dividend_amount = dividend_amount,
    #         current_market = current_market,
    #         current_cash_req = current_cash_req,
    #         cash_equity = cash_equity,
    #         stock_price_open = stock_price_open,
    #         stock_purchase_value = stock_purchase_value,
    #         stock_price_close = stock_price_close,
    #         stock_position = stock_position,
    #         stock_value = stock_value,
    #         cash_position = cash_position,
    #         portfolio_value = portfolio_value,
    #         total_dividend = total_dividend,
    #         current_profit = current_profit,
    #         current_roi = current_roi,
    #         current_CAGR = current_CAGR,

    #     """



    # c.execute(insert_statement, values)
    # conn.commit()


###########################################################################
### CLOSE CONNECTION TO DATABASE ##########################################
c.close()
conn.close()