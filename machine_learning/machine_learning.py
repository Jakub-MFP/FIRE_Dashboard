import bs4 as bs
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
import os
import pandas_datareader.data as web
import pickle
import requests
from datapackage import Package
from collections import Counter
from sklearn import svm, cross_validation, neighbors
from sklearn.ensemble import VotingClassifier, RandomForestClassifier
from statistics import mean
import pandas as pd
from alpha_vantage.techindicators import TechIndicators

ti = TechIndicators(key=api_key, output_format='pandas')

style.use('ggplot')

package = Package('https://datahub.io/core/s-and-p-500-companies/datapackage.json')

# print list of all resources:
print(package.resource_names)

# print processed tabular data (if exists any)
for resource in package.resources:
    resource.tabular # true
resource.read(keyed=True)

print(resource['symbol'].unique())

    # tickers = []
    # for row in table.findAll('tr')[1:]:
    #     ticker = row.findAll('td')[0].text
    #     tickers.append(ticker)

    # with open("sp500tickers.pickle","wb") as f:
    #     pickle.dump(tickers,f)

    # return tickers


# save_sp500_tickers()
# def get_data_from_alpha_vantage(reload_sp500=False):
#     if reload_sp500:
#         tickers = save_sp500_tickers()
#     else:
#         with open("sp500tickers.pickle", "rb") as f:
#             tickers = pickle.load(f)
#     if not os.path.exists('stock_dfs'):
#         os.makedirs('stock_dfs')


#     start = dt.datetime(2010, 1, 1)
#     end = dt.datetime.now()
#     for ticker in tickers:
#         # just in case your connection breaks, we'd like to save our progress!
#         if not os.path.exists('stock_dfs/{}.csv'.format(ticker)):
#             df = web.DataReader(ticker, 'morningstar', start, end)
#             df.reset_index(inplace=True)
#             df.set_index("Date", inplace=True)
#             df = df.drop("Symbol", axis=1)
#             df.to_csv('stock_dfs/{}.csv'.format(ticker))
#         else:
#             print('Already have {}'.format(ticker))


# # def compile_data():
# #     with open("sp500tickers.pickle", "rb") as f:
# #         tickers = pickle.load(f)

# #     main_df = pd.DataFrame()

#     for count, ticker in enumerate(tickers):
#         df = pd.read_csv('stock_dfs/{}.csv'.format(ticker))
#         df.set_index('Date', inplace=True)

#         df.rename(columns={'Adj Close': ticker}, inplace=True)
#         df.drop(['Open', 'High', 'Low', 'Close', 'Volume'], 1, inplace=True)

#         if main_df.empty:
#             main_df = df
#         else:
#             main_df = main_df.join(df, how='outer')

#         if count % 10 == 0:
#             print(count)
#     print(main_df.head())
#     main_df.to_csv('sp500_joined_closes.csv')

# def visualize_data():
#     df = pd.read_csv('sp500_joined_closes.csv')
#     df_corr = df.corr()
#     print(df_corr.head())
#     df_corr.to_csv('sp500corr.csv')
#     data1 = df_corr.values
#     fig1 = plt.figure()
#     ax1 = fig1.add_subplot(111)

#     heatmap1 = ax1.pcolor(data1, cmap=plt.cm.RdYlGn)
#     fig1.colorbar(heatmap1)

#     ax1.set_xticks(np.arange(data1.shape[1]) + 0.5, minor=False)
#     ax1.set_yticks(np.arange(data1.shape[0]) + 0.5, minor=False)
#     ax1.invert_yaxis()
#     ax1.xaxis.tick_top()
#     column_labels = df_corr.columns
#     row_labels = df_corr.index
#     ax1.set_xticklabels(column_labels)
#     ax1.set_yticklabels(row_labels)
#     plt.xticks(rotation=90)
#     heatmap1.set_clim(-1, 1)
#     plt.tight_layout()
#     plt.show()

# def process_data_for_labels(ticker):
#     hm_days = 7
#     df = pd.read_csv('sp500_joined_closes.csv', index_col=0)
#     tickers = df.columns.values.tolist()
#     df.fillna(0, inplace=True)

#     for i in range(1,hm_days+1):
#         df['{}_{}d'.format(ticker,i)] = (df[ticker].shift(-i) - df[ticker]) / df[ticker]

#     df.fillna(0, inplace=True)
#     return tickers, df

# def buy_sell_hold(*args):
#     cols = [c for c in args]
#     requirement = 0.02
#     for col in cols:
#         if col > requirement:
#             return 1
#         if col < -requirement:
#             return -1
#     return 0

# def extract_featuresets(ticker):
#     tickers, df = process_data_for_labels(ticker)

#     df['{}_target'.format(ticker)] = list(map( buy_sell_hold,
#                                                df['{}_1d'.format(ticker)],
#                                                df['{}_2d'.format(ticker)],
#                                                df['{}_3d'.format(ticker)],
#                                                df['{}_4d'.format(ticker)],
#                                                df['{}_5d'.format(ticker)],
#                                                df['{}_6d'.format(ticker)],
#                                                df['{}_7d'.format(ticker)] ))
#     vals = df['{}_target'.format(ticker)].values.tolist()
#     str_vals = [str(i) for i in vals]
#     print('Data spread:',Counter(str_vals))

#     ###Clean up our data
#     df.fillna(0, inplace=True)
#     df = df.replace([np.inf, -np.inf], np.nan)
#     df.dropna(inplace=True)

#     ###convert stock prices to % changes
#     df_vals = df[[ticker for ticker in tickers]].pct_change()
#     df_vals = df_vals.replace([np.inf, -np.inf], 0)
#     df_vals.fillna(0, inplace=True)
#     X = df_vals.values
#     y = df['{}_target'.format(ticker)].values
#     return X,y,df

# def do_ml(ticker):
#     X, y, df = extract_featuresets(ticker)

#     X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.25)

#     clf = VotingClassifier([('lsvc', svm.LinearSVC()),
#                             ('knn', neighbors.KNeighborsClassifier()),
#                             ('rfor', RandomForestClassifier())])

#     clf.fit(X_train, y_train)
#     confidence = clf.score(X_test, y_test)
#     print('accuracy:', confidence)
#     predictions = clf.predict(X_test)
#     print('predicted class counts:', Counter(predictions))
#     print()
#     print()
#     return confidence


# # examples of running:
# do_ml('XOM')
# do_ml('AAPL')
# do_ml('ABT')

# with open("sp500tickers.pickle","rb") as f:
#     tickers = pickle.load(f)

# accuracies = []
# for count,ticker in enumerate(tickers):

#     if count%10==0:
#         print(count)

#     accuracy = do_ml(ticker)
#     accuracies.append(accuracy)
#     print("{} accuracy: {}. Average accuracy:{}".format(ticker,accuracy,mean(accuracies)))