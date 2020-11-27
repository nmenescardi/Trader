from dateutil import tz
from datetime import datetime, time
import holidays

class Market:
	def __init__(self):
		self.nyc_tz = tz.gettz('America/New_York')

		self.us_holidays = holidays.US()
		self.start = time(9, 30)
		self.end = time(16, 0)


	def get_market_time(self):
		return datetime.now(tz=self.nyc_tz)

	
	def is_market_open(self):
		#TODO: check for weekends and holidays
		market_time = self.get_market_time()
		
		# Check for weekends
		if market_time.date().weekday() > 4:
			return False

		# If a holiday
		if market_time.strftime('%Y-%m-%d') in self.us_holidays:
			return False

		is_market_open = self.start < market_time.time() < self.end
		return is_market_open
