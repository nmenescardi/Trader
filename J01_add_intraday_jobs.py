from HistoricalData.InsertIntradayData import InsertIntradayData

intraday = InsertIntradayData(full_data = False)
intraday.add_jobs()

#***  1 - Add a month (full_data = False). 
# Each weekend? --> https://crontab.guru/#0_15_*_*_6
# If needed to insert all (2 years -> 12 months) > (full_data = True)
