import datetime
from Data.HistoricalData import HistoricalData
from backtrader import DataBase, date2num

class MySQL(DataBase):
	params = (
		('ticker', "AAPL"),
		('fromdate', datetime.datetime.min),
		('todate', datetime.datetime.max),
	)

	def start(self):
		self.result = HistoricalData().get_prices(
			ticker = self.p.ticker,
			from_date = self.p.fromdate,
			to_date = self.p.todate
		)

	def _load(self):
		one_row = self.result.fetchone()
		if one_row is None:
			return False

		self.lines.datetime[0] = date2num(one_row[0]) # for intraday data, time also need to be combined here.
		self.lines.open[0] = float(one_row[1])
		self.lines.high[0] = float(one_row[2])
		self.lines.low[0] = float(one_row[3])
		self.lines.close[0] = float(one_row[4])
		self.lines.volume[0] = int(one_row[5])
		self.lines.openinterest[0] = -1
		return True
