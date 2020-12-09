from Data.Indicators import Indicators as indicatorsDAO
from Data.Stocks import Stocks
from DataFeed.YFinanceFeed import YFinanceFeed
from HistoricalData.Indicators.DailySetup import DailySetup
from Logger import Logger

class InsertDailyIndicators:

	def __init__(self, period = '250d'):
		self.period = period
		self.logger = Logger().get_logger()


	def run(self):
		indicators_dao = indicatorsDAO()

		stock_list = Stocks().get_all()
		self.logger.info('0041 - Ticker list: {}'.format(stock_list))
  
		for ticker in stock_list:
			self.logger.info('0038 - Calculating indicators for {}'.format(ticker))

			data = YFinanceFeed().get(ticker, period = self.period, interval = "1d")
			if data.empty:
				self.logger.info('0039 - No data for {}'.format(ticker))
				continue

			for indicator_class, indicator_config in DailySetup.config.items():
				
				indicator = indicator_class(data)
				for params in indicator_config:

					indicator_key, indicator_value = indicator.calculate( **params )

					self.logger.info('0040 - Inserting {} - {}'.format(indicator_key, indicator_value))

					indicators_dao.insert_value(
						ticker = ticker,
						indicator_key = indicator_key, 
						indicator_value = str(indicator_value), 
						date_time = str(data.index[-1]),
						main_timeframe = '1d'
					)
