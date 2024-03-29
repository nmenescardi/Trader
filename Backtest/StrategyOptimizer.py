import os, sys, itertools
from pathlib import Path
from datetime import datetime
import backtrader as bt
from itertools import product
from .DataFeed.MySQL import MySQL
from Logger import Logger

class StrategyOptimizer:

	def __init__(self):
		self.mod_path = os.path.dirname(os.path.abspath(sys.argv[0]))
		self.optimizations = []
		self.logger = Logger().get_logger()


	def add(self, optimization):
		self.optimizations.append(optimization)


	def run(self):
		for optimization in self.optimizations:
			
			for ticker in optimization['ticker_list']:
				self.logger.info('0028 - Running optimization for {}'.format(ticker))

				filename = ticker + '_5min' #TODO: no needed anymore
				ticker_file_name = filename.split(".")[0]

				optimization = self.__fill_default(optimization)

				if ticker_file_name in optimization['exclude']:
					continue

				# Create directory if not exists
				results_dir = "Backtest/results/{}/".format(optimization['results_folder'])
				Path(results_dir).mkdir(parents=True, exist_ok=True)

				results_file_path = "{}/{}_{}_{}.csv".format(
					results_dir, 
					ticker_file_name, 
					optimization['from_date'].strftime('%Y-%m-%d'),
					optimization['to_date'].strftime('%Y-%m-%d')
				)
				results_file_path = os.path.join(self.mod_path, results_file_path)

				param_names = list(optimization['strategy_params'].keys())
				param_combinations = (zip(param_names, x) for x in product(*optimization['strategy_params'].values()))

				data = MySQL(
					ticker = ticker,
					fromdate = optimization['from_date'],
					todate = optimization['to_date'],
				)

				for param_set in param_combinations:

					cerebro = bt.Cerebro(optreturn=False)

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
