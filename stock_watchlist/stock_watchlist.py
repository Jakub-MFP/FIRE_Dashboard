import pandas as pd
import time
import random
import numpy as np
import math
import requests
import os
import json
import sys
from collections import OrderedDict
from peewee import *
from tabulate import tabulate
import datetime as dt
from datetime import datetime
from datetime import timedelta 


### SETTING UP DATABASE ###
db = SqliteDatabase('stocktest1.db')

class Entry(Model):
    stock_ticker = TextField()
    market_cap = IntegerField()
    #timestamp = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db

### SETTING UP FUNCTIONS ###

def initialize():
    db.connect()
    db.create_tables([Entry], safe=True)


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def menu_loop():
    choice = None

    while choice != 'q':
        clear()
        print("Enter 'q' to quit.")
        for key, value in menu.items(): 
            print('{}) {}'.format(key,value.__doc__))
        choice = input('Action: ').lower().strip()

        if choice in menu:
            clear()
            menu[choice]()





### STOCK WATCH LIST  ###
stock_list = [
    'TSLA', 
    'BA', 
    'MSFT'
]


def add_stock_db():
    """ Update Stock Lists"""
    for stock in stock_list:
        try

def start_api_key():
    """ Starts the download of all stocks"""
    # Sets Alpha Vantage API Key
    keys = open('keys').read()

        # Provides an estimate for how long it will take script to run
    estimate = int((len(stock_list)*60))
    start = datetime.now() + timedelta(seconds=estimate)
    start_time = (start.strftime("%d/%m/%Y %H:%M:%S"))

    print(("Estimated Completion : {} ").format(start_time))
    print("")
    #### ANALYZE STOCKS INSIDE STOCK LIST #####

    for item in stock_list:
        stock_ticker = item
        #timestamp = entry.timestamp.strftime('%A %B %d, %Y %I %M%p')
        time.sleep(2)
        

        base_url = 'https://www.alphavantage.co/query?'
        params = {'function': 'OVERVIEW',
                'symbol': stock_ticker,
                'apikey': keys}
        response_data_overview = requests.get(base_url, params=params)



        # base_url = 'https://www.alphavantage.co/query?'
        # params = {'function': 'INCOME_STATEMENT',
        #         'symbol': stock_ticker,
        #         'apikey': keys}
        # response_data_income = requests.get(base_url, params=params)



        # base_url = 'https://www.alphavantage.co/query?'
        # params = {'function': 'BALANCE_SHEET',
        #         'symbol': stock_ticker,
        #         'apikey': keys}
        # response_data_balance = requests.get(base_url, params=params)



        # base_url = 'https://www.alphavantage.co/query?'
        # params = {'function': 'CASH_FLOW',
        #         'symbol': stock_ticker,
        #         'apikey': keys}
        # response_data_cashflow = requests.get(base_url, params=params)



        ###### DATA POINTS FORUMLAS ######
        data_overview_MarketCapitalization = response_data_overview.json()['MarketCapitalization']



        ###### ANALYSIS OUTPUT ######
        #print("The Market Cap for {} is = {}").format(stock_ticker,data_overview_MarketCapitalization)
        

        # Completion Time
    # end = datetime.now()
    # complete_time = (end.strftime("%d/%m/%Y %H:%M:%S"))
    # print("Estimated Completion : {} ").format(start_time)
    # print("Actual Completion : {} ").format(complete_time)
  

### MENU OPTIONS ###
menu = OrderedDict([
    ('d', start_api_key),

])

### STARTS THE SCRIPT ###
if __name__ == '__main__':
    initialize() 
    menu_loop()