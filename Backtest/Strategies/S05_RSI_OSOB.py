import backtrader as bt
from .S00_Abstract_Strategy import Abstract_Strategy
from ..CustomIndicators.ATR_Delta import ATR_Delta
from ..CustomIndicators.SuperTrend import SuperTrend
from ..CustomIndicators.SMA_Delta import SMA_Delta

class RSI_OSOB(Abstract_Strategy):
	params = (
		('rsi_length', 2),
		('rsi_buy_limit', 10),
		('rsi_sell_limit', 90),
		('number_bars_stop', False),
	)

	def __init__(self):
		super().__init__()

		# Indicators
		self.rsi = bt.indicators.RSI_Safe(self.datas[0], period=self.params.rsi_length)

		self.atr_delta = ATR_Delta(self.datas[0])

		self.htf_supertrend = SuperTrend(self.datas[0], period=14, multiplier=4)
		self.sma_delta = SMA_Delta(self.datas[0])
		self.fast_sma = bt.indicators.SimpleMovingAverage(self.datas[0], period=3)
		self.slow_sma = bt.indicators.SimpleMovingAverage(self.datas[0], period=25)
		self.trend_sma = bt.indicators.SimpleMovingAverage(self.datas[0], period=100)
		self.trend_sma = bt.indicators.SimpleMovingAverage(self.datas[0], period=200)


	def prenext(self):
		if len(self) > 14:
			self.next()


	def next(self):
		self.log('Close, %.2f' % self.dataclose[0])
  
		self.log('Position {}'.format(self.position.size))

		if self.order:
			return

		if not self.position.size: # Only one order at a time
			if self.rsi <= self.params.rsi_buy_limit: # RSI check

				self.order = self.buy()

		else: 
			if self.rsi >= self.params.rsi_sell_limit:
				self.sell()
				return

			else:
				self.maybe_limit_number_bars()

	
	def getParamsForResult(self):
		return {
			'RSI Length' : [self.p.rsi_length],
			'RSI Buy Limit' : [self.p.rsi_buy_limit],
			'RSI Sell Limit' : [self.p.rsi_sell_limit],
			'Days To Stop' : [self.p.number_bars_stop],
		}
