# ENTER OBJECTS TO GET CERTAIN STOCK DATA HERE
    # This file will have all the formulas to find the various stock data points 
    # like daily price, PS , PE , balance sheet info ect. 
    # Any metric anyone wants they can create it here

from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.cryptocurrencies import CryptoCurrencies
from alpha_vantage.techindicators import TechIndicators
from alpha_vantage.sectorperformance import SectorPerformances
from alpha_vantage.alphavantage import AlphaVantage
import pandas as pd
import time
import random
import numpy as np
import math
import datetime as dt
import requests
import os
import json
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
### ^^^ DON'T EDIT ^^^ ###

### CALLING APIs FROM ALPHA VANTAGE TO ORGANIZE INTO INDIVIDUAL DATA POINTS ###
    # https://www.alphavantage.co/documentation/


    ### MISC QUERIES ###
# All active Stocks for last trading day
    # https://www.alphavantage.co/query?function=LISTING_STATUS&apikey=demo
    # Fundamental Data > Listing & Delisting Status
data_daily_lastActiveStocks = "need to make forumla"
data_overview_Alpha = "need to make forumla"



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



    ### FUNADMENTAL DATA > COMPANY OVERVIEW ###
    # https://www.alphavantage.co/query?function=OVERVIEW&symbol=IBM&apikey=demo

base_url = 'https://www.alphavantage.co/query?'
params = {'function': 'OVERVIEW',
		 'symbol': stock_ticker,
		 'apikey': keys}
response_data_overview = requests.get(base_url, params=params)

data_overview_Name = response_data_overview.json()['Name']
data_overview_AssetType = response_data_overview.json()['AssetType']
data_overview_Description = response_data_overview.json()['Description']
data_overview_Exchange = response_data_overview.json()['Exchange']
data_overview_Currency = response_data_overview.json()['Currency']
data_overview_Country = response_data_overview.json()['Country']
data_overview_Sector = response_data_overview.json()['Sector']
data_overview_Industry = response_data_overview.json()['Industry']
data_overview_Address = response_data_overview.json()['Address']
data_overview_FullTimeEmployees = response_data_overview.json()['FullTimeEmployees']
data_overview_FiscalYearEnd = response_data_overview.json()['FiscalYearEnd']
data_overview_FiscalYearEnd = response_data_overview.json()['FiscalYearEnd']
data_overview_MarketCapitalization = response_data_overview.json()['MarketCapitalization']
data_overview_EBITDA = response_data_overview.json()['EBITDA']
data_overview_PERatio = response_data_overview.json()['PERatio']
data_overview_PEGRatio = response_data_overview.json()['PEGRatio']
data_overview_BookValue = response_data_overview.json()['BookValue']
data_overview_DividendPerShare = response_data_overview.json()['DividendPerShare']
data_overview_DividendYield = response_data_overview.json()['DividendYield']
data_overview_EPS = response_data_overview.json()['EPS']
data_overview_RevenuePerShareTTM = response_data_overview.json()['RevenuePerShareTTM']
data_overview_ProfitMargin = response_data_overview.json()['ProfitMargin']
data_overview_OperatingMarginTTM = response_data_overview.json()['OperatingMarginTTM']
data_overview_ReturnOnAssetsTTM = response_data_overview.json()['ReturnOnAssetsTTM']
data_overview_ReturnOnEquityTTM = response_data_overview.json()['ReturnOnEquityTTM']
data_overview_RevenueTTM = response_data_overview.json()['RevenueTTM']
data_overview_GrossProfitTTM = response_data_overview.json()['GrossProfitTTM']
data_overview_DilutedEPSTTM = response_data_overview.json()['DilutedEPSTTM']
data_overview_QuarterlyEarningsGrowthYOY = response_data_overview.json()['QuarterlyEarningsGrowthYOY']
data_overview_QuarterlyRevenueGrowthYOY = response_data_overview.json()['QuarterlyRevenueGrowthYOY']
data_overview_AnalystTargetPrice = response_data_overview.json()['AnalystTargetPrice']
data_overview_TrailingPE = response_data_overview.json()['TrailingPE']
data_overview_ForwardPE = response_data_overview.json()['ForwardPE']
data_overview_PriceToSalesRatioTTM = response_data_overview.json()['PriceToSalesRatioTTM']
data_overview_PriceToBookRatio = response_data_overview.json()['PriceToBookRatio']
data_overview_EVToRevenue = response_data_overview.json()['EVToRevenue']
data_overview_EVToEBITDA = response_data_overview.json()['EVToEBITDA']
data_overview_Beta = response_data_overview.json()['Beta']
data_overview_52WeekHigh = response_data_overview.json()['52WeekHigh']
data_overview_52WeekLow = response_data_overview.json()['52WeekLow']
data_overview_50DayMovingAverage = response_data_overview.json()['50DayMovingAverage']
data_overview_200DayMovingAverage = response_data_overview.json()['200DayMovingAverage']
data_overview_SharesOutstanding = response_data_overview.json()['SharesOutstanding']
data_overview_SharesFloat = response_data_overview.json()['SharesFloat']
data_overview_SharesShort = response_data_overview.json()['SharesShort']
data_overview_SharesShortPriorMonth = response_data_overview.json()['SharesShortPriorMonth']
data_overview_ShortRatio = response_data_overview.json()['ShortRatio']
data_overview_ShortPercentOutstanding = response_data_overview.json()['ShortPercentOutstanding']
data_overview_ShortPercentFloat = response_data_overview.json()['ShortPercentFloat']
data_overview_PercentInsiders = response_data_overview.json()['PercentInsiders']
data_overview_PercentInstitutions = response_data_overview.json()['PercentInstitutions']
data_overview_ForwardAnnualDividendRate = response_data_overview.json()['ForwardAnnualDividendRate']
data_overview_ForwardAnnualDividendYield = response_data_overview.json()['ForwardAnnualDividendYield']
data_overview_PayoutRatio = response_data_overview.json()['PayoutRatio']
data_overview_DividendDate = response_data_overview.json()['DividendDate']
data_overview_ExDividendDate = response_data_overview.json()['ExDividendDate']
data_overview_LastSplitFactor = response_data_overview.json()['LastSplitFactor']
data_overview_LastSplitDate = response_data_overview.json()['LastSplitDate']



    ### FUNDAMENTAL DATA > INCOME STATEMENT ###
    # https://www.alphavantage.co/query?function=INCOME_STATEMENT&symbol=IBM&apikey=demo
    # We can have data be <annual> or <quarterly> 
        # date is denaoted by "fiscalDateEnding"

base_url = 'https://www.alphavantage.co/query?'
params = {'function': 'INCOME_STATEMENT',
		 'symbol': stock_ticker,
		 'apikey': keys}
response_data_income = requests.get(base_url, params=params)



    # LAST ANNUAL INCOME STATEMENT RESULTS
data_income_annual_last_fiscalDateEnding = response_data_income.json()['annualReports'][0]['fiscalDateEnding']
data_income_annual_last_reportedCurrency = response_data_income.json()['annualReports'][0]['reportedCurrency']
data_income_annual_last_totalRevenue = response_data_income.json()['annualReports'][0]['totalRevenue']
data_income_annual_last_totalOperatingExpense = response_data_income.json()['annualReports'][0]['totalOperatingExpense']
data_income_annual_last_costOfRevenue = response_data_income.json()['annualReports'][0]['costOfRevenue']
data_income_annual_last_grossProfit = response_data_income.json()['annualReports'][0]['grossProfit']
data_income_annual_last_ebit = response_data_income.json()['annualReports'][0]['ebit']
data_income_annual_last_netIncome = response_data_income.json()['annualReports'][0]['netIncome']
data_income_annual_last_researchAndDevelopment = response_data_income.json()['annualReports'][0]['researchAndDevelopment']
data_income_annual_last_effectOfAccountingCharges = response_data_income.json()['annualReports'][0]['effectOfAccountingCharges']
data_income_annual_last_incomeBeforeTax = response_data_income.json()['annualReports'][0]['incomeBeforeTax']
data_income_annual_last_minorityInterest = response_data_income.json()['annualReports'][0]['minorityInterest']
data_income_annual_last_sellingGeneralAdministrative = response_data_income.json()['annualReports'][0]['sellingGeneralAdministrative']
data_income_annual_last_otherNonOperatingIncome = response_data_income.json()['annualReports'][0]['otherNonOperatingIncome']
data_income_annual_last_operatingIncome = response_data_income.json()['annualReports'][0]['operatingIncome']
data_income_annual_last_otherOperatingExpense = response_data_income.json()['annualReports'][0]['otherOperatingExpense']
data_income_annual_last_interestExpense = response_data_income.json()['annualReports'][0]['interestExpense']
data_income_annual_last_taxProvision = response_data_income.json()['annualReports'][0]['taxProvision']
data_income_annual_last_interestIncome = response_data_income.json()['annualReports'][0]['interestIncome']
data_income_annual_last_netInterestIncome = response_data_income.json()['annualReports'][0]['netInterestIncome']
data_income_annual_last_extraordinaryItems = response_data_income.json()['annualReports'][0]['extraordinaryItems']
data_income_annual_last_nonRecurring = response_data_income.json()['annualReports'][0]['nonRecurring']
data_income_annual_last_otherItems = response_data_income.json()['annualReports'][0]['otherItems']
data_income_annual_last_incomeTaxExpense = response_data_income.json()['annualReports'][0]['incomeTaxExpense']
data_income_annual_last_totalOtherIncomeExpense = response_data_income.json()['annualReports'][0]['totalOtherIncomeExpense']
data_income_annual_last_discontinuedOperations = response_data_income.json()['annualReports'][0]['discontinuedOperations']
data_income_annual_last_netIncomeFromContinuingOperations = response_data_income.json()['annualReports'][0]['netIncomeFromContinuingOperations']
data_income_annual_last_netIncomeApplicableToCommonShares = response_data_income.json()['annualReports'][0]['netIncomeApplicableToCommonShares']
data_income_annual_last_preferredStockAndOtherAdjustments = response_data_income.json()['annualReports'][0]['preferredStockAndOtherAdjustments']



    # LAST QUARTERLY INCOME STATEMENT RESULTS
data_income_quarterly_last_fiscalDateEnding = response_data_income.json()['quarterlyReports'][0]['fiscalDateEnding']
data_income_quarterly_last_reportedCurrency = response_data_income.json()['quarterlyReports'][0]['reportedCurrency']
data_income_quarterly_last_totalRevenue = response_data_income.json()['quarterlyReports'][0]['totalRevenue']
data_income_quarterly_last_totalOperatingExpense = response_data_income.json()['quarterlyReports'][0]['totalOperatingExpense']
data_income_quarterly_last_costOfRevenue = response_data_income.json()['quarterlyReports'][0]['costOfRevenue']
data_income_quarterly_last_grossProfit = response_data_income.json()['quarterlyReports'][0]['grossProfit']
data_income_quarterly_last_ebit = response_data_income.json()['quarterlyReports'][0]['ebit']
data_income_quarterly_last_netIncome = response_data_income.json()['quarterlyReports'][0]['netIncome']
data_income_quarterly_last_researchAndDevelopment = response_data_income.json()['quarterlyReports'][0]['researchAndDevelopment']
data_income_quarterly_last_effectOfAccountingCharges = response_data_income.json()['quarterlyReports'][0]['effectOfAccountingCharges']
data_income_quarterly_last_incomeBeforeTax = response_data_income.json()['quarterlyReports'][0]['incomeBeforeTax']
data_income_quarterly_last_minorityInterest = response_data_income.json()['quarterlyReports'][0]['minorityInterest']
data_income_quarterly_last_sellingGeneralAdministrative = response_data_income.json()['quarterlyReports'][0]['sellingGeneralAdministrative']
data_income_quarterly_last_otherNonOperatingIncome = response_data_income.json()['quarterlyReports'][0]['otherNonOperatingIncome']
data_income_quarterly_last_operatingIncome = response_data_income.json()['quarterlyReports'][0]['operatingIncome']
data_income_quarterly_last_otherOperatingExpense = response_data_income.json()['quarterlyReports'][0]['otherOperatingExpense']
data_income_quarterly_last_interestExpense = response_data_income.json()['quarterlyReports'][0]['interestExpense']
data_income_quarterly_last_taxProvision = response_data_income.json()['quarterlyReports'][0]['taxProvision']
data_income_quarterly_last_interestIncome = response_data_income.json()['quarterlyReports'][0]['interestIncome']
data_income_quarterly_last_netInterestIncome = response_data_income.json()['quarterlyReports'][0]['netInterestIncome']
data_income_quarterly_last_extraordinaryItems = response_data_income.json()['quarterlyReports'][0]['extraordinaryItems']
data_income_quarterly_last_nonRecurring = response_data_income.json()['quarterlyReports'][0]['nonRecurring']
data_income_quarterly_last_otherItems = response_data_income.json()['quarterlyReports'][0]['otherItems']
data_income_quarterly_last_incomeTaxExpense = response_data_income.json()['quarterlyReports'][0]['incomeTaxExpense']
data_income_quarterly_last_totalOtherIncomeExpense = response_data_income.json()['quarterlyReports'][0]['totalOtherIncomeExpense']
data_income_quarterly_last_discontinuedOperations = response_data_income.json()['quarterlyReports'][0]['discontinuedOperations']
data_income_quarterly_last_netIncomeFromContinuingOperations = response_data_income.json()['quarterlyReports'][0]['netIncomeFromContinuingOperations']
data_income_quarterly_last_netIncomeApplicableToCommonShares = response_data_income.json()['quarterlyReports'][0]['netIncomeApplicableToCommonShares']
data_income_quarterly_last_preferredStockAndOtherAdjustments = response_data_income.json()['quarterlyReports'][0]['preferredStockAndOtherAdjustments']



    ### FUNDAMENTAL DATA > BALANCE SHEET ###
    # https://www.alphavantage.co/query?function=BALANCE_SHEET&symbol=IBM&apikey=demo
        # We can have data be <annual> or <quarterly> 
        # date is denaoted by "fiscalDateEnding"

base_url = 'https://www.alphavantage.co/query?'
params = {'function': 'BALANCE_SHEET',
		 'symbol': stock_ticker,
		 'apikey': keys}
response_data_balance = requests.get(base_url, params=params)



    # LAST ANNUAL BALANCE SHEET DATA
data_balance_annual_last_fiscalDateEnding = response_data_balance.json()['annualReports'][0]['fiscalDateEnding']
data_balance_annual_last_reportedCurrency = response_data_balance.json()['annualReports'][0]['reportedCurrency']
data_balance_annual_last_totalAssets = response_data_balance.json()['annualReports'][0]['totalAssets']
data_balance_annual_last_intangibleAssets = response_data_balance.json()['annualReports'][0]['intangibleAssets']
data_balance_annual_last_earningAssets = response_data_balance.json()['annualReports'][0]['earningAssets']
data_balance_annual_last_otherCurrentAssets = response_data_balance.json()['annualReports'][0]['otherCurrentAssets']
data_balance_annual_last_totalLiabilities = response_data_balance.json()['annualReports'][0]['totalLiabilities']
data_balance_annual_last_totalShareholderEquity = response_data_balance.json()['annualReports'][0]['totalShareholderEquity']
data_balance_annual_last_deferredLongTermLiabilities = response_data_balance.json()['annualReports'][0]['deferredLongTermLiabilities']
data_balance_annual_last_otherCurrentLiabilities = response_data_balance.json()['annualReports'][0]['otherCurrentLiabilities']
data_balance_annual_last_commonStock = response_data_balance.json()['annualReports'][0]['commonStock']
data_balance_annual_last_retainedEarnings = response_data_balance.json()['annualReports'][0]['retainedEarnings']
data_balance_annual_last_otherLiabilities = response_data_balance.json()['annualReports'][0]['otherLiabilities']
data_balance_annual_last_goodwill = response_data_balance.json()['annualReports'][0]['goodwill']
data_balance_annual_last_otherAssets = response_data_balance.json()['annualReports'][0]['otherAssets']
data_balance_annual_last_cash = response_data_balance.json()['annualReports'][0]['cash']
data_balance_annual_last_totalCurrentLiabilities = response_data_balance.json()['annualReports'][0]['totalCurrentLiabilities']
data_balance_annual_last_shortTermDebt = response_data_balance.json()['annualReports'][0]['shortTermDebt']
data_balance_annual_last_currentLongTermDebt = response_data_balance.json()['annualReports'][0]['currentLongTermDebt']
data_balance_annual_last_otherShareholderEquity = response_data_balance.json()['annualReports'][0]['otherShareholderEquity']
data_balance_annual_last_propertyPlantEquipment = response_data_balance.json()['annualReports'][0]['propertyPlantEquipment']
data_balance_annual_last_totalCurrentAssets = response_data_balance.json()['annualReports'][0]['totalCurrentAssets']
data_balance_annual_last_longTermInvestments = response_data_balance.json()['annualReports'][0]['longTermInvestments']
data_balance_annual_last_netTangibleAssets = response_data_balance.json()['annualReports'][0]['netTangibleAssets']
data_balance_annual_last_shortTermInvestments = response_data_balance.json()['annualReports'][0]['shortTermInvestments']
data_balance_annual_last_netReceivables = response_data_balance.json()['annualReports'][0]['netReceivables']
data_balance_annual_last_longTermDebt = response_data_balance.json()['annualReports'][0]['longTermDebt']
data_balance_annual_last_inventory = response_data_balance.json()['annualReports'][0]['inventory']
data_balance_annual_last_accountsPayable = response_data_balance.json()['annualReports'][0]['accountsPayable']
data_balance_annual_last_totalPermanentEquity = response_data_balance.json()['annualReports'][0]['totalPermanentEquity']
data_balance_annual_last_additionalPaidInCapital = response_data_balance.json()['annualReports'][0]['additionalPaidInCapital']
data_balance_annual_last_commonStockTotalEquity = response_data_balance.json()['annualReports'][0]['commonStockTotalEquity']
data_balance_annual_last_preferredStockTotalEquity = response_data_balance.json()['annualReports'][0]['preferredStockTotalEquity']
data_balance_annual_last_retainedEarningsTotalEquity = response_data_balance.json()['annualReports'][0]['retainedEarningsTotalEquity']
data_balance_annual_last_treasuryStock = response_data_balance.json()['annualReports'][0]['treasuryStock']
data_balance_annual_last_accumulatedAmortization = response_data_balance.json()['annualReports'][0]['accumulatedAmortization']
data_balance_annual_last_otherNonCurrrentAssets = response_data_balance.json()['annualReports'][0]['otherNonCurrrentAssets']
data_balance_annual_last_deferredLongTermAssetCharges = response_data_balance.json()['annualReports'][0]['deferredLongTermAssetCharges']
data_balance_annual_last_totalNonCurrentAssets = response_data_balance.json()['annualReports'][0]['totalNonCurrentAssets']
data_balance_annual_last_capitalLeaseObligations = response_data_balance.json()['annualReports'][0]['capitalLeaseObligations']
data_balance_annual_last_totalLongTermDebt = response_data_balance.json()['annualReports'][0]['totalLongTermDebt']
data_balance_annual_last_otherNonCurrentLiabilities = response_data_balance.json()['annualReports'][0]['otherNonCurrentLiabilities']
data_balance_annual_last_totalNonCurrentLiabilities = response_data_balance.json()['annualReports'][0]['totalNonCurrentLiabilities']
data_balance_annual_last_negativeGoodwill = response_data_balance.json()['annualReports'][0]['negativeGoodwill']
data_balance_annual_last_warrants = response_data_balance.json()['annualReports'][0]['warrants']
data_balance_annual_last_preferredStockRedeemable = response_data_balance.json()['annualReports'][0]['preferredStockRedeemable']
data_balance_annual_last_capitalSurplus = response_data_balance.json()['annualReports'][0]['capitalSurplus']
data_balance_annual_last_liabilitiesAndShareholderEquity = response_data_balance.json()['annualReports'][0]['liabilitiesAndShareholderEquity']
data_balance_annual_last_cashAndShortTermInvestments = response_data_balance.json()['annualReports'][0]['cashAndShortTermInvestments']
data_balance_annual_last_accumulatedDepreciation = response_data_balance.json()['annualReports'][0]['accumulatedDepreciation']
data_balance_annual_last_commonStockSharesOutstanding = response_data_balance.json()['annualReports'][0]['commonStockSharesOutstanding']



    # LAST QUARTERLY BALANCE SHEET DATA
data_balance_quarterly_last_fiscalDateEnding = response_data_balance.json()['quarterlyReports'][0]['fiscalDateEnding']
data_balance_quarterly_last_reportedCurrency = response_data_balance.json()['quarterlyReports'][0]['reportedCurrency']
data_balance_quarterly_last_totalAssets = response_data_balance.json()['quarterlyReports'][0]['totalAssets']
data_balance_quarterly_last_intangibleAssets = response_data_balance.json()['quarterlyReports'][0]['intangibleAssets']
data_balance_quarterly_last_earningAssets = response_data_balance.json()['quarterlyReports'][0]['earningAssets']
data_balance_quarterly_last_otherCurrentAssets = response_data_balance.json()['quarterlyReports'][0]['otherCurrentAssets']
data_balance_quarterly_last_totalLiabilities = response_data_balance.json()['quarterlyReports'][0]['totalLiabilities']
data_balance_quarterly_last_totalShareholderEquity = response_data_balance.json()['quarterlyReports'][0]['totalShareholderEquity']
data_balance_quarterly_last_deferredLongTermLiabilities = response_data_balance.json()['quarterlyReports'][0]['deferredLongTermLiabilities']
data_balance_quarterly_last_otherCurrentLiabilities = response_data_balance.json()['quarterlyReports'][0]['otherCurrentLiabilities']
data_balance_quarterly_last_commonStock = response_data_balance.json()['quarterlyReports'][0]['commonStock']
data_balance_quarterly_last_retainedEarnings = response_data_balance.json()['quarterlyReports'][0]['retainedEarnings']
data_balance_quarterly_last_otherLiabilities = response_data_balance.json()['quarterlyReports'][0]['otherLiabilities']
data_balance_quarterly_last_goodwill = response_data_balance.json()['quarterlyReports'][0]['goodwill']
data_balance_quarterly_last_otherAssets = response_data_balance.json()['quarterlyReports'][0]['otherAssets']
data_balance_quarterly_last_cash = response_data_balance.json()['quarterlyReports'][0]['cash']
data_balance_quarterly_last_totalCurrentLiabilities = response_data_balance.json()['quarterlyReports'][0]['totalCurrentLiabilities']
data_balance_quarterly_last_shortTermDebt = response_data_balance.json()['quarterlyReports'][0]['shortTermDebt']
data_balance_quarterly_last_currentLongTermDebt = response_data_balance.json()['quarterlyReports'][0]['currentLongTermDebt']
data_balance_quarterly_last_otherShareholderEquity = response_data_balance.json()['quarterlyReports'][0]['otherShareholderEquity']
data_balance_quarterly_last_propertyPlantEquipment = response_data_balance.json()['quarterlyReports'][0]['propertyPlantEquipment']
data_balance_quarterly_last_totalCurrentAssets = response_data_balance.json()['quarterlyReports'][0]['totalCurrentAssets']
data_balance_quarterly_last_longTermInvestments = response_data_balance.json()['quarterlyReports'][0]['longTermInvestments']
data_balance_quarterly_last_netTangibleAssets = response_data_balance.json()['quarterlyReports'][0]['netTangibleAssets']
data_balance_quarterly_last_shortTermInvestments = response_data_balance.json()['quarterlyReports'][0]['shortTermInvestments']
data_balance_quarterly_last_netReceivables = response_data_balance.json()['quarterlyReports'][0]['netReceivables']
data_balance_quarterly_last_longTermDebt = response_data_balance.json()['quarterlyReports'][0]['longTermDebt']
data_balance_quarterly_last_inventory = response_data_balance.json()['quarterlyReports'][0]['inventory']
data_balance_quarterly_last_accountsPayable = response_data_balance.json()['quarterlyReports'][0]['accountsPayable']
data_balance_quarterly_last_totalPermanentEquity = response_data_balance.json()['quarterlyReports'][0]['totalPermanentEquity']
data_balance_quarterly_last_additionalPaidInCapital = response_data_balance.json()['quarterlyReports'][0]['additionalPaidInCapital']
data_balance_quarterly_last_commonStockTotalEquity = response_data_balance.json()['quarterlyReports'][0]['commonStockTotalEquity']
data_balance_quarterly_last_preferredStockTotalEquity = response_data_balance.json()['quarterlyReports'][0]['preferredStockTotalEquity']
data_balance_quarterly_last_retainedEarningsTotalEquity = response_data_balance.json()['quarterlyReports'][0]['retainedEarningsTotalEquity']
data_balance_quarterly_last_treasuryStock = response_data_balance.json()['quarterlyReports'][0]['treasuryStock']
data_balance_quarterly_last_accumulatedAmortization = response_data_balance.json()['quarterlyReports'][0]['accumulatedAmortization']
data_balance_quarterly_last_otherNonCurrrentAssets = response_data_balance.json()['quarterlyReports'][0]['otherNonCurrrentAssets']
data_balance_quarterly_last_deferredLongTermAssetCharges = response_data_balance.json()['quarterlyReports'][0]['deferredLongTermAssetCharges']
data_balance_quarterly_last_totalNonCurrentAssets = response_data_balance.json()['quarterlyReports'][0]['totalNonCurrentAssets']
data_balance_quarterly_last_capitalLeaseObligations = response_data_balance.json()['quarterlyReports'][0]['capitalLeaseObligations']
data_balance_quarterly_last_totalLongTermDebt = response_data_balance.json()['quarterlyReports'][0]['totalLongTermDebt']
data_balance_quarterly_last_otherNonCurrentLiabilities = response_data_balance.json()['quarterlyReports'][0]['otherNonCurrentLiabilities']
data_balance_quarterly_last_totalNonCurrentLiabilities = response_data_balance.json()['quarterlyReports'][0]['totalNonCurrentLiabilities']
data_balance_quarterly_last_negativeGoodwill = response_data_balance.json()['quarterlyReports'][0]['negativeGoodwill']
data_balance_quarterly_last_warrants = response_data_balance.json()['quarterlyReports'][0]['warrants']
data_balance_quarterly_last_preferredStockRedeemable = response_data_balance.json()['quarterlyReports'][0]['preferredStockRedeemable']
data_balance_quarterly_last_capitalSurplus = response_data_balance.json()['quarterlyReports'][0]['capitalSurplus']
data_balance_quarterly_last_liabilitiesAndShareholderEquity = response_data_balance.json()['quarterlyReports'][0]['liabilitiesAndShareholderEquity']
data_balance_quarterly_last_cashAndShortTermInvestments = response_data_balance.json()['quarterlyReports'][0]['cashAndShortTermInvestments']
data_balance_quarterly_last_accumulatedDepreciation = response_data_balance.json()['quarterlyReports'][0]['accumulatedDepreciation']
data_balance_quarterly_last_commonStockSharesOutstanding = response_data_balance.json()['quarterlyReports'][0]['commonStockSharesOutstanding']



    ### FUNDAMENTAL DATA > CASH FLOW ###
    # https://www.alphavantage.co/query?function=CASH_FLOW&symbol=IBM&apikey=demo
        # We can have data be <annual> or <quarterly> 
        # date is denaoted by "fiscalDateEnding"


base_url = 'https://www.alphavantage.co/query?'
params = {'function': 'CASH_FLOW',
		 'symbol': stock_ticker,
		 'apikey': keys}
response_data_cashflow = requests.get(base_url, params=params)



    # LAST ANNUAL CASH FLOW DATA
data_cashflow_annual_last_fiscalDateEnding = response_data_cashflow.json()['annualReports'][0]['fiscalDateEnding']
data_cashflow_annual_last_reportedCurrency = response_data_cashflow.json()['annualReports'][0]['reportedCurrency']
data_cashflow_annual_last_investments = response_data_cashflow.json()['annualReports'][0]['investments']
data_cashflow_annual_last_changeInLiabilities = response_data_cashflow.json()['annualReports'][0]['changeInLiabilities']
data_cashflow_annual_last_cashflowFromInvestment = response_data_cashflow.json()['annualReports'][0]['cashflowFromInvestment']
data_cashflow_annual_last_otherCashflowFromInvestment = response_data_cashflow.json()['annualReports'][0]['otherCashflowFromInvestment']
data_cashflow_annual_last_netBorrowings = response_data_cashflow.json()['annualReports'][0]['netBorrowings']
data_cashflow_annual_last_cashflowFromFinancing = response_data_cashflow.json()['annualReports'][0]['cashflowFromFinancing']
data_cashflow_annual_last_otherCashflowFromFinancing = response_data_cashflow.json()['annualReports'][0]['otherCashflowFromFinancing']
data_cashflow_annual_last_changeInOperatingActivities = response_data_cashflow.json()['annualReports'][0]['changeInOperatingActivities']
data_cashflow_annual_last_netIncome = response_data_cashflow.json()['annualReports'][0]['netIncome']
data_cashflow_annual_last_changeInCash = response_data_cashflow.json()['annualReports'][0]['changeInCash']
data_cashflow_annual_last_operatingCashflow = response_data_cashflow.json()['annualReports'][0]['operatingCashflow']
data_cashflow_annual_last_otherOperatingCashflow = response_data_cashflow.json()['annualReports'][0]['otherOperatingCashflow']
data_cashflow_annual_last_depreciation = response_data_cashflow.json()['annualReports'][0]['depreciation']
data_cashflow_annual_last_dividendPayout = response_data_cashflow.json()['annualReports'][0]['dividendPayout']
data_cashflow_annual_last_stockSaleAndPurchase = response_data_cashflow.json()['annualReports'][0]['stockSaleAndPurchase']
data_cashflow_annual_last_changeInInventory = response_data_cashflow.json()['annualReports'][0]['changeInInventory']
data_cashflow_annual_last_changeInAccountReceivables = response_data_cashflow.json()['annualReports'][0]['changeInAccountReceivables']
data_cashflow_annual_last_changeInNetIncome = response_data_cashflow.json()['annualReports'][0]['changeInNetIncome']
data_cashflow_annual_last_capitalExpenditures = response_data_cashflow.json()['annualReports'][0]['capitalExpenditures']
data_cashflow_annual_last_changeInReceivables = response_data_cashflow.json()['annualReports'][0]['changeInReceivables']
data_cashflow_annual_last_changeInExchangeRate = response_data_cashflow.json()['annualReports'][0]['changeInExchangeRate']
data_cashflow_annual_last_changeInCashAndCashEquivalents = response_data_cashflow.json()['annualReports'][0]['changeInCashAndCashEquivalents']



    # LAST QUARTERLY CASH FLOW DATA
data_cashflow_quarterly_last_fiscalDateEnding = response_data_cashflow.json()['quarterlyReports'][0]['fiscalDateEnding']
data_cashflow_quarterly_last_reportedCurrency = response_data_cashflow.json()['quarterlyReports'][0]['reportedCurrency']
data_cashflow_quarterly_last_investments = response_data_cashflow.json()['quarterlyReports'][0]['investments']
data_cashflow_quarterly_last_changeInLiabilities = response_data_cashflow.json()['quarterlyReports'][0]['changeInLiabilities']
data_cashflow_quarterly_last_cashflowFromInvestment = response_data_cashflow.json()['quarterlyReports'][0]['cashflowFromInvestment']
data_cashflow_quarterly_last_otherCashflowFromInvestment = response_data_cashflow.json()['quarterlyReports'][0]['otherCashflowFromInvestment']
data_cashflow_quarterly_last_netBorrowings = response_data_cashflow.json()['quarterlyReports'][0]['netBorrowings']
data_cashflow_quarterly_last_cashflowFromFinancing = response_data_cashflow.json()['quarterlyReports'][0]['cashflowFromFinancing']
data_cashflow_quarterly_last_otherCashflowFromFinancing = response_data_cashflow.json()['quarterlyReports'][0]['otherCashflowFromFinancing']
data_cashflow_quarterly_last_changeInOperatingActivities = response_data_cashflow.json()['quarterlyReports'][0]['changeInOperatingActivities']
data_cashflow_quarterly_last_netIncome = response_data_cashflow.json()['quarterlyReports'][0]['netIncome']
data_cashflow_quarterly_last_changeInCash = response_data_cashflow.json()['quarterlyReports'][0]['changeInCash']
data_cashflow_quarterly_last_operatingCashflow = response_data_cashflow.json()['quarterlyReports'][0]['operatingCashflow']
data_cashflow_quarterly_last_otherOperatingCashflow = response_data_cashflow.json()['quarterlyReports'][0]['otherOperatingCashflow']
data_cashflow_quarterly_last_depreciation = response_data_cashflow.json()['quarterlyReports'][0]['depreciation']
data_cashflow_quarterly_last_dividendPayout = response_data_cashflow.json()['quarterlyReports'][0]['dividendPayout']
data_cashflow_quarterly_last_stockSaleAndPurchase = response_data_cashflow.json()['quarterlyReports'][0]['stockSaleAndPurchase']
data_cashflow_quarterly_last_changeInInventory = response_data_cashflow.json()['quarterlyReports'][0]['changeInInventory']
data_cashflow_quarterly_last_changeInAccountReceivables = response_data_cashflow.json()['quarterlyReports'][0]['changeInAccountReceivables']
data_cashflow_quarterly_last_changeInNetIncome = response_data_cashflow.json()['quarterlyReports'][0]['changeInNetIncome']
data_cashflow_quarterly_last_capitalExpenditures = response_data_cashflow.json()['quarterlyReports'][0]['capitalExpenditures']
data_cashflow_quarterly_last_changeInReceivables = response_data_cashflow.json()['quarterlyReports'][0]['changeInReceivables']
data_cashflow_quarterly_last_changeInExchangeRate = response_data_cashflow.json()['quarterlyReports'][0]['changeInExchangeRate']
data_cashflow_quarterly_last_changeInCashAndCashEquivalents = response_data_cashflow.json()['quarterlyReports'][0]['changeInCashAndCashEquivalents']
