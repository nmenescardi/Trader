from __future__ import (absolute_import, division, print_function,
						unicode_literals)
import os.path

from datetime import datetime
from .Strategies.S01_RSI_OverSold import RSI_OverSold
from .Strategies.S05_RSI_OSOB import RSI_OSOB
from .StrategyOptimizer import StrategyOptimizer

import time

def run():
	start_time = time.time()

#if __name__ == '__main__':

	strategy_optimizer = StrategyOptimizer()
 
	strategy_optimizer.add({
		'dataset_dir' : 'datasets/test/',
		'results_folder' : 'test',
		'strategy' : RSI_OverSold,
		'strategy_params' : {
			'rsi_length' : [5,14],#[5,9,14,25],
			'rsi_buy_limit' : [5,15,25],#[*range(5,35,5), 2],
			'take_profit' : [*range(1,6)],
		},
		'from_date' : datetime(2020,4,1),
		'to_date' : datetime(2020,11,2),
		'dt_format' : '%Y-%m-%d %H:%M'
	})

	strategy_optimizer.run()

	print("--- %s seconds ---" % (time.time() - start_time))