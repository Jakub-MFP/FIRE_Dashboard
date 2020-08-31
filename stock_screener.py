# THIS FILE IS THE STOCK SCREENER SCRIPT

import pandas as pd
import time
import random
import numpy as np
import math
import datetime as dt
import requests
import os
import json

# Lists
stock_list = []
default_list=['TSLA', 'BA', 'MSFT', 'AAPL']

def user_help(): # Help commands during INPUT command
    print("""
/// HELP COMMANDS FOR INPUT ///
Enter 'DONE' to stop adding or removing stocks.
Enter 'SHOW' to see all the stocks. 
Enter 'DEL' to remove stocks from the list.
Enter 'HELP' for this help.
""")


def main_intro():
    print("""
/// WELCOME TO THE STOCK SCREENER ///

/// HELP COMMANDS ///
Enter 'INPUT' to add stocks individually.
Enter 'FILE' to import your own csv file. 
Enter 'DEFAULT' to run default stock list.
Enter 'CHOOSE' to see choices of premade stock lists. 
""")

def del_item_intro():
        print("""*** WARNING ***
You are about to remove stocks from list!
""")

def show_list(): #display list of stocks
    print("Here are your stocks: ")
    for item in stock_list:
        print(">>> " + item)


def add_to_list(item): #adds item to list
    stock_list.append(item)
    print("{} has been addded, List has {} stock tickers".format(item, len(stock_list)))


def remove_from_list(item): #removes item from list
    stock_list.remove(item)
    print("{} has been removed, List has {} stock tickers".format(item, len(stock_list)))

main_intro()

while True: #main loop
    new_item = input("PICK OPTION > ")

    if new_item == 'INPUT':
        user_help()

        while True:
            new_item = input("Add stock ticker > ") #ask user to input stock

            if new_item == 'DONE':
                break

            elif new_item == 'HELP':
                user_help()
                continue 

            elif new_item == 'SHOW':
                show_list()
                continue

            elif new_item == 'INPUT':
                print("ERROR: You are already in INPUT ")
                print("Enter 'HELP' for more options or add a stock ticker.")
                continue

            elif new_item == 'DEL': # Removing items from stock list
                del_item_intro()

                while True:
                    new_item = input("Remove stock ticker > ")

                    if new_item == 'DONE':
                       break 

                    elif new_item == 'HELP':
                        user_help()
                        continue 

                    elif new_item == 'SHOW':
                        show_list() 
                        continue

                    remove_from_list(new_item)
                continue # will go back to adding stock ticker

            add_to_list(new_item) #adds stock ticker to list       

        break   
    

    elif new_item == 'FILE':
        print("Select your CSV File")
        break

    elif new_item == 'DEFAULT':
        stock_list=default_list
        break



### NOW THAT WE HAVE GOTTEN THE STOCK_LIST POPULATED WITH STOCK TICKERS
for item in stock_list:
    stock_ticker=item # assign stock ticker for every new item in loop

#checks the key licence for alphavantage
    lines = open('keys').read().splitlines()
    keys=random.choice(lines)

    # acceses the library on alpha vantage
    base_url = 'https://www.alphavantage.co/query?'
    params = {'function': 'OVERVIEW',
            'symbol': stock_ticker,
            'apikey': keys}
    response_data_overview = requests.get(base_url, params=params)

    # assigns the object data_overview_MarketCapitalizaiton the data point from alpha vantage
    data_overview_MarketCapitalization = response_data_overview.json()['MarketCapitalization']


    print("The Market Cap for {} is = {}".format(stock_ticker,data_overview_MarketCapitalization))
