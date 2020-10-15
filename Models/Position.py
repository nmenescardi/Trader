class Position:

	def __init__(self, ticker, amount=50, stopLoss=-2, takeProfit=0.5, isBuyingPosition=True):
		self.ticker = ticker
		self.amount = amount
		self.stopLoss = stopLoss
		self.takeProfit = takeProfit
		self.isBuyingPosition = isBuyingPosition