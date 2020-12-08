from Data.DB import DB
from Data.AbstractDAO import AbstractDAO
from datetime import datetime


class Stocks(AbstractDAO):

	def __init__(self):
		super(Stocks, self).__init__()
		self.ticker_ids = {} #TODO: static property?

	
	def get_all(self):
		iterator = self.execute("SELECT * FROM stocks;", named_tuple=True)

		stocks = []

		for stock in iterator:
			# Update cache
			self.ticker_ids[stock.ticker] = stock.stock_id

			# Add to result list
			stocks.append(stock.ticker)
		
		return stocks

	
	def get_focus(self):
		iterator = self.execute(
			"""
				SELECT st.* FROM stocks st
				INNER JOIN stock_list sl
				ON st.stock_id = sl.stock_id
				WHERE sl.list_id = 1 OR sl.list_id = 2
			"""
			, named_tuple=True
		)

		stocks = []

		for stock in iterator:
			# Update cache
			self.ticker_ids[stock.ticker] = stock.stock_id

			# Add to result list
			stocks.append(stock.ticker)
		
		return stocks


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
