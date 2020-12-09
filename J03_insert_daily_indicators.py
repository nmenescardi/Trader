from HistoricalData.InsertDailyIndicators import InsertDailyIndicators
from Helpers.Market import Market  

if not Market().is_market_open():
	InsertDailyIndicators().run()
	
# Daily Indicator. After market closed? -> https://crontab.guru/#0_16_*_*_1-5
