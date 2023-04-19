
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

#Make our first API call
#authenticate trading client
trading_client = TradingClient(API_KEY, API_SECRET, paper=True)

stock_client = StockHistoricalDataClient(API_KEY, API_SECRET)

# multisymbol_request_params = StockLatestQuoteRequest(symbol_or_symbols=["AMZN", "NVDA", "UBER"])
# latest_multisymbol_quotes = stock_client.get_stock_latest_quote(multisymbol_request_params)
# print(latest_multisymbol_quotes)

#Using web-socket API to stream real time data
wss_client = StockDataStream(API_KEY, API_SECRET)

async def quote_data_handler(data):
    print(data)
    
wss_client.subscribe_trades(quote_data_handler, 'AMZN')
wss_client.run()



