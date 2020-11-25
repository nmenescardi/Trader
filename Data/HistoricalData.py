from Data.DB import DB
from Data.AbstractDAO import AbstractDAO
from datetime import datetime


class HistoricalData(AbstractDAO):

	def insert_stock_price(self, ticker, time_price, open_price, high_price, low_price, close_price, volume, timeframe):

		cursor = self.execute("SELECT stock_id FROM stocks WHERE ticker = %s;",
			(ticker,)
		)

		ticker_id_result = cursor.fetchone()

		if ticker_id_result is None:
			return

		ticker_id = ticker_id_result[0]

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
