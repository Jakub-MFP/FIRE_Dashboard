# ENTER OBJECTS TO GET CERTAIN STOCK DATA HERE
    # This file will have all the formulas to find the various stock metrics 
    # like daily price, PS , PE , balance sheet info ect. 
    # Any metric anyone wants they can create a class for it here. 

import pandas as pd
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.cryptocurrencies import CryptoCurrencies
from alpha_vantage.techindicators import TechIndicators
from alpha_vantage.sectorperformance import SectorPerformances
from alpha_vantage.alphavantage import AlphaVantage

import time
import random
import numpy as np
import math
import datetime as dt
    # Import stock ticker to be used from quick_stock_analysis.py
from quick_stock_analysis import stock_ticker



### IMPORTS KEY FROM KEYS FILE ###
lines = open('keys').read().splitlines()
keys=random.choice(lines)

ts = TimeSeries (key=keys, output_format = "pandas")
cs = CryptoCurrencies (key=keys, output_format = "pandas")
ti = TechIndicators (key=keys, output_format = "pandas")
sp = SectorPerformances (key=keys, output_format = "pandas")
av = AlphaVantage (key=keys, output_format = "pandas")

demo = "N/A"
### DO NOT EEDIT THIS ###



### CALLING APIs FROM ALPHA VANTAGE TO ORGANIZE INTO INDIVIDUAL DATA POINTS ###
    # https://www.alphavantage.co/documentation/


    ### MISC QUERIES ###
# All active Stocks for last trading day
    # https://www.alphavantage.co/query?function=LISTING_STATUS&apikey=demo
    # Fundamental Data > Listing & Delisting Status
data_daily_lastActiveStocks = []



    ### STOCK TIME SERIES > DAILY ADJUSTED ###
        # Date / Open / High / Low / Close / Adjusted Close / Volume / Dividend / Split
data_daily, meta_data = ts.get_daily_adjusted(symbol=stock_ticker, outputsize ='compact')
        # data_daily['column name'][row number]
data_daily_lastOpenPrice = data_daily['1. open'][0]
data_daily_lastHighPrice = data_daily['2. high'][0]
data_daily_lastLowPrice = data_daily['3. low'][0]
data_daily_lastAdjustedClosingPrice = data_daily['5. adjusted close'][0]
data_daily_lastTradingVolume = data_daily['6. volume'][0]
data_daily_lastDividendAmount = data_daily['7. dividend amount'][0]

# print(data_daily_dividend_amount)
# print(data_daily_last_open_price)
# print(data_daily_last_adjusted_price)



    ### FUNADMENTAL DATA > COMPANY OVERVIEW ###
    # https://www.alphavantage.co/query?function=OVERVIEW&symbol=IBM&apikey=demo
    # DEMO DATA
#data_company_overview, meta_data = av.overview(symbol=stock_ticker, outputsize ='full')
data_overview_Name = "International Business Machines Corporation"
data_overview_AssetType = "Common Stock" 
data_overview_Description = "blah blah" 
data_overview_Exchange = "NYSE"
data_overview_Currency = "USD"
data_overview_Country = "USA"   
data_overview_Sector = "Technology"
data_overview_Industry = "Information Techonology Services"
data_overview_Address = "address"
data_overview_FullTimeEmployees = "352600"
data_overview_FiscalYearEnd = "December"
data_overview_FiscalYearEnd = "2020-06-30"
data_overview_MarketCapitilization = 111384715264
data_overview_EBITDA = 0
data_overview_PERatio = 0
data_overview_PEGRatio = 0
data_overview_BookValue = 0
data_overview_DividendPerShare = 6.52
data_overview_DividendYield = 0.0523
data_overview_EPS = 0
data_overview_RevenuesPerShareTTM = 0
data_overview_ProfitMargin = 0.1043
data_overview_OperatingMarginTTM = 0.1185
data_overview_ReturnOnAssetsTTM = 0
data_overview_ReturnOnEquityTTM = 0
data_overview_RevenueTTM = 75499003904
data_overview_GrossProfitTTM = 36489000000
data_overview_DilutedEPSTTM = 0
data_overview_QuarterlyEarningsGrowthYOY = -0.458
data_overview_QuarterlyRevenueGrowthYOY = -0.054
data_overview_AnalystTargetPrice = 135.19
data_overview_TrailingPE = 14.1327
data_overview_ForwardPE = 11.2867
data_overview_PriceToSalesRatioTTM = 1.4762
data_overview_PriceToBookRatio = 5.4017
data_overview_EVToRevenue = 0
data_overview_EVToEBITD = 0
data_overview_Beta = 1.2071
data_overview_52WeekHigh = 158.75
data_overview_52WeekLow = 90.56
data_overview_50DayMovingAverage = 124.6553
data_overview_200DayMovingAverage = 123.1466
data_overview_SharesOutstanding = 890579008
data_overview_SharesFloat = 889189445
data_overview_SharesShort = 21600483
data_overview_SharesShortPriorMonth = 23242369
data_overview_ShortRatio = 4.51
data_overview_ShortPercentOutstanding = 0.02
data_overview_ShortPercentFloat = 0.0243
data_overview_PercentInsiders = 0.108
data_overview_PercentInstitutions = 58.555
data_overview_ForwardAnnualDividendRate = 6.52
data_overview_ForwardAnnualDividendYield = 0.0523
data_overview_PayoutRatio = 0.7358
data_overview_DividendDate = "2020-09-10"
data_overview_ExDividendDate = "2020-08-07"
data_overview_LastSplitFactor = "2:1"
data_overview_LastSplitDate = "1999-05-27"
data_overview_Alpha = 1.2071



    ### FUNDAMENTAL DATA > INCOME STATEMENT ###
    # https://www.alphavantage.co/query?function=INCOME_STATEMENT&symbol=IBM&apikey=demo
    # We can have data be <annual> or <quarterly> 
        # date is denaoted by "fiscalDateEnding"
    # DEMO DATA
#data_income_statement, meta_data = fd.get_INCOME_STATEMENT(symbol=stock_ticker, outputsize ='compact')
    
    # LAST ANNUAL INCOME STATEMENT RESULTS
data_income_annual_last_fiscalDateEnding = 0
data_income_annual_last_reportedCurrency = 0
data_income_annual_last_totalRevenue = 0
data_income_annual_last_totalOperatingExpense = 0
data_income_annual_last_costOfRevenue = 0
data_income_annual_last_grossProfit = 0
data_income_annual_last_ebit = 0
data_income_annual_last_netIncome = 0
data_income_annual_last_researchAndDevelopment = 0
data_income_annual_last_effectOfAccountingCharges = 0
data_income_annual_last_incomeBeforeTax = 0
data_income_annual_last_minorityInterest = 0
data_income_annual_last_sellingGeneralAdministrative = 0
data_income_annual_last_otherNonOperatingIncome = 0
data_income_annual_last_operatingIncome = 0
data_income_annual_last_otherOperatingExpense = 0
data_income_annual_last_interestExpense = 0
data_income_annual_last_taxProvision = 0
data_income_annual_last_interestIncome = 0
data_income_annual_last_netInterestIncome = 0
data_income_annual_last_extraordinaryItems = 0
data_income_annual_last_nonRecurring = 0
data_income_annual_last_otherItems = 0
data_income_annual_last_incomeTaxExpense = 0
data_income_annual_last_totalOtherIncomeExpense = 0
data_income_annual_last_discontinuedOperations = 0
data_income_annual_last_netIncomeFromContinuingOperations = 0
data_income_annual_last_netIncomeApplicableToCommonShares = 0
data_income_annual_last_preferredStockAndOtherAdjustments = 0

    # LAST QUARTERLY INCOME STATEMENT RESULTS
data_income_quarterly_last_fiscalDateEnding = 0
data_income_quarterly_last_reportedCurrency = 0
data_income_quarterly_last_totalRevenue = 0
data_income_quarterly_last_totalOperatingExpense = 0
data_income_quarterly_last_costOfRevenue = 0
data_income_quarterly_last_grossProfit = 0
data_income_quarterly_last_ebit = 0
data_income_quarterly_last_netIncome = 0
data_income_quarterly_last_researchAndDevelopment = 0
data_income_quarterly_last_effectOfAccountingCharges = 0
data_income_quarterly_last_incomeBeforeTax = 0
data_income_quarterly_last_minorityInterest = 0
data_income_quarterly_last_sellingGeneralAdministrative = 0
data_income_quarterly_last_otherNonOperatingIncome = 0
data_income_quarterly_last_operatingIncome = 0
data_income_quarterly_last_otherOperatingExpense = 0
data_income_quarterly_last_interestExpense = 0
data_income_quarterly_last_taxProvision = 0
data_income_quarterly_last_interestIncome = 0
data_income_quarterly_last_netInterestIncome = 0
data_income_quarterly_last_extraordinaryItems = 0
data_income_quarterly_last_nonRecurring = 0
data_income_quarterly_last_otherItems = 0
data_income_quarterly_last_incomeTaxExpense = 0
data_income_quarterly_last_totalOtherIncomeExpense = 0
data_income_quarterly_last_discontinuedOperations = 0
data_income_quarterly_last_netIncomeFromContinuingOperations = 0
data_income_quarterly_last_netIncomeApplicableToCommonShares = 0
data_income_quarterly_last_preferredStockAndOtherAdjustments = 0



    ### FUNDAMENTAL DATA > BALANCE SHEET ###
    # https://www.alphavantage.co/query?function=BALANCE_SHEET&symbol=IBM&apikey=demo
        # We can have data be <annual> or <quarterly> 
        # date is denaoted by "fiscalDateEnding"
    # DEMO DATA

    # LAST ANNUAL BALANCE SHEET DATA
data_balance_annual_last_fiscalDateEnding = 0
data_balance_annual_last_reportedCurrency = 0
data_balance_annual_last_totalAssets = 0
data_balance_annual_last_intangibleAssets = 0
data_balance_annual_last_earningAssets = 0
data_balance_annual_last_otherCurrentAssets = 0
data_balance_annual_last_totalLiabilities = 0
data_balance_annual_last_totalShareholderEquity = 0
data_balance_annual_last_deferredLongTermLiabilities = 0
data_balance_annual_last_otherCurrentLiabilities = 0
data_balance_annual_last_commonStock = 0
data_balance_annual_last_retainedEarnings = 0
data_balance_annual_last_otherLiabilities = 0
data_balance_annual_last_goodwill = 0
data_balance_annual_last_otherAssets = 0
data_balance_annual_last_cash = 0
data_balance_annual_last_totalCurrentLiabilities = 0
data_balance_annual_last_shortTermDebt = 0
data_balance_annual_last_currentLongTermDebt = 0
data_balance_annual_last_otherShareholderEquity = 0
data_balance_annual_last_propertyPlantEquipment = 0
data_balance_annual_last_totalCurrentAssets = 0
data_balance_annual_last_longTermInvestments = 0
data_balance_annual_last_netTangibleAssets = 0
data_balance_annual_last_shortTermInvestments = 0
data_balance_annual_last_netReceivables = 0
data_balance_annual_last_longTermDebt = 0
data_balance_annual_last_inventory = 0
data_balance_annual_last_accountsPayable = 0
data_balance_annual_last_totalPermanentEquity = 0
data_balance_annual_last_additionalPaidInCapital = 0
data_balance_annual_last_commonStockTotalEquity = 0
data_balance_annual_last_preferredStockTotalEquity = 0
data_balance_annual_last_retainedEarningsTotalEquity = 0
data_balance_annual_last_treasuryStock = 0
data_balance_annual_last_accumulatedAmortization = 0
data_balance_annual_last_otherNonCurrrentAssets = 0
data_balance_annual_last_deferredLongTermAssetCharges = 0
data_balance_annual_last_totalNonCurrentAssets = 0
data_balance_annual_last_capitalLeaseObligations = 0
data_balance_annual_last_totalLongTermDebt = 0
data_balance_annual_last_otherNonCurrentLiabilities = 0
data_balance_annual_last_totalNonCurrentLiabilities = 0
data_balance_annual_last_negativeGoodwill = 0
data_balance_annual_last_warrants = 0
data_balance_annual_last_preferredStockRedeemable = 0
data_balance_annual_last_capitalSurplus = 0
data_balance_annual_last_liabilitiesAndShareholderEquity = 0
data_balance_annual_last_cashAndShortTermInvestments = 0
data_balance_annual_last_accumulatedDepreciation = 0
data_balance_annual_last_commonStockSharesOutstanding = 0

    # LAST QUARTERLY BALANCE SHEET DATA
data_balance_quarterly_last_fiscalDateEnding = 0
data_balance_quarterly_last_reportedCurrency = 0
data_balance_quarterly_last_totalAssets = 0
data_balance_quarterly_last_intangibleAssets = 0
data_balance_quarterly_last_earningAssets = 0
data_balance_quarterly_last_otherCurrentAssets = 0
data_balance_quarterly_last_totalLiabilities = 0
data_balance_quarterly_last_totalShareholderEquity = 0
data_balance_quarterly_last_deferredLongTermLiabilities = 0
data_balance_quarterly_last_otherCurrentLiabilities = 0
data_balance_quarterly_last_commonStock = 0
data_balance_quarterly_last_retainedEarnings = 0
data_balance_quarterly_last_otherLiabilities = 0
data_balance_quarterly_last_goodwill = 0
data_balance_quarterly_last_otherAssets = 0
data_balance_quarterly_last_cash = 0
data_balance_quarterly_last_totalCurrentLiabilities = 0
data_balance_quarterly_last_shortTermDebt = 0
data_balance_quarterly_last_currentLongTermDebt = 0
data_balance_quarterly_last_otherShareholderEquity = 0
data_balance_quarterly_last_propertyPlantEquipment = 0
data_balance_quarterly_last_totalCurrentAssets = 0
data_balance_quarterly_last_longTermInvestments = 0
data_balance_quarterly_last_netTangibleAssets = 0
data_balance_quarterly_last_shortTermInvestments = 0
data_balance_quarterly_last_netReceivables = 0
data_balance_quarterly_last_longTermDebt = 0
data_balance_quarterly_last_inventory = 0
data_balance_quarterly_last_accountsPayable = 0
data_balance_quarterly_last_totalPermanentEquity = 0
data_balance_quarterly_last_additionalPaidInCapital = 0
data_balance_quarterly_last_commonStockTotalEquity = 0
data_balance_quarterly_last_preferredStockTotalEquity = 0
data_balance_quarterly_last_retainedEarningsTotalEquity = 0
data_balance_quarterly_last_treasuryStock = 0
data_balance_quarterly_last_accumulatedAmortization = 0
data_balance_quarterly_last_otherNonCurrrentAssets = 0
data_balance_quarterly_last_deferredLongTermAssetCharges = 0
data_balance_quarterly_last_totalNonCurrentAssets = 0
data_balance_quarterly_last_capitalLeaseObligations = 0
data_balance_quarterly_last_totalLongTermDebt = 0
data_balance_quarterly_last_otherNonCurrentLiabilities = 0
data_balance_quarterly_last_totalNonCurrentLiabilities = 0
data_balance_quarterly_last_negativeGoodwill = 0
data_balance_quarterly_last_warrants = 0
data_balance_quarterly_last_preferredStockRedeemable = 0
data_balance_quarterly_last_capitalSurplus = 0
data_balance_quarterly_last_liabilitiesAndShareholderEquity = 0
data_balance_quarterly_last_cashAndShortTermInvestments = 0
data_balance_quarterly_last_accumulatedDepreciation = 0
data_balance_quarterly_last_commonStockSharesOutstanding = 0

    ### FUNDAMENTAL DATA > CASH FLOW ###
    # https://www.alphavantage.co/query?function=CASH_FLOW&symbol=IBM&apikey=demo
        # We can have data be <annual> or <quarterly> 
        # date is denaoted by "fiscalDateEnding"
    # DEMO DATA

    # LAST ANNUAL CASH FLOW DATA
data_cashflow_annual_last_fiscalDateEnding = 0
data_cashflow_annual_last_reportedCurrency = 0
data_cashflow_annual_last_investments = 0
data_cashflow_annual_last_changeInLiabilities = 0
data_cashflow_annual_last_cashflowFromInvestment = 0
data_cashflow_annual_last_otherCashflowFromInvestment = 0
data_cashflow_annual_last_netBorrowings = 0
data_cashflow_annual_last_cashflowFromFinancing = 0
data_cashflow_annual_last_otherCashflowFromFinancing = 0
data_cashflow_annual_last_changeInOperatingActivities = 0
data_cashflow_annual_last_netIncome = 0
data_cashflow_annual_last_changeInCash = 0
data_cashflow_annual_last_operatingCashflow = 0
data_cashflow_annual_last_otherOperatingCashflow = 0
data_cashflow_annual_last_depreciation = 0
data_cashflow_annual_last_dividendPayout = 0
data_cashflow_annual_last_stockSaleAndPurchase = 0
data_cashflow_annual_last_changeInInventory = 0
data_cashflow_annual_last_changeInAccountReceivables = 0
data_cashflow_annual_last_changeInNetIncome = 0
data_cashflow_annual_last_capitalExpenditures = 0
data_cashflow_annual_last_changeInReceivables = 0
data_cashflow_annual_last_changeInExchangeRate = 0
data_cashflow_annual_last_changeInCashAndCashEquivalents = 0

    # LAST QUARTERLY CASH FLOW DATA
data_cashflow_quarterly_last_fiscalDateEnding = 0
data_cashflow_quarterly_last_reportedCurrency = 0
data_cashflow_quarterly_last_investments = 0
data_cashflow_quarterly_last_changeInLiabilities = 0
data_cashflow_quarterly_last_cashflowFromInvestment = 0
data_cashflow_quarterly_last_otherCashflowFromInvestment = 0
data_cashflow_quarterly_last_netBorrowings = 0
data_cashflow_quarterly_last_cashflowFromFinancing = 0
data_cashflow_quarterly_last_otherCashflowFromFinancing = 0
data_cashflow_quarterly_last_changeInOperatingActivities = 0
data_cashflow_quarterly_last_netIncome = 0
data_cashflow_quarterly_last_changeInCash = 0
data_cashflow_quarterly_last_operatingCashflow = 0
data_cashflow_quarterly_last_otherOperatingCashflow = 0
data_cashflow_quarterly_last_depreciation = 0
data_cashflow_quarterly_last_dividendPayout = 0
data_cashflow_quarterly_last_stockSaleAndPurchase = 0
data_cashflow_quarterly_last_changeInInventory = 0
data_cashflow_quarterly_last_changeInAccountReceivables = 0
data_cashflow_quarterly_last_changeInNetIncome = 0
data_cashflow_quarterly_last_capitalExpenditures = 0
data_cashflow_quarterly_last_changeInReceivables = 0
data_cashflow_quarterly_last_changeInExchangeRate = 0
data_cashflow_quarterly_last_changeInCashAndCashEquivalents = 0







