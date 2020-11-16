import time, pandas as pd
from .Strategies.Setup import StrategiesSetup
from .Strategies.Factory import StrategiesFactory

class Manager:

	def __init__(self):
		self.strategies_factory = StrategiesFactory()


	def run(self):
		while(True):
			for strategy_key, strategy_config in StrategiesSetup.config.items():
				for params in strategy_config:
					strategy = self.strategies_factory.make(strategy_key)
					strategy.perform(**params)
					#time.sleep(1)
