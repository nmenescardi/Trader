from Data.DB import DB
from Data.AbstractDAO import AbstractDAO
from Data.Stocks import Stocks
from datetime import datetime


class Indicators(AbstractDAO):

	def __init__(self):
		super(Indicators, self).__init__()
		self.stocksDAO = Stocks()


	def insert_value(self, ticker, indicator_key, indicator_value, date_time, main_timeframe = '1d'):

		ticker_id = self.stocksDAO.get_ticker_id(ticker)

		self.execute(
			"""
				INSERT IGNORE INTO indicators 
					(stock_id, indicator_key, indicator_value, main_timeframe, date_time)
				VALUES 
					(%s,%s,%s,%s,%s);
			""",
			(ticker_id, indicator_key, indicator_value, main_timeframe, date_time, )
		)
		self.db.commit()
