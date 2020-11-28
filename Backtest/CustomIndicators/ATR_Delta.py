
from __future__ import (absolute_import, division, print_function,
						unicode_literals)

import backtrader as bt

class ATR_Delta(bt.Indicator):
	params = (('atr_period', 7), ('sma_period', 50),)
	lines = ('atr_sma_delta',)
	#plotinfo = dict(subplot=False)

	def __init__(self):
		self.atr = bt.indicators.AverageTrueRange(self.data, period=self.p.atr_period)
		self.atr_sma = bt.indicators.SmoothedMovingAverage(self.atr, period=self.p.sma_period)
		self.atr_sma_delta = ((self.atr_sma / self.atr) - 1) * 100

	def next(self):
		self.l.atr_sma_delta[0] = self.atr_sma_delta[0]
		#self.l.atr_sma_delta[0] = 1
