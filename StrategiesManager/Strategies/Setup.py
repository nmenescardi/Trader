class StrategiesSetup():

	RSI_OverSold = 'RSI_OverSold'
	
	config = {

		# Defaults: 'ltf_interval' : "5m", 'rsi_period' : 5
		RSI_OverSold : [
			{'ticker': 'AAPL', 'rsi_period' : 5, 'rsi_limit': 25, 'tp_percentage': 5 },
			{'ticker': 'ADBE', 'rsi_period' : 5, 'rsi_limit': 20, 'tp_percentage': 3 },
			{'ticker': 'AMD', 'rsi_period' : 14, 'rsi_limit': 30, 'tp_percentage': 1 },
			#{'ticker': 'AMZN', 'rsi_period' : 14, 'rsi_limit': 30, 'tp_percentage': 1 },
			{'ticker': 'ANSS', 'rsi_period' : 14, 'rsi_limit': 30, 'tp_percentage': 2 },
			{'ticker': 'BABA', 'rsi_period' : 14, 'rsi_limit': 30, 'tp_percentage': 3 },
			{'ticker': 'BBBY', 'rsi_period' : 5, 'rsi_limit': 30, 'tp_percentage': 4 },
			#{'ticker': 'BLDR', 'rsi_period' : 5, 'rsi_limit': 30, 'tp_percentage': 4 },
			{'ticker': 'BYD', 'rsi_period' : 5, 'rsi_limit': 15, 'tp_percentage': 2 },
			{'ticker': 'BYND', 'rsi_period' : 5, 'rsi_limit': 20, 'tp_percentage': 5 },
			{'ticker': 'CHTR', 'rsi_period' : 25, 'rsi_limit': 30, 'tp_percentage': 5 },
			{'ticker': 'CHWY', 'rsi_period' : 14, 'rsi_limit': 25, 'tp_percentage': 5 },
			{'ticker': 'COUP', 'rsi_period' : 14, 'rsi_limit': 30, 'tp_percentage': 3 },
			{'ticker': 'CRL', 'rsi_period' : 14, 'rsi_limit': 30, 'tp_percentage': 5 },
			{'ticker': 'CRM', 'rsi_period' : 5, 'rsi_limit': 20, 'tp_percentage': 5 },
			{'ticker': 'CROX', 'rsi_period' : 5, 'rsi_limit': 15, 'tp_percentage': 4 },
			{'ticker': 'CRWD', 'rsi_period' : 5, 'rsi_limit': 25, 'tp_percentage': 3 },
			{'ticker': 'CSIQ', 'rsi_period' : 5, 'rsi_limit': 10, 'tp_percentage': 5 },
			{'ticker': 'CTAS', 'rsi_period' : 5, 'rsi_limit': 15, 'tp_percentage': 5 },
			{'ticker': 'CVNA', 'rsi_period' : 5, 'rsi_limit': 15, 'tp_percentage': 5 },
			{'ticker': 'CZR', 'rsi_period' : 5, 'rsi_limit': 20, 'tp_percentage': 3 },
			{'ticker': 'DAL', 'rsi_period' : 5, 'rsi_limit': 5, 'tp_percentage': 5 },
			{'ticker': 'DAR', 'rsi_period' : 5, 'rsi_limit': 25, 'tp_percentage': 5 },
			{'ticker': 'DELL', 'rsi_period' : 5, 'rsi_limit': 15, 'tp_percentage': 2 },
			{'ticker': 'DHI', 'rsi_period' : 5, 'rsi_limit': 25, 'tp_percentage': 3 },
			{'ticker': 'DHR', 'rsi_period' : 5, 'rsi_limit': 15, 'tp_percentage': 5 },
			{'ticker': 'DKS', 'rsi_period' : 14, 'rsi_limit': 50, 'tp_percentage': 1 },
			{'ticker': 'CVNA', 'rsi_period' : 5, 'rsi_limit': 15, 'tp_percentage': 2 },		
			{'ticker': 'DOCU', 'rsi_period' : 5, 'rsi_limit': 30, 'tp_percentage': 2 },	
		]
	}

