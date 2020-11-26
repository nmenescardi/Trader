from Data.DB import DB
from Data.AbstractDAO import AbstractDAO
from datetime import datetime


class HistoricalData(AbstractDAO):

	def __init__(self):
		super(HistoricalData, self).__init__()
		self.ticker_ids = {}


	def get_ticker_id(self, ticker):
		if ticker in self.ticker_ids:
			return self.ticker_ids[ticker]

		#TODO: Refactor into separate 'Stocks' DAO
		cursor = self.execute("SELECT stock_id FROM stocks WHERE ticker = %s;",
			(ticker,)
		)

		ticker_id_result = cursor.fetchone()

		if ticker_id_result is None:
			raise Exception #TODO: custom Exception

		self.ticker_ids[ticker] = ticker_id_result[0]

		return ticker_id_result[0]


	def insert_stock_price(self, ticker, time_price, open_price, high_price, low_price, close_price, volume, timeframe):

		ticker_id = self.get_ticker_id(ticker)

		self.execute(
			"""
				INSERT IGNORE INTO stock_prices 
					(stock_id, time_price, open_price, high_price, low_price, close_price, volume, timeframe)
				VALUES 
					(%s,%s,%s,%s,%s,%s,%s,%s);
			""",
			(ticker_id, time_price, open_price, high_price, low_price, close_price, volume, timeframe, )
		)
		self.db.commit()
