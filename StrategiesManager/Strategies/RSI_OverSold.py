from stockstats import StockDataFrame
from Models.Position import Position

class RSI_OverSold:

	def __init__(self, queuesHandler, dataProvider):
		self.queuesHandler = queuesHandler
		self.dataProvider = dataProvider
		self.__ignore_warnings()


	def perform(self, ticker, rsi_period = 5, rsi_limit = 20, atr_tp_multiplier = 0.5):
		#print(locals())

		# 1 - Calculate Take Profit using daily ATR
		data_daily = self.dataProvider.get(ticker, period="20d", interval="1d")
		df_daily = StockDataFrame.retype(data_daily)
		atr_daily = df_daily['atr'][-2] # Discard last value (real-time price)
		last_close = df_daily['close'][-2]
		move_percentage = atr_daily * 100 / last_close

		# if multiplier is 0.5 -> take profit percentage is half of the daily movement (ATR) 
		tp_percentage = move_percentage * atr_tp_multiplier
		

		# 2 - Calculate RSI using Lower TimeFrame (ltf) data
		data_ltf = self.dataProvider.get(ticker)
		df_ltf = StockDataFrame.retype(data_ltf)
		
		rsi_key = 'rsi_' + str(rsi_period)
  
		print(ticker)
		print(round(tp_percentage,2))

		# 3 - Open a position if RSI value is crossing up the limit
		is_crossing_up = self.__crossover(
    		series = df_ltf[rsi_key], 
    		limit = rsi_limit,
			offset = 2
    	)

		if is_crossing_up or True:
			amount = 200
			takeProfit = amount * tp_percentage / 100
			print('take profit {}'.format(takeProfit))

			self.queuesHandler.add_position_to_open(Position(
				ticker = ticker,
				amount = amount,
				stopLoss = -3, #TODO: False
				takeProfit = round(takeProfit, 2),
			))
   
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
