import time, pandas as pd
from .yFinanceDataProvider import yFinanceDataProvider 
from .Strategy import Strategy

class Manager:

	def __init__(self, queuesHandler):
		self.strategy = Strategy(
			queuesHandler = queuesHandler, 
			dataProvider = yFinanceDataProvider()
		)
		self.minutesToWait = 0.5
		self.tickerList = ['GME','NIO','ZM','BYD','PTON','LAD','GNRC','CVNA','GPI','MDB','VEEV','INSP','NWPX','PKI','CROX','MRTX','PODD','DAR','MTH','PENN','FIVN','DRI','HBI','Z','LEN','COUP','SNAP','LOW','VCYT','BBBY','TWLO','DKS','FBHS','NUAN','POOL','FRPT','NKE','DOCU','RS','TOL','HD','FDX','FCX','TGT','RGEN','GGB','LULU','ZEN','DPZ','MSCI','STMP','PG','IDXX','PAYC','TREX','MELI','ANSS','NOW','SE','W','CZR','STNE','CHTR','ETSY','DHI','FAST','ZTS','CRL','ZNGA','IRTC','OMI','MTCH','SQ','RUN','AMD','NXPI','AAPL','RH','TMO','DHR','NVCR','BABA','ENPH','UPS','BLDR','MRVL','GPS','NVDA','NIU','PDD','PINS','PYPL','HUBS','SHOP','WIX','DELL','IBP','POWI','CTAS','AMZN','JD','PANW','SGEN','DAL','NVTA','ADBE','BYND','SNOW','EXAS','CRM','SEDG','ROKU','FVRR','CRWD','MRNA','SPWR','TWTR','TSLA','SAIL','TQQQ','CSIQ','TTD','INFY','FSLY']


	def run(self):		
		while(True):
			for ticker in self.tickerList:
				self.strategy.perform(ticker)
				time.sleep(5)

			#time.sleep(60 * self.minutesToWait)
