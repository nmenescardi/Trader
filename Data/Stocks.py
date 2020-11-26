from Data.DB import DB
from Data.AbstractDAO import AbstractDAO
from datetime import datetime


class Stocks(AbstractDAO):

	def __init__(self):
		super(Stocks, self).__init__()
		self.ticker_ids = {}


	def get_ticker_id(self, ticker):
		if ticker in self.ticker_ids:
			return self.ticker_ids[ticker]

		cursor = self.execute("SELECT stock_id FROM stocks WHERE ticker = %s;",
			(ticker,)
		)

		ticker_id_result = cursor.fetchone()

		if ticker_id_result is None:
			raise Exception #TODO: custom Exception

		self.ticker_ids[ticker] = ticker_id_result[0]

		return ticker_id_result[0]