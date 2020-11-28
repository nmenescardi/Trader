import os, sys, itertools
from datetime import datetime
import backtrader as bt
from itertools import product

class StrategyOptimizer:

	def __init__(self):
		self.mod_path = os.path.dirname(os.path.abspath(sys.argv[0]))
		self.optimizations = []


	def add(self, optimization):
		self.optimizations.append(optimization)


	def run(self):
		for optimization in self.optimizations:
			
			for filename in os.listdir( optimization['dataset_dir'] ):
				ticker_file_name = filename.split(".")[0]

				optimization = self.__fill_default(optimization)

				if ticker_file_name in optimization['exclude']:
					continue

				results_file_path = "results/{}/{}_{}.csv".format(optimization['results_folder'], ticker_file_name, optimization['from_date'].strftime('%Y-%m-%d'))
				results_file_path = os.path.join(self.mod_path, results_file_path)

				param_names = list(optimization['strategy_params'].keys())
				param_combinations = (zip(param_names, x) for x in product(*optimization['strategy_params'].values()))

				for param_set in param_combinations:
					print(ticker_file_name)

					cerebro = bt.Cerebro(optreturn=False)

					data_file_name = '{}/{}.csv'.format(optimization['dataset_dir'], ticker_file_name)
					data = bt.feeds.GenericCSVData(
						dataname=os.path.join(self.mod_path, data_file_name),
						#dtformat='%Y-%m-%d %H:%M',
						fromdate = optimization['from_date'],
						todate = optimization['to_date'],
						dtformat=optimization['dt_format'],
						buffered= True,
					)
					cerebro.adddata(data)

					if optimization['should_resample']:
						cerebro.resampledata(data, timeframe=bt.TimeFrame.Days)

					cerebro.broker.setcash(optimization['startcash'])

					cerebro.addsizer(bt.sizers.PercentSizerInt, percents=100)

					cerebro.addanalyzer(bt.analyzers.TradeAnalyzer, _name="ta")

					cerebro.broker.setcommission(commission=optimization['commission']) 

					cerebro.addstrategy(
						optimization['strategy'],
						** dict(param_set),
						results_file_path = results_file_path,
					)
					cerebro.run(maxcpus=1)

	
	def __fill_default(self, optimization):
		default = {
			'dataset_dir' : 'datasets/5min/',
			'results_folder' : 'Default_Folder',
			'startcash' : 10000,
			'from_date' : datetime(2018,11,13),
			'to_date' : datetime.now(),
			'should_resample' : False,
			'commission' : 0.0005,
			'ticker_file_name' : 'AAPL5min',
			'exclude' : [],
			'dt_format' : '%Y-%m-%d',
		}

		for key, value in default.items():
			try:
				optimization[key] = optimization[key]
			except (KeyError, NameError):
				optimization[key] = default[key]

		return optimization
