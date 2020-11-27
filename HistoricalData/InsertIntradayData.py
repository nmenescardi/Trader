from Data.HistoricalData import HistoricalData
from Data.Stocks import Stocks
from DataFeed.AlphaVantage import AlphaVantage

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

			df = AlphaVantage().get_data(ticker, amount_years = self.amount_years, amount_months = self.amount_months)

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
