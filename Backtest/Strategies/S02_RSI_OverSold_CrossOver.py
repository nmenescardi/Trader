import backtrader as bt
from .S00_Abstract_Strategy import Abstract_Strategy

class RSI_OverSold_CrossOver(Abstract_Strategy):
	params = (
		('rsi_length', 14),
		('rsi_buy_limit', 30),
		('take_profit', 5),
	)

	def __init__(self):
		super().__init__()

		# Indicators
		self.rsi_crossup = bt.ind.CrossUp(bt.indicators.RSI_Safe(period=self.p.rsi_length), self.p.rsi_sell_limit)


	def next(self):
		self.log('Close, %.2f' % self.ltf_dataclose[0])
  
		self.log('Position {}'.format(self.position.size))

		if self.order:
			return

		if self.rsi_crossup == 1:
			if not self.position.size: # Only one order at a time

				self.log('BUY CREATE, %.2f' % self.ltf_dataclose[0])

				tp_percentage = self.p.take_profit / 100 + 1
				take_profit = self.ltf_dataclose[0] * tp_percentage

				self.order = self.buy(
					price=self.ltf_dataclose[0], 
					exectype=bt.Order.Limit, 
					transmit=False,
				)
				self.tp_order = self.sell(price=take_profit, exectype=bt.Order.Limit,
						transmit=True, parent=self.order)

	
	def getParamsForResult(self):
		return {
			'RSI Length' : [self.params.rsi_length],
			'RSI Buy Limit' : [self.params.rsi_buy_limit],
			'Take Profit' : [self.params.take_profit],
		}
