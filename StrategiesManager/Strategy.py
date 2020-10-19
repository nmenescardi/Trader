from stockstats import StockDataFrame

class Strategy:

	def __init__(self, queuesHandler, dataProvider):
		self.queuesHandler = queuesHandler
		self.dataProvider = dataProvider
		self.__ignore_warnings()


	def perform(self, ticker, rsi_period = 5, rsi_limit = 20):
		data = self.dataProvider.get(ticker)
		df = StockDataFrame.retype(data)
		
		rsi_key = 'rsi_' + str(rsi_period)
		#print(df[rsi_key], 2)
  
		print(ticker)

		is_crossing_up = self.__crossover(
    		series = df[rsi_key], 
    		limit = rsi_limit,
			offset = 2
    	)

		if is_crossing_up:
			self.queuesHandler.add_ticker_to_open(ticker)
			print('Opening a position for {}'.format(ticker))


	def __crossover(self, series, limit, offset = 1):
		last_index = - offset
		previous_index = last_index - 1
  
		last_value = series[last_index]
		previous_value = series[previous_index]

		print("Last: {}, Previous: {}".format(last_value, previous_value))
		
		if( previous_value <= limit and last_value > limit):
			return True
		return False


	def __ignore_warnings(self):
		import warnings, logging
		warnings.filterwarnings("ignore")
		logging.disable(logging.CRITICAL)
