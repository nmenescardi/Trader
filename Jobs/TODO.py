#TODO: Cron jobs for VPS

#***  1 - Add two months (full_data = False). Each month? ***
""" intraday = InsertIntradayData(full_data = False)
intraday.add_jobs() """
# If needed to insert all (2 years -> 12 months) > (full_data = True)


#***  2 - Download and insert intraday data. Once per day after market is closed + 2 hours? ***
""" intraday = InsertIntradayData()

i = 0
alphaventage_limit_per_day = 450
while True:
	i+=1
	is_there_more = intraday.run()

	if not is_there_more or i == alphaventage_limit_per_day:
		break """


#***  3 - Daily Indicator. After market closed? ***
""" InsertDailyIndicators().run() """


#***  4 - Backtest stocks. Once per month? ***
#TODO: Focus or all above 200SMA?
#TODO: decide about how to handle results



#***  5 -  etoro update positions 30 mins before market opens?