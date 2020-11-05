from stockstats import StockDataFrame
from Models.Position import Position

class RSI_OverSold:

	def __init__(self, queuesHandler, dataProvider):
		self.queuesHandler = queuesHandler
		self.dataProvider = dataProvider
		self.__ignore_warnings()


	def perform(
    	self, 
    	ticker, 
    	rsi_period = 5, 
    	rsi_limit = 20, 
    	tp_percentage = 0.5, 
    	amount = 200, 
    	ltf_interval="5m",
    	ltf_period="2d"
    ):
		#print(locals())
		
		# Calculate RSI using Lower TimeFrame (ltf) data
		data_ltf = self.dataProvider.get(symbol = ticker, interval = ltf_interval, period = ltf_period)
		df_ltf = StockDataFrame.retype(data_ltf)
		
		rsi_key = 'rsi_' + str(rsi_period)
  
		print(ticker)

		if df_ltf[rsi_key][-2] < rsi_limit:
			takeProfit = amount * tp_percentage / 100

			self.queuesHandler.add_position_to_open(Position(
				ticker = ticker,
				amount = amount,
				stopLoss = False,
				takeProfit = round(takeProfit, 2),
			))
   
			print('Opening a position for {}. Take profit {}'.format(ticker, takeProfit))


	def __crossover(self, series, limit, offset = 1):
		last_index = - offset
		previous_index = last_index - 1
  
		last_value = round(series[last_index], 2)
		previous_value = round(series[previous_index], 2)

		print("Last: {}, Previous: {}".format(last_value, previous_value))
		
		if( previous_value <= limit and last_value > limit):
			return True
		return False


	def __ignore_warnings(self):
		import warnings, logging
		warnings.filterwarnings("ignore")
		logging.disable(logging.CRITICAL)