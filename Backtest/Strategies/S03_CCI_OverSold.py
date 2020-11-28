import backtrader as bt
from .S00_Abstract_Strategy import Abstract_Strategy

class CCI_OverSold(Abstract_Strategy):
	params = (
		('cci_length', 14),
		('cci_buy_limit', 30),
		('take_profit', 5),
		('cci_sell_limit', 70),
	)

	def __init__(self):
		super().__init__()

		# Indicators
		self.cci = bt.indicators.CommodityChannelIndex(self.datas[0], period=self.params.cci_length)

	def next(self):
		self.log('Close, %.2f' % self.ltf_dataclose[0])
  
		self.log('Position {}'.format(self.position.size))

		if self.order:
			return

		if self.cci < self.params.cci_buy_limit: # cci check
			if not self.position.size: # Only one order at a time

				self.log('BUY CREATE, %.2f' % self.ltf_dataclose[0])

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
		return {
			'cci Length' : [self.params.cci_length],
			'cci Buy Limit' : [self.params.cci_buy_limit],
			'Take Profit' : [self.params.take_profit],
		}
