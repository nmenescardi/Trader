from HistoricalData.Indicators.Abstract_Indicator import Abstract_Indicator

class Is_Above_SMAs(Abstract_Indicator):

	def calculate(self, **kwargs):
		periods =  kwargs.get('periods', ['200'])

		sma_db_key = 'Is_Above_SMAs'
		is_above_SMAs = True

		close = round(self.data['close'][-1], 2)

		for period in periods:

			sma_df_key = 'close_{}_sma'.format(period)
			sma_value = round(self.data[sma_df_key][-1], 2)

			sma_db_key += '_{}'.format(period)
			
			if close < sma_value:
				is_above_SMAs = False


		return sma_db_key, is_above_SMAs
