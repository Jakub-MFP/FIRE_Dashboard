#Description: This program attempts to optimize a users portfolio using Efficient Frontier

import sys

# pip install PyPortfolioOpt
from pypfopt.efficient_frontier import EfficientFrontier
from pypfopt import risk_models
from pypfopt import expected_returns

# Import the python libraries
from pandas_datareader import data as web
import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

# pip install pulp

# Get the stock symbols / tickers for the portfolio
assets =  ["TSLA", "BA", "DIS", "GOOG", "PFE", "LMND", "BYND", "ECL", "SQ", "SMSN.L"]

# Assign weights to the stocks. Weights must = 1 so 0.2 for each
weights = np.array([0.2696, 0.0637, 0.0881, 0.0824, 0.1066, 0.0598, 0.0642, 0.0655, 0.1105, 0.0868])
weights

#Get the stock starting date
stockStartDate = '2013-01-01'

# Get the stocks ending date aka todays date and format it in the form YYYY-MM-DD
today = '2020-08-16'

#Create a dataframe to store the adjusted close price of the stocks
df = pd.DataFrame()

#Store the adjusted close price of stock into the data frame
for stock in assets:
   df[stock] = web.DataReader(stock,data_source='yahoo',start=stockStartDate , end=today)['Adj Close']

print(df)

# Create the title 'Portfolio Adj Close Price History
title = 'Portfolio Adj. Close Price History    '

#Get the stocks
my_stocks = df

#Create and plot the graph
plt.figure(figsize=(12.2,4.5)) #width = 12.2in, height = 4.5

# Loop through each stock and plot the Adj Close for each day
for c in my_stocks.columns.values:
  plt.plot( my_stocks[c],  label=c)#plt.plot( X-Axis , Y-Axis, line_width, alpha_for_blending,  label)
plt.title(title)
plt.xlabel('Date',fontsize=18)
plt.ylabel('Adj. Price USD ($)',fontsize=18)
plt.legend(my_stocks.columns.values, loc='upper left')
plt.show()

#Show the daily simple returns, NOTE: Formula = new_price/old_price - 1
returns = df.pct_change()
print(returns)

# To show the annualized co-variance matrix we must multiply the co-variance matrix by the number of trading days for the current year.
cov_matrix_annual = returns.cov() * 157
print(cov_matrix_annual)

# portfolio variance using the formula : Expected portfolio variance= WT * (Covariance Matrix) * W
port_variance = np.dot(weights.T, np.dot(cov_matrix_annual, weights))
print(port_variance)

# portfolio volatility using the formula : Expected portfolio volatility= SQRT (WT * (Covariance Matrix) * W)
port_volatility = np.sqrt(port_variance)
print(port_volatility)

# calculate the portfolio annual simple return
portfolioSimpleAnnualReturn = np.sum(returns.mean()*weights) * 252
print(portfolioSimpleAnnualReturn)

#expected annual return, volatility or risk, and variance
percent_var = str(round(port_variance, 2) * 100) + '%'
percent_vols = str(round(port_volatility, 2) * 100) + '%'
percent_ret = str(round(portfolioSimpleAnnualReturn, 2)*100)+'%'
print("Expected annual return : "+ percent_ret)
print('Annual volatility/standard deviation/risk : '+percent_vols)
print('Annual variance : '+percent_var)

# Calculate the expected returns and the annualised sample covariance matrix of daily asset returns.
mu = expected_returns.mean_historical_return(df)#returns.mean() * 252
S = risk_models.sample_cov(df) #Get the sample covariance matrix

# Optimize for maximal Sharpe ratio
ef = EfficientFrontier(mu, S)
weights = ef.max_sharpe() #Maximize the Sharpe ratio, and get the raw weights
cleaned_weights = ef.clean_weights() 
print(cleaned_weights) #Note the weights may have some rounding error, meaning they may not add up exactly to 1 but should be close
ef.portfolio_performance(verbose=True)

from pypfopt.discrete_allocation import DiscreteAllocation, get_latest_prices
latest_prices = get_latest_prices(df)
weights = cleaned_weights 
da = DiscreteAllocation(weights, latest_prices, total_portfolio_value=816.73)
allocation, leftover = da.lp_portfolio()
print("Discrete allocation:", allocation)
print("Funds remaining: ${:.2f}".format(leftover))



