import yfinance as yf

class YFinanceFeed:

	def get(self, symbol, period="2d", interval="5m"):
		return yf.Ticker(symbol).history(period=period, interval=interval, debug=False)
