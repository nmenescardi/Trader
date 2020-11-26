from Data.DB import DB
from Data.AbstractDAO import AbstractDAO
from Data.Stocks import Stocks
from datetime import datetime


class HistoricalData(AbstractDAO):

	def __init__(self):
		super(HistoricalData, self).__init__()
		self.stocksDAO = Stocks()


	def insert_stock_price(self, ticker, time_price, open_price, high_price, low_price, close_price, volume, timeframe):

		ticker_id = self.stocksDAO.get_ticker_id(ticker)

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
