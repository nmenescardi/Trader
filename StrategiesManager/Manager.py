import time, pandas as pd
from .Strategies.Setup import StrategiesSetup
from .Strategies.Factory import StrategiesFactory

class Manager:

	def __init__(self):
		self.strategies_factory = StrategiesFactory()


	def run(self):
		while(True):
			for strategy_key, strategy_config in StrategiesSetup.config.items():
				try:
					strategy = self.strategies_factory.make(strategy_key)
					for params in strategy_config:
						strategy.perform(**params)
				except Exception as e:
					print('Exception reading data feed: {}.'.format(e))
					time.sleep(120)
