# ONLY ADD STOCK ANALYSIS FORUMLAS HERE
    #This file will have all the stock analysis formulas that people developed. 
    # I will include my own personal one here as a default. 

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

# test_restult = int(sdf.data_overview_MarketCapitalization) + int(sdf.data_overview_RevenueTTM)
# print(("testing if this works =  {}").format(test_restult))

# def default_analysis ():
#     int(1) + int(1)
#     return

# print(default_analysis)

hype_A = 1000
hype_P = 500
hype_r = 7
def hype_market_years(): 
    round(((math.log(hype_A/hype_P)) / (math.log(1+hype_r))),2)
    
    return

result = str(hype_market_years)
print(result)
