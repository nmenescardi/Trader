import backtrader as bt
from .S00_Abstract_Strategy import Abstract_Strategy

class RSI_OverSold(Abstract_Strategy):
	params = (
		('rsi_length', 14),
		('rsi_buy_limit', 30),
		('take_profit', 5),
	)

	def __init__(self):
		super().__init__()

		# Indicators
		self.rsi = bt.indicators.RSI_Safe(self.datas[0], period=self.params.rsi_length)


	def next(self):
		self.log('Close, %.2f' % self.ltf_dataclose[0])
  
		self.log('Position {}'.format(self.position.size))

		if self.order:
			return

		if self.rsi < self.params.rsi_buy_limit: # RSI check
			if not self.position.size: # Only one order at a time

				self.log('Buy order created. Price {}. Datetime: {}.'.format(self.ltf_dataclose[0], self.datetime.datetime()))

				tp_percentage = self.params.take_profit / 100 + 1
				take_profit = self.ltf_dataclose[0] * tp_percentage

				self.order = self.buy(
					price=self.ltf_dataclose[0], 
					exectype=bt.Order.Limit, 
					transmit=False,
				)
				self.tp_order = self.sell(price=take_profit, exectype=bt.Order.Limit,
						transmit=True, parent=self.order)

	
	def getParamsForResult(self):
		params =  {
			'RSI Length' : [self.params.rsi_length],
			'RSI Buy Limit' : [self.params.rsi_buy_limit],
			'Take Profit' : [self.params.take_profit],
		}
		self.logger.info('0029 - Param combination: {}'.format(params))
		return params
