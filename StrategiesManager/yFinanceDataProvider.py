import yfinance as yf

class yFinanceDataProvider:

	def get(self, symbol, period="1d", interval="5m"):
		return yf.Ticker(symbol).history(period=period, interval=interval, debug=False)
