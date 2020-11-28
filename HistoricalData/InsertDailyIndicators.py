from Data.Indicators import Indicators as indicatorsDAO
from Data.Stocks import Stocks
from DataFeed.YFinanceFeed import YFinanceFeed
from HistoricalData.Indicators.DailySetup import DailySetup

class InsertDailyIndicators:

	def __init__(self, period = '250d'):
		self.period = period


	def run(self):
		indicators_dao = indicatorsDAO()
  
		for ticker in Stocks().get_all():
			print('Calculating indicators for {}'.format(ticker))

			data = YFinanceFeed().get(ticker, period = self.period, interval = "1d")
			if data.empty:
				print('No data for {}'.format(ticker))
				continue

			for indicator_class, indicator_config in DailySetup.config.items():
				
				indicator = indicator_class(data)
				for params in indicator_config:

					indicator_key, indicator_value = indicator.calculate( **params )

					indicators_dao.insert_value(
						ticker = ticker,
						indicator_key = indicator_key, 
						indicator_value = str(indicator_value), 
						date_time = str(data.index[-1]),
						main_timeframe = '1d'
					)
