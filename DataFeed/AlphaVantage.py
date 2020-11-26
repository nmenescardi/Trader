import os,time
import pandas as pd
from enum import Enum  
from dotenv import load_dotenv

class AlphaVantage():
	
	def __init__(self):
		load_dotenv()
		self.key = os.getenv("ALPHAVANTAGE_API_KEY")
		self.apiUrl = 'https://www.alphavantage.co/query'

		self.Adjusted = Enum('Adjusted', 'true false')
		self.Interval = Enum('Interval', '_1min _5min _15min _30min _60min')
		self.OutputSize = Enum('outputsize', 'compact full')
		self.DataType = Enum('datatype', 'json csv')


	def get_slice(self, year, month):
		return 'year{}month{}'.format(year, month) 


	def get_interval(self, interval):
		return interval.name[1:] 

	
	def remove_extended_hours(self, data):
		data['time'] = pd.to_datetime(data['time'])
		data = data.set_index('time')
		return data.between_time('09:30', '16:00')


	def time_series_intraday_extended(self, symbol, interval, slice, adjusted):
		
		url = '{}?function=TIME_SERIES_INTRADAY_EXTENDED&symbol={}&interval={}&slice={}&adjusted={}&apikey={}'

		try:
			time.sleep(5)
			data = pd.read_csv(url.format(self.apiUrl, symbol, self.get_interval(interval), slice, adjusted,  self.key))

			print('Done slice {}. Ticker: {}'.format(slice, symbol))

			return self.remove_extended_hours(data)

		except Exception as e:
			print('Exception getting slice {}. Ticker: {}. Exception: {}'.format(slice, symbol, e))
			return pd.DataFrame()


	def get_data(self, symbol = 'AAPL', amount_years = 2, amount_months = 12):

		data = []
		
		for year in range(1, amount_years + 1):
			for month in range(1, amount_months + 1):
				data.append(
    				self.time_series_intraday_extended(
            			symbol, 
            			self.Interval._5min, 
            			self.get_slice(year,month), 
            			self.Adjusted.false
            		)
    			)
		
		return pd.concat(data) # return single DF
