
from __future__ import (absolute_import, division, print_function,
						unicode_literals)

import backtrader as bt

class SMA_Delta(bt.Indicator):
	params = (('fast_sma_period', 3), ('slow_sma_period', 25),)
	lines = ('sma_delta',)
	#plotinfo = dict(subplot=False)

	def __init__(self):
		self.fast_sma = bt.indicators.SimpleMovingAverage(self.datas[0], period=self.p.fast_sma_period)
		self.slow_sma = bt.indicators.SimpleMovingAverage(self.datas[0], period=self.p.slow_sma_period)
		self.sma_delta = ((self.fast_sma / self.slow_sma) - 1) * 100

	def next(self):
		self.l.sma_delta[0] = self.sma_delta[0]

