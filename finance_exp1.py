import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators

style.use('ggplot')

### ASK FOR STOCK TICKER
stock_ticker=input("Enter a stock ticker symbol: ")
stock=SYMBOL(str(stock_ticker))

### ASK FOR STARTING AND ENDING DATE
default_date_setting = str((input("Do you want to use default date settings? Y / N :  ")))

    # Default date settings
if default_date_setting == 'Y':
    start_year=2020
    start_month=1
    start_day=1
    end_date=dt.datetime.now()

    # Will ask user to enter start / end date. Along with setting the string for end date
else:
    start_year, start_month, start_day = input("Enter Start DATE YYYY-MM-DD.  ").split('-')
    end_year, end_month, end_day = input("Enter End DATE YYYY-MM-DD.  ").split('-')
    end_date=dt.datetime(int(end_year),int(end_month),int(end_day))
   
   # Sets the string for start date
start_date=dt.datetime(int(start_year),int(start_month),int(start_day))

df = web.DataReader(stock, 'alpha_vantage', start_year, start_month, start_day, end_date)
df.reset_index(inplace=True)
df.set_index("Date", inplace=True)
df = df.drop("Symbol", axis=1)

print(df.head())

df.plot()
plt.show()

df['Adj Close'].plot()
plt.show()

df[['High','Low']]
plt.show()

df['100ma'] = df['Adj Close'].rolling(window=100,min_periods=0).mean()
print(df.head())
ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)
ax2 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1,sharex=ax1)
ax1.plot(df.index, df['Adj Close'])
ax1.plot(df.index, df['100ma'])
ax2.bar(df.index, df['Volume'])

plt.show()
