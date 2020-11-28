import backtrader as bt
from .S00_Abstract_Strategy import Abstract_Strategy

class Quantified_MA_Delta_Close(Abstract_Strategy):
	params = (
		('slow_sma_length', 10),
		('sma_closing_length', 5),
		('sma_delta', 25),
	)

	def __init__(self):
		self.sma_delta_percentage = self.p.sma_delta / 10
		self.log('SMA Delta {}'.format(self.sma_delta_percentage))

		# Indicators
		self.slow_sma = bt.indicators.SmoothedMovingAverage(self.datas[0], period=self.p.slow_sma_length)
		self.closing_sma = bt.indicators.SmoothedMovingAverage(self.datas[0], period=self.p.sma_closing_length)
		self.trend_sma = bt.indicators.SmoothedMovingAverage(self.datas[0], period=200)


	def next(self):
		self.log('Close, %.2f' % self.ltf_dataclose[0])

		self.log('Position {}'.format(self.position.size))

		if self.order:
			return

		if not self.position.size: # Only one order at a time
			if self.ltf_dataclose[0] > self.trend_sma:

				sma_delta = ((self.ltf_dataclose[0] / self.slow_sma[0]) - 1) * 100
				self.log('Slow {}. Delta {}.'.format(self.slow_sma[0], sma_delta))
    
				if sma_delta < -self.sma_delta_percentage:

					self.log('BUY at {}.'.format(self.ltf_dataclose[0]))
					self.order = self.buy()

		else:
			if self.ltf_dataclose[0] > self.closing_sma:
				self.sell()

	
	def getParamsForResult(self):
		return {
			'Slow SMA' : [self.p.slow_sma_length],
			'Closing SMA' : [self.p.sma_closing_length],
			'SMA Delta' : [self.p.sma_delta],
		}
