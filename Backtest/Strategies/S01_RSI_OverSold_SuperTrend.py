import backtrader as bt
from .S00_Abstract_Strategy import Abstract_Strategy
from ..CustomIndicators.SuperTrend import SuperTrend

class RSI_OverSold_SuperTrend(Abstract_Strategy):
	params = (
		('rsi_length', 14),
		('rsi_buy_limit', 30),
		('take_profit', 5),
		('supertrend_multiplier', 3),
		('supertrend_period', 7),
	)


	def __init__(self):
		super().__init__()

		# idem for High TimeFrame (eg 1 day)
		self.htf_dataclose = self.datas[1].close

		# Indicators
		self.rsi = bt.indicators.RSI_Safe(self.datas[0], period=self.params.rsi_length)
  
		self.htf_supertrend = SuperTrend(self.datas[1], period=self.p.supertrend_period, multiplier=self.p.supertrend_multiplier)
		#self.crossover = bt.ind.CrossOver(self.ltf_dataclose, self.htf_sma)


	def next(self):
		self.log('Close, %.2f' % self.ltf_dataclose[0])
  
		self.log('Close HTF, %.2f' % self.htf_dataclose[0])
		
		self.log('SuperTrend {}'.format(self.htf_supertrend[0]))
  
		self.log('Position {}'.format(self.position.size))

		if self.order:
			return

		if self.ltf_dataclose[0] > self.htf_supertrend[0]: # Price above trend
			if self.rsi < self.params.rsi_buy_limit: # RSI check
				if not self.position.size: # Only one order at a time

					self.log('BUY CREATE, %.2f' % self.ltf_dataclose[0])

					tp_percentage = self.params.take_profit / 100 + 1
					take_profit = self.ltf_dataclose[0] * tp_percentage
					sl_percentage = tp_percentage / 3
					stop_loss = self.ltf_dataclose[0] * (1 - sl_percentage / 100)

					self.order = self.buy(
						price=self.ltf_dataclose[0], 
						exectype=bt.Order.Limit, 
						transmit=False,
					)
					self.tp_order = self.sell(price=take_profit, exectype=bt.Order.Limit,
							transmit=True, parent=self.order)
		elif self.position.size > 0:
			self.log('LTF Close {} below Supertrend {}. Closing position.'.format(self.ltf_dataclose[0], self.htf_supertrend[0]))
			self.sell(size = self.position.size)
			self.broker.cancel(self.tp_order)

	
	def getParamsForResult(self):
		return {
			'RSI Length' : [self.params.rsi_length],
			'RSI Buy Limit' : [self.params.rsi_buy_limit],
			'Take Profit' : [self.params.take_profit],
			'SuperTrend Period' : [self.params.supertrend_period],
			'SuperTrend Multiplier' : [self.params.supertrend_multiplier],
		}
