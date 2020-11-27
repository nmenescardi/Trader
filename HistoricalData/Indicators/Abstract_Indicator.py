from abc import ABC, abstractmethod
from stockstats import StockDataFrame

class Abstract_Indicator(ABC):

	def __init__(self, data):
		self.data = StockDataFrame.retype(data)
		#TODO: error handling


	@abstractmethod
	def calculate(self, **kwargs):
		pass
