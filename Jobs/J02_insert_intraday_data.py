from HistoricalData.InsertIntradayData import InsertIntradayData

intraday = InsertIntradayData()

i = 0
alphaventage_limit_per_day = 450
while True:
	i+=1
	is_there_more = intraday.run()

	if not is_there_more or i == alphaventage_limit_per_day:
		break

# Download and insert intraday data. 
# Once per day after market is closed + 2 hours -> https://crontab.guru/#0_18_*_*_1-5