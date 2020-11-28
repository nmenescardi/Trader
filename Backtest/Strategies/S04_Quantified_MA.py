import backtrader as bt
from .S00_Abstract_Strategy import Abstract_Strategy

class Quantified_MA(Abstract_Strategy):
	params = (
		('sma_pair_length', (5,10,)),
		('sma_closing_length', 5),
		('sma_delta', 25), # Possible range [1-100]
	)

	def __init__(self):
		super().__init__()

		self.sma_delta_percentage = self.p.sma_delta / 10
		self.log('SMA Delta {}'.format(self.sma_delta_percentage))

		self.fast_sma_length = self.p.sma_pair_length[0]
		self.slow_sma_length = self.p.sma_pair_length[1]

		# Indicators
		self.fast_sma = bt.indicators.SmoothedMovingAverage(self.datas[0], period=self.fast_sma_length)
		self.slow_sma = bt.indicators.SmoothedMovingAverage(self.datas[0], period=self.slow_sma_length)
		self.closing_sma = bt.indicators.SmoothedMovingAverage(self.datas[0], period=self.p.sma_closing_length)
		self.trend_sma = bt.indicators.SmoothedMovingAverage(self.datas[0], period=200)


	def next(self):
		self.log('Close, %.2f' % self.ltf_dataclose[0])
  
		self.log('Position {}'.format(self.position.size))

		if self.order:
			return

		if not self.position.size: # Only one order at a time
			if self.ltf_dataclose[0] > self.trend_sma:

				sma_delta = ((self.fast_sma[0] / self.slow_sma[0]) - 1) * 100
				self.log('Fast {}. Slow {}. Delta {}.'.format(self.fast_sma[0], self.slow_sma[0], sma_delta))
    
				if sma_delta < -self.sma_delta_percentage:

					self.log('BUY at {}.'.format(self.ltf_dataclose[0]))
					self.order = self.buy()

		else:
			if self.ltf_dataclose[0] > self.closing_sma:
				self.sell()

	
	def getParamsForResult(self):
		return {
			'Fast SMA' : [self.fast_sma_length],
			'Slow SMA' : [self.slow_sma_length],
			'Closing SMA' : [self.p.sma_closing_length],
			'SMA Delta' : [self.p.sma_delta],
		}
