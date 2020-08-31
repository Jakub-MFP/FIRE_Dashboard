# ONLY ADD STOCK ANALYSIS FORUMLAS HERE
    #This file will have all the stock analysis formulas that people developed. 
    # I will include my own personal one here as a default. 

import requests
import os
import json
import math
import stock_data_formulas as sdf

test_restult = int(sdf.data_overview_MarketCapitalization) + int(sdf.data_overview_RevenueTTM)
print(("testing if this works =  {}").format(test_restult))