from HistoricalData.Indicators.Abstract_Indicator import Abstract_Indicator

class RSI(Abstract_Indicator):

	def calculate(self, **kwargs):
		period =  kwargs.get('period', '200')

		#TODO: Check if df has enough periods. Otherwise save a default value like 'N/A'. Send it to Abstract 

		rsi_df_key = 'rsi_{}'.format(period)

		rsi_value = round(self.data[rsi_df_key][-1], 2)

		rsi_db_key = 'RSI_{}'.format(period)

		return rsi_db_key, rsi_value
