# ENTER OBJECTS TO GET CERTAIN STOCK DATA HERE
    # This file will have all the formulas to find the various stock metrics 
    # like daily price, PS , PE , balance sheet info ect. 
    # Any metric anyone wants they can create a class for it here. 

import pandas as pd
from alpha_vantage.timeseries import TimeSeries
import time
import random


    # This uses the keys in the keys file that will be randomly grabbed 
lines = open('keys').read().splitlines()
keys=random.choice(lines)

stock_ticker = "MSFT"

ts = TimeSeries (key=keys, output_format = "pandas")

data, meta_data =ts.get_daily_adjusted(symbol=stock_ticker, outputsize ='compact')

# adjusted_close = data['5. adjusted close']
# last_price=adjusted_close[0]

print(data)