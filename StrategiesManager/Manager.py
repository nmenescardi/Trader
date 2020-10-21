import time, pandas as pd
from .yFinanceDataProvider import yFinanceDataProvider 
from .Strategies.RSI_OverSold import RSI_OverSold
from .StrategiesSetup import StrategiesSetup

class Manager:

	def __init__(self, queuesHandler):
		self.strategy = RSI_OverSold(
			queuesHandler = queuesHandler, 
			dataProvider = yFinanceDataProvider()
		)

		# Get params for current strategy
		strategy_name = type(self.strategy).__name__
		self.strategy_params = StrategiesSetup.config.get(strategy_name)


	def run(self):
		while(True):
			for params in self.strategy_params:
				self.strategy.perform(**params)
				time.sleep(1)
