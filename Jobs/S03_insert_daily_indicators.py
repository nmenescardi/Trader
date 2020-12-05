from HistoricalData.InsertDailyIndicators import InsertDailyIndicators
from Helpers.Market import Market  

if (Market().is_market_open()):
	# Daily Indicator. After market closed? ***
	InsertDailyIndicators().run()
