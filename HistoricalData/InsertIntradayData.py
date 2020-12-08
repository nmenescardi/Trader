from Data.HistoricalData import HistoricalData
from Data.Stocks import Stocks
from Data.AlphaVentageJobs import AlphaVentageJobs
from DataFeed.AlphaVantage import AlphaVantage
import sys

class InsertIntradayData:

	def __init__(self, full_data = False):
		self.failed_jobs_dao = AlphaVentageJobs()

		if full_data:
			# Two years of data
			self.amount_years = 1
			self.amount_months = 11
		else:
			# Only last month (it's a slice with the latest 30 days approx. So, a slice may contain data from different months)
			self.amount_years = 1
			self.amount_months = 1


	def __insert_results(self, df, ticker):
		sys.stdout.flush()
		historical_data = HistoricalData()

		for index, row in df.iterrows():
			historical_data.insert_stock_price(
				ticker = ticker,
				time_price = str(index),
				open_price = str(row['open']),
				high_price = str(row['high']),
				low_price = str(row['low']),
				close_price = str(row['close']),
				volume = str(row['volume']),
				timeframe = '5m', #TODO: handle different timeframes
			)
			#print(index, row['open'], row['high'], row['low'], row['close'], row['volume'])


	def run(self):
		job = self.failed_jobs_dao.get_single_job()

		if job is None:
			return False # Already reached the last failed job enqueued

		df = AlphaVantage().get_data(
			ticker = job['ticker'], 
			month = job['data_month'], 
			year = job['data_year']
		)

		if df is None:
			self.failed_jobs_dao.mark_as_failed(
				job_id = job['job_id']
			)
		
		else:
			self.__insert_results(df, job['ticker'])
			self.failed_jobs_dao.mark_as_finished(
				job_id = job['job_id']
			)

		return True


	def add_jobs(self):
		for ticker in Stocks().get_focus(): #Stocks().get_all():

			for year in range(1, self.amount_years + 1):
				for month in range(1, self.amount_months + 1):

					self.failed_jobs_dao.insert_job(
						ticker = ticker, 
						data_month = month, 
						data_year = year
					)
