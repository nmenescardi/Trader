from HistoricalData.Indicators.Abstract_Indicator import Abstract_Indicator

class SMA(Abstract_Indicator):

	def calculate(self, **kwargs):
		period =  kwargs.get('period', '200')

		#TODO: Check if df has enough periods. Otherwise save a default value like 'N/A'. Send it to Abstract 

		sma_df_key = 'close_{}_sma'.format(period)
		sma_value = round(self.data[sma_df_key][-1], 2)

		sma_db_key = 'SMA_{}'.format(period)

		return sma_db_key, sma_value
