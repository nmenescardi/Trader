
from datetime import datetime
from .Strategies.S01_RSI_OverSold import RSI_OverSold
from .Strategies.S05_RSI_OSOB import RSI_OSOB
from .StrategyOptimizer import StrategyOptimizer
from Data.Stocks import Stocks
from Logger import Logger
import time

def run():
	start_time = time.time()

	logger = Logger().get_logger()
	logger.info('0026 - Starting up optimization')

	strategy_optimizer = StrategyOptimizer()
 
	strategy_optimizer.add({
		'ticker_list' : Stocks().get_focus(), #TODO: Allow other lists
		'results_folder' : '5Min_RSI_OverSold',
		'strategy' : RSI_OverSold,
		'strategy_params' : {
			'rsi_length' : [5,9,14,25],
			'rsi_buy_limit' : [*range(5,35,5), 2],
			'take_profit' : [*range(1,6), *range(7,15,2)],
		},
		'from_date' : datetime(2020,4,1),
		#'to_date' : datetime(2020,11,2),
		'dt_format' : '%Y-%m-%d %H:%M'
	})

	strategy_optimizer.run()

	runtime_minutes = (time.time() - start_time) / 60
	logger.info('0027 - Finishing up optimization. Runtime in minutes: {}'.format(runtime_minutes))
