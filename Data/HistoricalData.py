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


	def get_prices(self, ticker, from_date, to_date):

		ticker_id = self.stocksDAO.get_ticker_id(ticker)

		from_date_str = from_date.strftime("%Y-%m-%d") + ' 00:00'
		to_date_str = to_date.strftime("%Y-%m-%d") + ' 23:59'

		return self.execute(
			"""
				SELECT time_price,open_price,high_price,low_price,close_price,volume
				FROM stock_prices
				WHERE stock_id = %s AND time_price between %s and %s
				ORDER BY time_price ASC;
			""",
			(ticker_id, from_date_str, to_date_str, )
		)
