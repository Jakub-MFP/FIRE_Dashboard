# THIS IS THE MASTER FILE, RUN THIS TO INTERACT WITH THE DASHBOARD

    # CURRENT FILES YOU CAN INTERACT WITH
        # quick_stock_analysis.py for individual stock analysis
        # stock_screener.py for an automated script to filter stocks
        # portfolio_dashboard.py to view the perfomrance of your stocks
            # You need to set up a user_template_settings.py file first before this will work
import pandas as pd
from pandas import DataFrame
import time
import random
import numpy as np
import math
import datetime as dt
import requests
import os
import json
from tabulate import tabulate

menu_items = [
['STOCKS','> Stock Screener for flexible stock analysis'],
['SIMPLEX','> Expected Value Analysis for Single Stock'],
['CALC','> Launch Compound Interest Calculator'],
['EFC','> Launch Effeceint Forntier Calculator'],
['TEST','> Launch Strategy Backtest Calculator'],
['SETTINGS','> Settings for Portfolio SetUp '],
['PORTFOLIO','> View your portfolio or a mockup'],
['SAVE','> Save your results as CSV'],
['HELP','> View all the menu items again'],
['EXIT','> End the program and current instance'],
]


def help_settings():
    df = DataFrame(menu_items,  columns =['COMMANDS > ','DESCRIPTION'])
    print(tabulate(df, showindex=False, headers=df.columns))


print("""
//////////////////////////
///// FIRE DASHBOARD /////
//////////////////////////

.....MAIN MENU OPTIONS.....
""")

help_settings()

while True:
    print("")
    new_item = input("PICK COMMAND >  ").upper()

    if new_item == 'STOCK':
        import stock_screener
    
    elif new_item == 'SIMPLEX':
        print("This option is in development")
        continue

    elif new_item == 'CALC':
        print("This option is in development")
        continue

    elif new_item == 'EFC':
        print("This option is in development")
        continue

    elif new_item == 'TEST':
        print("This option is in development")
        continue

    elif new_item == 'SETTINGS':
        print("This option is in development")
        continue
    elif new_item == 'PORTFOLIO':
        print("This option is in development")
        continue

    elif new_item == 'SAVE':
        print("This option is in development")
        continue

    elif new_item == 'HELP':
        help_settings()
        continue

    elif new_item == 'EXIT':
        break

    continue

print ("""
////////////////////////////
FIRE DASHBOARD IS NOW CLOSED
////////////////////////////
""")
