class Position:

	def __init__(self, ticker, amount=100, stopLoss=-10, takeProfit=1, isBuyingPosition=True):
		self.ticker = ticker.lower()
		self.amount = amount
		self.stopLoss = stopLoss
		self.takeProfit = takeProfit
		self.isBuyingPosition = isBuyingPosition


	def print_params(self):
		print(vars(self))
