from Data.HistoricalData import HistoricalData
from Data.Stocks import Stocks
from DataFeed.AlphaVantage import AlphaVantage
import sys

class InsertIntradayData:

	def __init__(self, full_data = False):
		if full_data:
			# Two years of data
			self.amount_years = 2
			self.amount_months = 12
		else:
			# Only last two months
			self.amount_years = 1
			self.amount_months = 2


	def run(self):
		for ticker in Stocks().get_all():

			for year in range(1, self.amount_years + 1):
				for month in range(1, self.amount_months + 1):

					sys.stdout.flush()
					df = AlphaVantage().get_data(ticker = ticker, month = month, year = year)

					historical_data = HistoricalData()

					for index, row in df.iterrows():
						historical_data.insert_stock_price(
							ticker = ticker,
							time_price = str(index),
							open_price = str(row['open']),
							high_price = str(row['high']),
							low_price = str(row['low']),
							close_price = str(row['close']),
							volume = str(row['volume']),
							timeframe = '5m', #TODO: handle different timeframes
						)
						#print(index, row['open'], row['high'], row['low'], row['close'], row['volume'])
