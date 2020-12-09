class StrategiesSetup():

	RSI_OverSold = 'RSI_OverSold'
	
	config = {

		# Defaults: 'ltf_interval' : "5m", 'rsi_period' : 5
		RSI_OverSold : [
			{'ticker': 'AAPL', 'rsi_period' : 14, 'rsi_limit': 30, 'tp_percentage': 1 },
			{'ticker': 'ADBE', 'rsi_period' : 5, 'rsi_limit': 10, 'tp_percentage': 1 },
			{'ticker': 'AMD', 'rsi_period' : 5, 'rsi_limit': 5, 'tp_percentage': 2 },
			{'ticker': 'AMZN', 'rsi_period' : 5, 'rsi_limit': 20, 'tp_percentage': 1 },
			{'ticker': 'ANSS', 'rsi_period' : 14, 'rsi_limit': 10, 'tp_percentage': 1 },
			{'ticker': 'BABA', 'rsi_period' : 14, 'rsi_limit': 15, 'tp_percentage': 1 },
			{'ticker': 'BBBY', 'rsi_period' : 25, 'rsi_limit': 25, 'tp_percentage': 1 },
			{'ticker': 'BYD', 'rsi_period' : 5, 'rsi_limit': 20, 'tp_percentage': 1 },
			{'ticker': 'BYND', 'rsi_period' : 5, 'rsi_limit': 10, 'tp_percentage': 2 },
			{'ticker': 'CHTR', 'rsi_period' : 14, 'rsi_limit': 25, 'tp_percentage': 1 },
			{'ticker': 'CHWY', 'rsi_period' : 25, 'rsi_limit': 30, 'tp_percentage': 1 },
			{'ticker': 'COUP', 'rsi_period' : 14, 'rsi_limit': 30, 'tp_percentage': 3 },
			{'ticker': 'CRM', 'rsi_period' : 5, 'rsi_limit': 25, 'tp_percentage': 1 },
			{'ticker': 'CROX', 'rsi_period' : 5, 'rsi_limit': 20, 'tp_percentage': 2 },
			{'ticker': 'CRWD', 'rsi_period' : 9, 'rsi_limit': 15, 'tp_percentage': 5 },
			{'ticker': 'CSIQ', 'rsi_period' : 5, 'rsi_limit': 10, 'tp_percentage': 3 },
			{'ticker': 'CVNA', 'rsi_period' : 5, 'rsi_limit': 5, 'tp_percentage': 1 },
			{'ticker': 'CZR', 'rsi_period' : 5, 'rsi_limit': 5, 'tp_percentage': 5 },
			{'ticker': 'DAL', 'rsi_period' : 25, 'rsi_limit': 25, 'tp_percentage': 4 },
			{'ticker': 'DAR', 'rsi_period' : 25, 'rsi_limit': 25, 'tp_percentage': 3 },
			{'ticker': 'DELL', 'rsi_period' : 14, 'rsi_limit': 15, 'tp_percentage': 3 },
			{'ticker': 'DHI', 'rsi_period' : 5, 'rsi_limit': 10, 'tp_percentage': 1 },
			{'ticker': 'DHR', 'rsi_period' : 5, 'rsi_limit': 15, 'tp_percentage': 1 },
			{'ticker': 'DKS', 'rsi_period' : 5, 'rsi_limit': 10, 'tp_percentage': 1 },
			{'ticker': 'DOCU', 'rsi_period' : 9, 'rsi_limit': 30, 'tp_percentage': 2 },
			#{'ticker': 'DOYU', 'rsi_period' : 5, 'rsi_limit': 15, 'tp_percentage': 2 },	
			{'ticker': 'DPZ', 'rsi_period' : 5, 'rsi_limit': 5, 'tp_percentage': 1 },	
			{'ticker': 'DRI', 'rsi_period' : 25, 'rsi_limit': 25, 'tp_percentage': 4 },	
			{'ticker': 'EDU', 'rsi_period' : 5, 'rsi_limit': 10, 'tp_percentage': 3 },	
			{'ticker': 'ENPH', 'rsi_period' : 5, 'rsi_limit': 30, 'tp_percentage': 2 },	
			{'ticker': 'ETSY', 'rsi_period' : 5, 'rsi_limit': 25, 'tp_percentage': 2 },	
			{'ticker': 'FAST', 'rsi_period' : 14, 'rsi_limit': 30, 'tp_percentage': 2 },	
			{'ticker': 'FBHS', 'rsi_period' : 9, 'rsi_limit': 15, 'tp_percentage': 1 },	
			{'ticker': 'FCX', 'rsi_period' : 5, 'rsi_limit': 15, 'tp_percentage': 1 },	
			{'ticker': 'FDX', 'rsi_period' : 9, 'rsi_limit': 10, 'tp_percentage': 1 },	
			{'ticker': 'FRPT', 'rsi_period' : 14, 'rsi_limit': 20, 'tp_percentage': 4 },	
			{'ticker': 'FSLY', 'rsi_period' : 9, 'rsi_limit': 10, 'tp_percentage': 1 },
			{'ticker': 'FVRR', 'rsi_period' : 5, 'rsi_limit': 20, 'tp_percentage': 5 },	
			{'ticker': 'GME', 'rsi_period' : 9, 'rsi_limit': 25, 'tp_percentage': 4 },
			{'ticker': 'GNRC', 'rsi_period' : 5, 'rsi_limit': 10, 'tp_percentage': 2 },	
			{'ticker': 'GPI', 'rsi_period' : 25, 'rsi_limit': 25, 'tp_percentage': 1 },	
			{'ticker': 'GPS', 'rsi_period' : 14, 'rsi_limit': 20, 'tp_percentage': 1 },	
			{'ticker': 'HD', 'rsi_period' : 14, 'rsi_limit': 30, 'tp_percentage': 4 },	
			#{'ticker': 'HUBS', 'rsi_period' : 5, 'rsi_limit': 25, 'tp_percentage': 5 },	
			{'ticker': 'IBP', 'rsi_period' : 5, 'rsi_limit': 15, 'tp_percentage': 1 },	
			{'ticker': 'IDXX', 'rsi_period' : 9, 'rsi_limit': 20, 'tp_percentage': 1 },	
			{'ticker': 'INFY', 'rsi_period' : 5, 'rsi_limit': 30, 'tp_percentage': 1 },	
			{'ticker': 'INSP', 'rsi_period' : 5, 'rsi_limit': 10, 'tp_percentage': 3 },	
			{'ticker': 'IPHI', 'rsi_period' : 5, 'rsi_limit': 15, 'tp_percentage': 2 },	
			{'ticker': 'IRTC', 'rsi_period' : 5, 'rsi_limit': 5, 'tp_percentage': 1 },	
			#{'ticker': 'JD', 'rsi_period' : 9, 'rsi_limit': 30, 'tp_percentage': 5 }, #TODO: Map ticker -> URL
			#{'ticker': 'LAD', 'rsi_period' : 5, 'rsi_limit': 30, 'tp_percentage': 2 },	
			{'ticker': 'LEN', 'rsi_period' : 25, 'rsi_limit': 30, 'tp_percentage': 1 },	
			{'ticker': 'LOW', 'rsi_period' : 5, 'rsi_limit': 25, 'tp_percentage': 1 },	
			{'ticker': 'LULU', 'rsi_period' : 9, 'rsi_limit': 25, 'tp_percentage': 1 },	
			{'ticker': 'MDB', 'rsi_period' : 14, 'rsi_limit': 25, 'tp_percentage': 5 },	
			{'ticker': 'MELI', 'rsi_period' : 9, 'rsi_limit': 30, 'tp_percentage': 3 },	
			{'ticker': 'MRNA', 'rsi_period' : 5, 'rsi_limit': 30, 'tp_percentage': 5 }, # Manual TP	
			{'ticker': 'MRTX', 'rsi_period' : 5, 'rsi_limit': 25, 'tp_percentage': 1 },	
			{'ticker': 'MRVL', 'rsi_period' : 14, 'rsi_limit': 30, 'tp_percentage': 1 },	
			{'ticker': 'MSCI', 'rsi_period' : 14, 'rsi_limit': 15, 'tp_percentage': 2 },	
			{'ticker': 'MTCH', 'rsi_period' : 14, 'rsi_limit': 20, 'tp_percentage': 1 },	
			{'ticker': 'MTH', 'rsi_period' : 5, 'rsi_limit': 25, 'tp_percentage': 2 },	
			{'ticker': 'NIO', 'rsi_period' : 2, 'rsi_limit': 10, 'tp_percentage': 15, 'days_between_orders' : 1, 'max_positions_amount': 5 },	# Manual TP
			{'ticker': 'NIU', 'rsi_period' : 5, 'rsi_limit': 15, 'tp_percentage': 15 },	# Manual TP
			{'ticker': 'NKE', 'rsi_period' : 9, 'rsi_limit': 20, 'tp_percentage': 3 },	
			{'ticker': 'NOW', 'rsi_period' : 14, 'rsi_limit': 25, 'tp_percentage': 1 },	
			{'ticker': 'NUAN', 'rsi_period' : 14, 'rsi_limit': 20, 'tp_percentage': 3 },	
			{'ticker': 'NVCR', 'rsi_period' : 5, 'rsi_limit': 5, 'tp_percentage': 1 },	
			{'ticker': 'NVDA', 'rsi_period' : 5, 'rsi_limit': 20, 'tp_percentage': 1 },	
			{'ticker': 'NXPI', 'rsi_period' : 25, 'rsi_limit': 25, 'tp_percentage': 5 },	
			{'ticker': 'OMI', 'rsi_period' : 14, 'rsi_limit': 30, 'tp_percentage': 2 },	
			{'ticker': 'PAYC', 'rsi_period' : 5, 'rsi_limit': 5, 'tp_percentage': 3 },	
			{'ticker': 'PDD', 'rsi_period' : 5, 'rsi_limit': 10, 'tp_percentage': 2 },	
			{'ticker': 'PG', 'rsi_period' : 25, 'rsi_limit': 25, 'tp_percentage': 1 },	
			{'ticker': 'PINS', 'rsi_period' : 9, 'rsi_limit': 20, 'tp_percentage': 1 },	
			{'ticker': 'PKI', 'rsi_period' : 5, 'rsi_limit': 20, 'tp_percentage': 3 },	
			{'ticker': 'PODD', 'rsi_period' : 14, 'rsi_limit': 30, 'tp_percentage': 1 },	
			{'ticker': 'POOL', 'rsi_period' : 5, 'rsi_limit': 5, 'tp_percentage': 5 },	
			{'ticker': 'POWI', 'rsi_period' : 25, 'rsi_limit': 25, 'tp_percentage': 1 },	
			{'ticker': 'PTON', 'rsi_period' : 5, 'rsi_limit': 20, 'tp_percentage': 3 },	
			{'ticker': 'PYPL', 'rsi_period' : 9, 'rsi_limit': 20, 'tp_percentage': 5 },	
			#{'ticker': 'RGEN', 'rsi_period' : 5, 'rsi_limit': 25, 'tp_percentage': 1 },	
			{'ticker': 'RH', 'rsi_period' : 5, 'rsi_limit': 5, 'tp_percentage': 1 },	
			{'ticker': 'ROKU', 'rsi_period' : 5, 'rsi_limit': 15, 'tp_percentage': 1 },	
			{'ticker': 'RS', 'rsi_period' : 9, 'rsi_limit': 15, 'tp_percentage': 2 },	
			{'ticker': 'SAIL', 'rsi_period' : 5, 'rsi_limit': 20, 'tp_percentage': 3 },	
			{'ticker': 'SE', 'rsi_period' : 5, 'rsi_limit': 25, 'tp_percentage': 3 },	
			{'ticker': 'SGEN', 'rsi_period' : 5, 'rsi_limit': 20, 'tp_percentage': 1 },	
			{'ticker': 'SHOP', 'rsi_period' : 5, 'rsi_limit': 25, 'tp_percentage': 5 },	
			{'ticker': 'SNAP', 'rsi_period' : 5, 'rsi_limit': 10, 'tp_percentage': 1 },	
			{'ticker': 'SNOW', 'rsi_period' : 14, 'rsi_limit': 25, 'tp_percentage': 1 },	# Manual TP
			{'ticker': 'SPWR', 'rsi_period' : 5, 'rsi_limit': 15, 'tp_percentage': 5 },	
			{'ticker': 'SQ', 'rsi_period' : 5, 'rsi_limit': 25, 'tp_percentage': 1, 'days_between_orders' : 1 },	
			{'ticker': 'STMP', 'rsi_period' : 5, 'rsi_limit': 5, 'tp_percentage': 1 },	
			{'ticker': 'STNE', 'rsi_period' : 5, 'rsi_limit': 15, 'tp_percentage': 1 },	
			{'ticker': 'TGT', 'rsi_period' : 14, 'rsi_limit': 20, 'tp_percentage': 2 },	
			{'ticker': 'TMO', 'rsi_period' : 5, 'rsi_limit': 10, 'tp_percentage': 2 },	
			{'ticker': 'TOL', 'rsi_period' : 5, 'rsi_limit': 15, 'tp_percentage': 5 },	
			{'ticker': 'TREX', 'rsi_period' : 9, 'rsi_limit': 25, 'tp_percentage': 3 },	
			{'ticker': 'TSLA', 'rsi_period' : 14, 'rsi_limit': 25, 'tp_percentage': 1 },	
			{'ticker': 'TTD', 'rsi_period' : 5, 'rsi_limit': 5, 'tp_percentage': 1 },	
			{'ticker': 'TWLO', 'rsi_period' : 25, 'rsi_limit': 25, 'tp_percentage': 1 },	
			{'ticker': 'TWTR', 'rsi_period' : 5, 'rsi_limit': 15, 'tp_percentage': 3 },	# Winner
			{'ticker': 'TWTR', 'rsi_period' : 5, 'rsi_limit': 5, 'tp_percentage': 1 },	# Efficient
			{'ticker': 'UPS', 'rsi_period' : 9, 'rsi_limit': 15, 'tp_percentage': 1 },	
			{'ticker': 'VEEV', 'rsi_period' : 9, 'rsi_limit': 30, 'tp_percentage': 1 },	
			{'ticker': 'W', 'rsi_period' : 9, 'rsi_limit': 30, 'tp_percentage': 1 },	
			{'ticker': 'WIX', 'rsi_period' : 14, 'rsi_limit': 20, 'tp_percentage': 4 },	
			{'ticker': 'Z', 'rsi_period' : 5, 'rsi_limit': 10, 'tp_percentage': 3 },	
			{'ticker': 'ZEN', 'rsi_period' : 9, 'rsi_limit': 15, 'tp_percentage': 4 },	
			{'ticker': 'ZM', 'rsi_period' : 25, 'rsi_limit': 25, 'tp_percentage': 1 },	
			{'ticker': 'ZNGA', 'rsi_period' : 14, 'rsi_limit': 20, 'tp_percentage': 1 },	
			{'ticker': 'ZTS', 'rsi_period' : 9, 'rsi_limit': 15, 'tp_percentage': 1 },
   
			# Focus 2
			{'ticker': 'ABBV', 'rsi_period' : 25, 'rsi_limit': 25, 'tp_percentage': 1 },	
			{'ticker': 'ABC', 'rsi_period' : 9, 'rsi_limit': 15, 'tp_percentage': 2 },	
			{'ticker': 'ABCB', 'rsi_period' : 5, 'rsi_limit': 5, 'tp_percentage': 1 },	
			{'ticker': 'ABG', 'rsi_period' : 25, 'rsi_limit': 25, 'tp_percentage': 1 },	
			{'ticker': 'ABT', 'rsi_period' : 14, 'rsi_limit': 20, 'tp_percentage': 3 },
			{'ticker': 'ACM', 'rsi_period' : 5, 'rsi_limit': 30, 'tp_percentage': 1 },	
			{'ticker': 'ACN', 'rsi_period' : 9, 'rsi_limit': 15, 'tp_percentage': 1 },	
			{'ticker': 'ADI', 'rsi_period' : 25, 'rsi_limit': 25, 'tp_percentage': 3 },	
			{'ticker': 'ADP', 'rsi_period' : 9, 'rsi_limit': 20, 'tp_percentage': 1 },	
			{'ticker': 'ADSK', 'rsi_period' : 25, 'rsi_limit': 20, 'tp_percentage': 1 },	
			{'ticker': 'AFL', 'rsi_period' : 5, 'rsi_limit': 5, 'tp_percentage': 2 },	
			{'ticker': 'AGCO', 'rsi_period' : 14, 'rsi_limit': 15, 'tp_percentage': 1 },	
			{'ticker': 'AIZ', 'rsi_period' : 14, 'rsi_limit': 25, 'tp_percentage': 1 },	
			{'ticker': 'AJG', 'rsi_period' : 14, 'rsi_limit': 30, 'tp_percentage': 1 },	
			{'ticker': 'AME', 'rsi_period' : 9, 'rsi_limit': 15, 'tp_percentage': 2 },	
			{'ticker': 'ANTM', 'rsi_period' : 14, 'rsi_limit': 15, 'tp_percentage': 1 },	
			{'ticker': 'APH', 'rsi_period' : 9, 'rsi_limit': 15, 'tp_percentage': 4 },	
			{'ticker': 'ASML', 'rsi_period' : 14, 'rsi_limit': 25, 'tp_percentage': 1 },	
			{'ticker': 'BKNG', 'rsi_period' : 5, 'rsi_limit': 10, 'tp_percentage': 1 },	
			{'ticker': 'CNMD', 'rsi_period' : 5, 'rsi_limit': 10, 'tp_percentage': 1 },	
			{'ticker': 'DENN', 'rsi_period' : 9, 'rsi_limit': 15, 'tp_percentage': 1 },	
			{'ticker': 'DKNG', 'rsi_period' : 14, 'rsi_limit': 25, 'tp_percentage': 1 }, # manual TP	
			{'ticker': 'EEFT', 'rsi_period' : 25, 'rsi_limit': 25, 'tp_percentage': 1 },	
			#{'ticker': 'EV', 'rsi_period' : 5, 'rsi_limit': 30, 'tp_percentage': 2 },	
			{'ticker': 'EXPE', 'rsi_period' : 25, 'rsi_limit': 25, 'tp_percentage': 1 },	
			{'ticker': 'FIVE', 'rsi_period' : 14, 'rsi_limit': 20, 'tp_percentage': 1 },	
			{'ticker': 'GWPH', 'rsi_period' : 9, 'rsi_limit': 20, 'tp_percentage': 1 },	
			{'ticker': 'HDS', 'rsi_period' : 25, 'rsi_limit': 25, 'tp_percentage': 3 },	
			{'ticker': 'KTOS', 'rsi_period' : 9, 'rsi_limit': 25, 'tp_percentage': 1 },	
			{'ticker': 'LPSN', 'rsi_period' : 5, 'rsi_limit': 30, 'tp_percentage': 1 },	
			{'ticker': 'LYFT', 'rsi_period' : 5, 'rsi_limit': 5, 'tp_percentage': 3 },	
			{'ticker': 'LYV', 'rsi_period' : 9, 'rsi_limit': 20, 'tp_percentage': 2 },	
			{'ticker': 'MU', 'rsi_period' : 14, 'rsi_limit': 15, 'tp_percentage': 1 },	
			{'ticker': 'NET', 'rsi_period' : 14, 'rsi_limit': 20, 'tp_percentage': 1 },	
			{'ticker': 'NTLA', 'rsi_period' : 14, 'rsi_limit': 30, 'tp_percentage': 1 },	
			#{'ticker': 'PANW', 'rsi_period' : 5, 'rsi_limit': 25, 'tp_percentage': 4 },	
			{'ticker': 'PFGC', 'rsi_period' : 14, 'rsi_limit': 15, 'tp_percentage': 2 },	
			{'ticker': 'PI', 'rsi_period' : 5, 'rsi_limit': 20, 'tp_percentage': 1 },	
			{'ticker': 'PLAY', 'rsi_period' : 25, 'rsi_limit': 25, 'tp_percentage': 1 },	
			{'ticker': 'PLTR', 'rsi_period' : 14, 'rsi_limit': 30, 'tp_percentage': 1 }, # manual TP	
			{'ticker': 'QCOM', 'rsi_period' : 9, 'rsi_limit': 20, 'tp_percentage': 1 },	
			{'ticker': 'QRVO', 'rsi_period' : 14, 'rsi_limit': 30, 'tp_percentage': 1 },	
			{'ticker': 'RGA', 'rsi_period' : 14, 'rsi_limit': 15, 'tp_percentage': 1 },	
			{'ticker': 'ROST', 'rsi_period' : 14, 'rsi_limit': 20, 'tp_percentage': 1 },	
			{'ticker': 'SPOT', 'rsi_period' : 14, 'rsi_limit': 15, 'tp_percentage': 1 },	
			{'ticker': 'SPR', 'rsi_period' : 14, 'rsi_limit': 15, 'tp_percentage': 1 },	
			{'ticker': 'SYY', 'rsi_period' : 25, 'rsi_limit': 20, 'tp_percentage': 1 },	
			{'ticker': 'TA', 'rsi_period' : 14, 'rsi_limit': 20, 'tp_percentage': 1 },	
			{'ticker': 'TDOC', 'rsi_period' : 5, 'rsi_limit': 5, 'tp_percentage': 1 },	
			{'ticker': 'TEAM', 'rsi_period' : 14, 'rsi_limit': 20, 'tp_percentage': 5 },	
			{'ticker': 'TECH', 'rsi_period' : 14, 'rsi_limit': 20, 'tp_percentage': 1 },	
			{'ticker': 'TRMB', 'rsi_period' : 5, 'rsi_limit': 5, 'tp_percentage': 1 },	
			{'ticker': 'UAL', 'rsi_period' : 14, 'rsi_limit': 15, 'tp_percentage': 1 },	
			{'ticker': 'UBER', 'rsi_period' : 9, 'rsi_limit': 20, 'tp_percentage': 5 },	
			{'ticker': 'UI', 'rsi_period' : 14, 'rsi_limit': 30, 'tp_percentage': 1 },	
			{'ticker': 'ULTA', 'rsi_period' : 25, 'rsi_limit': 25, 'tp_percentage': 1 },	
			{'ticker': 'USFD', 'rsi_period' : 5, 'rsi_limit': 10, 'tp_percentage': 2 },	
			{'ticker': 'AVGO', 'rsi_period' : 5, 'rsi_limit': 10, 'tp_percentage': 1 },	
			{'ticker': 'AWK', 'rsi_period' : 14, 'rsi_limit': 15, 'tp_percentage': 1 },	
			{'ticker': 'BBY', 'rsi_period' : 25, 'rsi_limit': 20, 'tp_percentage': 1 },	
			{'ticker': 'BFAM', 'rsi_period' : 14, 'rsi_limit': 15, 'tp_percentage': 2 },	
			{'ticker': 'BHVN', 'rsi_period' : 14, 'rsi_limit': 15, 'tp_percentage': 3 },	
			{'ticker': 'BILI', 'rsi_period' : 9, 'rsi_limit': 10, 'tp_percentage': 3 },	
			{'ticker': 'BIO', 'rsi_period' : 14, 'rsi_limit': 15, 'tp_percentage': 2 },	
			{'ticker': 'BLDR', 'rsi_period' : 5, 'rsi_limit': 30, 'tp_percentage': 2 },	
			{'ticker': 'BRO', 'rsi_period' : 5, 'rsi_limit': 15, 'tp_percentage': 1 },	
			{'ticker': 'CDW', 'rsi_period' : 5, 'rsi_limit': 15, 'tp_percentage': 1 },	
			{'ticker': 'CHDN', 'rsi_period' : 9, 'rsi_limit': 10, 'tp_percentage': 1 },	
			{'ticker': 'COST', 'rsi_period' : 14, 'rsi_limit': 15, 'tp_percentage': 1 },	
			{'ticker': 'CPRT', 'rsi_period' : 5, 'rsi_limit': 20, 'tp_percentage': 1 },	
			{'ticker': 'CRL', 'rsi_period' : 5, 'rsi_limit': 5, 'tp_percentage': 1 },	
			{'ticker': 'CSGP', 'rsi_period' : 14, 'rsi_limit': 15, 'tp_percentage': 1 },	
			{'ticker': 'CTAS', 'rsi_period' : 14, 'rsi_limit': 20, 'tp_percentage': 1 },	
			{'ticker': 'CTLT', 'rsi_period' : 14, 'rsi_limit': 20, 'tp_percentage': 1 },	
			{'ticker': 'DE', 'rsi_period' : 14, 'rsi_limit': 15, 'tp_percentage': 1 },	
			{'ticker': 'DIS', 'rsi_period' : 5, 'rsi_limit': 15, 'tp_percentage': 1 },	
			{'ticker': 'DLTR', 'rsi_period' : 14, 'rsi_limit': 20, 'tp_percentage': 1 },	
			{'ticker': 'DNKN', 'rsi_period' : 5, 'rsi_limit': 15, 'tp_percentage': 1 },	
			{'ticker': 'DOV', 'rsi_period' : 14, 'rsi_limit': 15, 'tp_percentage': 1 },	
			{'ticker': 'DRE', 'rsi_period' : 14, 'rsi_limit': 15, 'tp_percentage': 1 },	
			{'ticker': 'DTE', 'rsi_period' : 5, 'rsi_limit': 5, 'tp_percentage': 1 },	
			{'ticker': 'EL', 'rsi_period' : 14, 'rsi_limit': 20, 'tp_percentage': 5 },	
			{'ticker': 'EVA', 'rsi_period' : 5, 'rsi_limit': 15, 'tp_percentage': 1 },	
			{'ticker': 'FTCH', 'rsi_period' : 14, 'rsi_limit': 15, 'tp_percentage': 1 },	
			{'ticker': 'GL', 'rsi_period' : 14, 'rsi_limit': 15, 'tp_percentage': 1 },	
			{'ticker': 'GOOG', 'rsi_period' : 9, 'rsi_limit': 20, 'tp_percentage': 2 },	
			{'ticker': 'GRMN', 'rsi_period' : 5, 'rsi_limit': 5, 'tp_percentage': 1 },	
			{'ticker': 'HOLX', 'rsi_period' : 5, 'rsi_limit': 20, 'tp_percentage': 3 },	
			{'ticker': 'HON', 'rsi_period' : 5, 'rsi_limit': 5, 'tp_percentage': 1 },	
			{'ticker': 'HUBS', 'rsi_period' : 14, 'rsi_limit': 25, 'tp_percentage': 1 },	
			{'ticker': 'IDXX', 'rsi_period' : 5, 'rsi_limit': 10, 'tp_percentage': 3 }, # Duplicated to test	
			{'ticker': 'IEX', 'rsi_period' : 14, 'rsi_limit': 20, 'tp_percentage': 1 },	
			{'ticker': 'INFO', 'rsi_period' : 25, 'rsi_limit': 25, 'tp_percentage': 1 },	
			{'ticker': 'INTU', 'rsi_period' : 5, 'rsi_limit': 25, 'tp_percentage': 4 },	
			{'ticker': 'IQV', 'rsi_period' : 9, 'rsi_limit': 10, 'tp_percentage': 1 },	
			{'ticker': 'KEYS', 'rsi_period' : 5, 'rsi_limit': 5, 'tp_percentage': 3 },	
			{'ticker': 'KLAC', 'rsi_period' : 14, 'rsi_limit': 15, 'tp_percentage': 1 },	
			{'ticker': 'LII', 'rsi_period' : 25, 'rsi_limit': 25, 'tp_percentage': 1 },	
			{'ticker': 'MASI', 'rsi_period' : 25, 'rsi_limit': 20, 'tp_percentage': 2 },	
			{'ticker': 'MCHP', 'rsi_period' : 25, 'rsi_limit': 30, 'tp_percentage': 3 },	
			{'ticker': 'MDT', 'rsi_period' : 14, 'rsi_limit': 20, 'tp_percentage': 2 },	
			{'ticker': 'MNST', 'rsi_period' : 9, 'rsi_limit': 25, 'tp_percentage': 3 },	
			{'ticker': 'MOH', 'rsi_period' : 14, 'rsi_limit': 25, 'tp_percentage': 1 },	
			{'ticker': 'MSFT', 'rsi_period' : 5, 'rsi_limit': 15, 'tp_percentage': 1 },	
			{'ticker': 'MSI', 'rsi_period' : 5, 'rsi_limit': 15, 'tp_percentage': 2 },	
			{'ticker': 'MTD', 'rsi_period' : 5, 'rsi_limit': 15, 'tp_percentage': 1 },	
			{'ticker': 'MXIM', 'rsi_period' : 5, 'rsi_limit': 5, 'tp_percentage': 1 },	
			{'ticker': 'NEE', 'rsi_period' : 5, 'rsi_limit': 5, 'tp_percentage': 1 },	
			{'ticker': 'NSC', 'rsi_period' : 25, 'rsi_limit': 30, 'tp_percentage': 1 },	
			{'ticker': 'NTRA', 'rsi_period' : 5, 'rsi_limit': 15, 'tp_percentage': 2 },	
			{'ticker': 'ODFL', 'rsi_period' : 25, 'rsi_limit': 25, 'tp_percentage': 1 },	
			{'ticker': 'OKTA', 'rsi_period' : 14, 'rsi_limit': 15, 'tp_percentage': 1 },	
			{'ticker': 'PAYX', 'rsi_period' : 9, 'rsi_limit': 15, 'tp_percentage': 1 },	
			{'ticker': 'PEN', 'rsi_period' : 5, 'rsi_limit': 5, 'tp_percentage': 2 },	
			{'ticker': 'PEP', 'rsi_period' : 14, 'rsi_limit': 20, 'tp_percentage': 1 },	
			{'ticker': 'PLD', 'rsi_period' : 25, 'rsi_limit': 25, 'tp_percentage': 2 },	
			{'ticker': 'PWR', 'rsi_period' : 5, 'rsi_limit': 5, 'tp_percentage': 1 },	
			{'ticker': 'QTWO', 'rsi_period' : 5, 'rsi_limit': 25, 'tp_percentage': 1 },	
			{'ticker': 'RACE', 'rsi_period' : 9, 'rsi_limit': 10, 'tp_percentage': 3 },	
			{'ticker': 'RSG', 'rsi_period' : 5, 'rsi_limit': 15, 'tp_percentage': 4 },	
			{'ticker': 'SHAK', 'rsi_period' : 25, 'rsi_limit': 25, 'tp_percentage': 1 },	
			{'ticker': 'SHW', 'rsi_period' : 9, 'rsi_limit': 25, 'tp_percentage': 1 },	
			{'ticker': 'SNE', 'rsi_period' : 14, 'rsi_limit': 25, 'tp_percentage': 1 },	
			{'ticker': 'STE', 'rsi_period' : 25, 'rsi_limit': 25, 'tp_percentage': 1 },	
			{'ticker': 'SYK', 'rsi_period' : 14, 'rsi_limit': 20, 'tp_percentage': 1 },	
			{'ticker': 'TDG', 'rsi_period' : 14, 'rsi_limit': 20, 'tp_percentage': 2 },	
			{'ticker': 'TMUS', 'rsi_period' : 5, 'rsi_limit': 10, 'tp_percentage': 2 },	
			{'ticker': 'TRU', 'rsi_period' : 14, 'rsi_limit': 30, 'tp_percentage': 1 },	
			{'ticker': 'TT', 'rsi_period' : 5, 'rsi_limit': 10, 'tp_percentage': 2 },	
			{'ticker': 'TXN', 'rsi_period' : 25, 'rsi_limit': 25, 'tp_percentage': 1 },	
			{'ticker': 'UNH', 'rsi_period' : 9, 'rsi_limit': 10, 'tp_percentage': 1 },	
			{'ticker': 'VCYT', 'rsi_period' : 9, 'rsi_limit': 10, 'tp_percentage': 2 },	
			{'ticker': 'VRSK', 'rsi_period' : 25, 'rsi_limit': 25, 'tp_percentage': 1 },	
			{'ticker': 'WMT', 'rsi_period' : 25, 'rsi_limit': 25, 'tp_percentage': 2 },	
		]
	}

