from HistoricalData.InsertIntradayData import InsertIntradayData

intraday = InsertIntradayData(full_data = False)
intraday.add_jobs()

#***  1 - Add two months (full_data = False). 
# Each month --> https://crontab.guru/#0_6_1_*_*
# If needed to insert all (2 years -> 12 months) > (full_data = True)