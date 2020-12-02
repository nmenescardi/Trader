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


	def time_series_intraday_extended(self, ticker, interval, data_slice, adjusted, seconds_to_wait):
		
		url = '{}?function=TIME_SERIES_INTRADAY_EXTENDED&symbol={}&interval={}&slice={}&adjusted={}&apikey={}'

		data = pd.read_csv(url.format(self.apiUrl, ticker, self.get_interval(interval), data_slice, adjusted,  self.key))

		
		print('Done slice {}. Ticker: {}. Waiting {} seconds...'.format(data_slice, ticker, seconds_to_wait))
		time.sleep(seconds_to_wait)

		return self.remove_extended_hours(data)


	def get_data(self, ticker = 'AAPL', month = 12, year = 2, data_slice = None, tries = 1):

		try:
			if data_slice is None:
				data_slice = self.get_slice(year, month)

			return self.time_series_intraday_extended(
				ticker = ticker, 
				interval = self.Interval._5min, 
				data_slice = data_slice, 
				adjusted = self.Adjusted.false,
				seconds_to_wait = 60 * tries
			)
		except Exception as e:

			print('Exception getting {}. Ticker: {}. Exception: {}. Tries: {}'.format(data_slice, ticker, e, tries))
			print(type(e))

			if tries < 3:
				return self.get_data(
					ticker = ticker,
					data_slice = data_slice,
					tries = tries + 1
				)
			
			return None
