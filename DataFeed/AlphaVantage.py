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

		data = pd.read_csv(url.format(self.apiUrl, symbol, self.get_interval(interval), slice, adjusted,  self.key))

		seconds_to_wait = 5
		print('Done slice {}. Ticker: {}. Waiting {} seconds...'.format(slice, symbol, seconds_to_wait))
		time.sleep(seconds_to_wait)

		return self.remove_extended_hours(data)


	def get_data(self, ticker = 'AAPL', month = 12, year = 2):

		try:
			data_slice = self.get_slice(year, month)
			return self.time_series_intraday_extended(
				ticker, 
				self.Interval._5min, 
				data_slice, 
				self.Adjusted.false
			)
		except Exception as e:
			#TODO: try again or save it for later
			print('Exception getting {}. Ticker: {}. Exception: {}'.format(data_slice, ticker, e))
			return pd.DataFrame()
	
