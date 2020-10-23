from Order_Queues.Order_Queues import Order_Queues
from .yFinanceDataProvider import yFinanceDataProvider 
from .S01_RSI_OverSold import RSI_OverSold
from .Setup import StrategiesSetup

class StrategiesFactory:

	def __init__(self):
		self.queuesHandler = Order_Queues()
		self.dataProvider = yFinanceDataProvider()


	def make(self, strategy_key):
		if(strategy_key == StrategiesSetup.RSI_OverSold):
			return RSI_OverSold(
				queuesHandler = self.queuesHandler, 
				dataProvider = self.dataProvider
			)
