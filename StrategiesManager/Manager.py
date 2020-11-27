import time, pandas as pd
from .Strategies.Setup import StrategiesSetup
from .Strategies.Factory import StrategiesFactory
from Helpers.Market import Market 

class Manager:

	def __init__(self):
		self.strategies_factory = StrategiesFactory()
		self.market_helper = Market()
		self.should_print_market_status = True

	
	def is_market_closed(self):
		if not self.market_helper.is_market_open():
			if self.should_print_market_status:
				print('Market is Closed...')
				self.should_print_market_status = False

			return True

		print('Market is Open')
		self.should_print_market_status = True
		return False


	def run(self):
		while(True):
			if self.is_market_closed():
				continue

			for strategy_key, strategy_config in StrategiesSetup.config.items():
				try:
					strategy = self.strategies_factory.make(strategy_key)
					for params in strategy_config:
						strategy.perform(**params)
				except Exception as e:
					print('Exception reading data feed: {}.'.format(e))
					time.sleep(120)
