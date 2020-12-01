from __future__ import (absolute_import, division, print_function,
						unicode_literals)
import os.path
import sys, os, itertools
from datetime import datetime
from matplotlib import warnings
import backtrader as bt
from Strategies.S01_RSI_OverSold import RSI_OverSold

import time
start_time = time.time()

dataset_dir = 'datasets/test/'

def run_strategies(
	rsi_length=14,
	rsi_buy_limit=15,
	take_profit=8,
	supertrend_period=7,
	supertrend_multiplier=3,
	rsi_sell_limit=82,
	printlog=False,
	startcash = 1000,
	min_days_between_trades = 2,
	ticker_file_name = 'AAPL-5min',
	from_date = datetime(2018,11,13),
	to_date = datetime.now(),
	should_plot = False,
	should_resample = False
):
	# Create a cerebro entity
	cerebro = bt.Cerebro(optreturn=False)

	results_file_path = "results/S01_RSI_OverSold_5min/{}_{}.csv".format(ticker_file_name, from_date.strftime('%Y-%m-%d'))

	# Datas are in a subfolder of the samples. Need to find where the script is
	# because it could have been called from anywhere
	modpath = os.path.dirname(os.path.abspath(sys.argv[0]))
	datapath = os.path.join(modpath, '{}/{}.csv'.format(dataset_dir, ticker_file_name))

	# Create a Data Feed
	data = bt.feeds.GenericCSVData(
		dataname=datapath,
		#dtformat='%Y-%m-%d %H:%M',
		fromdate = from_date,
		todate = to_date,
		dtformat='%Y-%m-%d',
		buffered= True,
		timeframe=bt.TimeFrame.Minutes, compression=5
	)
	
	# Add the Data Feed to Cerebro
	cerebro.adddata(data)

	if should_resample:
		cerebro.resampledata(data, timeframe=bt.TimeFrame.Days)


	# Set our desired cash start
	cerebro.broker.setcash(startcash)

	# Add a FixedSize sizer according to the stake
	cerebro.addsizer(bt.sizers.PercentSizerInt, percents=100)

	cerebro.addanalyzer(bt.analyzers.TradeAnalyzer, _name="ta")

	# Set the commission
	cerebro.broker.setcommission(commission=0.0005)  # 0.05% of the operation value

	cerebro.addstrategy(
		RSI_OverSold,
		rsi_length=rsi_length,
		rsi_buy_limit=rsi_buy_limit,
		take_profit=take_profit,
		#supertrend_period=supertrend_period,
		rsi_sell_limit=rsi_sell_limit,
		#supertrend_multiplier=supertrend_multiplier,
		printlog=printlog,
		amount = startcash, #(startcash / 3), #
		results_file_path = results_file_path
	)
	
	strategies = cerebro.run(maxcpus=1)

	portfolio_value = cerebro.broker.getvalue()
	print('Final Portfolio Value: ${}'.format( round(portfolio_value, 2) ))
	portfolio_change = round(100 * (portfolio_value / startcash -1), 2)
	print('Portfolio Change: {}%'.format(portfolio_change))

	if should_plot:
		sys.stdout.flush()
		cerebro.plot()


if __name__ == '__main__':

	for filename in os.listdir(dataset_dir):
		symbol_tf = filename.split(".")[0]
		
		# opt params:
		rsi_length = [*range(1,20)]
		rsi_buy_limit = [*range(1,80)]
		take_profit = [*range(1,8)]

		params_combination = itertools.product(rsi_length, rsi_buy_limit, take_profit)

		for params in params_combination:
			print(symbol_tf, *params)

			run_strategies(
				*params,
				rsi_sell_limit=82,
				printlog = False,
				startcash = 1000,
				ticker_file_name = symbol_tf,
				from_date = datetime(2020,4,1),
				#to_date = datetime(2020,4,22),
				should_plot = False,
				should_resample = False
			)

print("--- %s seconds ---" % (time.time() - start_time))