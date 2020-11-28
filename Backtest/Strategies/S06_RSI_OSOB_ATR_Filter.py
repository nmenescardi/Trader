import backtrader as bt
from .S00_Abstract_Strategy import Abstract_Strategy
from CustomIndicators.ATR_Delta import ATR_Delta
from CustomIndicators.SuperTrend import SuperTrend

class RSI_OSOB_ATR_Filter(Abstract_Strategy):
	params = (
		('rsi_length', 2),
		('rsi_buy_limit', 10),
		('rsi_sell_limit', 90),
		('atr_delta_filter', False),
	)

	def __init__(self):
		super().__init__()

		# Indicators
		self.rsi = bt.indicators.RSI_Safe(self.datas[0], period=self.params.rsi_length)

		self.atr_delta = ATR_Delta(self.datas[0])

		self.htf_supertrend = SuperTrend(self.datas[0], period=14, multiplier=4)
		#self.fast_sma = bt.indicators.SmoothedMovingAverage(self.datas[0], period=20)
		#self.slow_sma = bt.indicators.SmoothedMovingAverage(self.datas[0], period=50)
		#self.trend_sma = bt.indicators.SmoothedMovingAverage(self.datas[0], period=200)


	def prenext(self):
		if len(self) > 14:
			self.next()


	def next(self):
		self.log('Close, %.2f' % self.dataclose[0])
  
		self.log('Position {}'.format(self.position.size))
  
		self.log('ATR SMA Delta {}'.format(self.atr_delta[0]))

		if self.order:
			return

		if not self.position.size: # Only one order at a time
			if self.rsi <= self.params.rsi_buy_limit: # RSI check

				if not isinstance(self.p.atr_delta_filter, bool): # if filter is applied
					if self.atr_delta[0] > self.p.atr_delta_filter:
						self.log('Buy order using filter')
						self.order = self.buy()
				else:
					self.log('Buy order without filter')
					self.order = self.buy() # No filter -> Buy anyway

		elif self.rsi >= self.params.rsi_sell_limit:
				self.sell()

	
	def getParamsForResult(self):
		return {
			'RSI Length' : [self.params.rsi_length],
			'RSI Buy Limit' : [self.params.rsi_buy_limit],
			'RSI Sell Limit' : [self.params.rsi_sell_limit],
			'ATR Delta Filter' : [self.params.atr_delta_filter],
		}
