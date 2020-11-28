from HistoricalData.Indicators.Abstract_Indicator import Abstract_Indicator

class Is_Trending_Above_SMAs(Abstract_Indicator):

	def calculate(self, **kwargs):
		fast_MA =  kwargs.get('fast_MA', '20')
		med_MA =  kwargs.get('med_MA', '50')
		slow_MA =  kwargs.get('slow_MA', '200')

		sma_db_key = 'Is_Trending_Above_SMAs'
		is_trending_above_smas = False

		close = round(self.data['close'][-1], 2)

		fast_sma_df_key = 'close_{}_sma'.format(fast_MA)
		fast_sma = round(self.data[fast_sma_df_key][-1], 2)
		med_sma_df_key = 'close_{}_sma'.format(med_MA)
		med_sma = round(self.data[med_sma_df_key][-1], 2)
		slow_sma_df_key = 'close_{}_sma'.format(slow_MA)
		slow_sma = round(self.data[slow_sma_df_key][-1], 2)

		if (
			close > fast_sma 
			and fast_sma > med_sma
			and med_sma > slow_sma
		):
			is_trending_above_smas = True

		return sma_db_key, is_trending_above_smas
