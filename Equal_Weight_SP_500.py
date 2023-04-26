
import numpy as np
import pandas as pd
import requests
import math
#import xlsxwriter
import csv
import asyncio
import csv
import alpaca_trade_api as api
from alpaca_keys import API_KEY, API_SECRET, BASE_URL

from alpaca.trading.client import TradingClient
from alpaca.trading.requests import GetAssetsRequest
from alpaca.trading.enums import AssetClass
from alpaca.data.historical import StockHistoricalDataClient
from alpaca.data.requests import StockLatestQuoteRequest
from alpaca.data.live import StockDataStream
from alpaca.data.requests import CryptoBarsRequest
from alpaca.data.timeframe import TimeFrame

#save s&p 500 stocks as a pandas dataframe
#import list of stocks
stocks = pd.read_csv('/Users/alvinpl/Desktop/sp_500/sp_500_stocks.csv')
#stocks

#acquire API token
alpaca = api.REST(API_KEY, API_SECRET, BASE_URL)


#ACCESS stock symbol and price 
stock_client = StockHistoricalDataClient(API_KEY, API_SECRET)

multisymbol_request_params = StockLatestQuoteRequest(symbol_or_symbols=["NVDA"]) #"NVDA", "UBER"
latest_multisymbol_quotes = stock_client.get_stock_latest_quote(multisymbol_request_params)
print('Stock Symbol Data')
print(latest_multisymbol_quotes)

#PARSING out data
print('parsed data:')
print(latest_multisymbol_quotes['NVDA'].ask_price)

#ADDING our stock data to a pandas dataframe
my_columns = ['Ticker','Stock','Market Capitalization','Number of Shares to Buy']
final_dataframe = pd.DataFrame([[0,0,0,0]],columns=my_columns)
print('Dataframe: ')
print(final_dataframe)


#Make our first API call
#authenticate trading client
trading_client = TradingClient(API_KEY, API_SECRET, paper=True)
#Using web-socket API to stream real time data
# wss_client = StockDataStream(API_KEY, API_SECRET)

# async def quote_data_handler(data):
#     #print trade data, get the size and price
#     print(data)
    
# wss_client.subscribe_trades(quote_data_handler, 'AMZN')
# wss_client.run()



