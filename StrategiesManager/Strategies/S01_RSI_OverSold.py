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
    	amount = None,
    	ltf_interval="5m",
    	ltf_period="2d",
    	days_between_orders=2,
    	max_positions_amount=3,
    ):
		#print(locals())
		print(ticker)

		if amount is None:
			amount = self.queuesHandler.get_default_amount()
			print("Default Amount is: {}".format(amount))

		if self.queuesHandler.is_there_a_recent_order(ticker, days_between_orders):
			print('There is a recent order for {}'.format(ticker))
			return

		positions_amount = int(self.queuesHandler.get_positions_amount(ticker))
		print('There are {} opened positions for {}'.format(positions_amount, ticker))

		if max_positions_amount <= positions_amount:
			print('Already reached the limit of positions for {}'.format(ticker))
			return
		
		# Calculate RSI using Lower TimeFrame (ltf) data
		data_ltf = self.dataProvider.get(symbol = ticker, interval = ltf_interval, period = ltf_period)
		df_ltf = StockDataFrame.retype(data_ltf)
		
		rsi_key = 'rsi_' + str(rsi_period)
  
		rsi_serie = df_ltf[rsi_key]

		current_rsi = round(rsi_serie[-1], 2)
		previous_rsi = round(rsi_serie[-2], 2)

		#self.__print_df_tail(df_ltf)
		print("Current RSI({}): {}.. Previous RSI value: {}".format(rsi_period, current_rsi, previous_rsi))

		if previous_rsi < rsi_limit:
			takeProfit = amount * tp_percentage / 100

			self.queuesHandler.add_position_to_open(Position(
				ticker = ticker,
				amount = amount,
				stopLoss = False,
				takeProfit = round(takeProfit, 2),
			))

			self.queuesHandler.save_order(ticker)
   
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


	def __print_df_tail(self, df, rows=5):
		import pandas, sys
		pandas.set_option('display.max_columns', None)
		print(df.tail(rows))
		sys.stdout.flush()


	def print_full(self, df):
		pd.set_option('display.max_rows', len(df))
		print(df)
		pd.reset_option('display.max_rows')
