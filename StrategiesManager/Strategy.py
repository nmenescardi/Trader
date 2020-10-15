from stockstats import StockDataFrame

class Strategy:

	def __init__(self, queuesHandler, dataProvider):
		self.queuesHandler = queuesHandler
		self.dataProvider = dataProvider


	def perform(self, ticker):
		data = self.dataProvider.get(ticker)
		df = StockDataFrame.retype(data)

		print(df.tail())
		
		rsi_period = 5
		rsi_key = 'rsi_' + str(rsi_period)
		print(df[rsi_key], 2)
  
		rsi_value = df[rsi_key][-2]  # Discard last value. Consider the one before that
