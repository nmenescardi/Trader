import time, pandas as pd
from yFinanceDataProvider import yFinanceDataProvider 
from Strategy import Strategy

class Manager:

	def __init__(self, queuesHandler):
		self.strategy = Strategy(
			queuesHandler = queuesHandler, 
			dataProvider = yFinanceDataProvider()
		)
		self.minutesToWait = 0.5
		self.tickerList = ['TSLA']


	def run(self):		
		while(True):
			for ticker in self.tickerList:
				self.strategy.perform(ticker)

			time.sleep(60 * self.minutesToWait)
