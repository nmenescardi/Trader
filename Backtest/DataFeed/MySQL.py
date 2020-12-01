import datetime
from Data.HistoricalData import HistoricalData
from backtrader import DataBase, date2num

class MySQL(DataBase):
	params = (
		('ticker', "AAPL"),
		('fromdate', datetime.datetime.min),
		('todate', datetime.datetime.max),
	)

	def __init__(self):
		iterator = HistoricalData().get_prices(
			ticker = self.p.ticker,
			from_date = self.p.fromdate,
			to_date = self.p.todate
		)
		self.price_rows = iterator.fetchall()


	def start(self):
		self.price_i = 0


	def _load(self):
		if self.price_i >= len(self.price_rows):
			return False
		one_row = self.price_rows[self.price_i]
		self.price_i += 1

		self.lines.datetime[0] = date2num(one_row[0])
		self.lines.open[0] = float(one_row[1])
		self.lines.high[0] = float(one_row[2])
		self.lines.low[0] = float(one_row[3])
		self.lines.close[0] = float(one_row[4])
		self.lines.volume[0] = int(one_row[5])
		self.lines.openinterest[0] = -1
		return True
