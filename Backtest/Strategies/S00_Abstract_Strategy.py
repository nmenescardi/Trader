import os.path
import backtrader as bt
import pandas as pd

class Abstract_Strategy(bt.Strategy):
	params = (
		('should_make_report', True),
		('printlog', False),
		('results_file_path', 'results/results.csv'),
	)

	def __init__(self):
		self.startcash = self.broker.getvalue()
		self.bar_executed = 0

		# Keep a reference to the "close" of the Low DataFrame (eg: 5 minutes)
		self.dataclose = self.datas[0].close
		self.ltf_dataclose = self.datas[0].close

		# To keep track of pending orders and buy price/commission
		self.order = None
		self.buyprice = None
		self.buycomm = None

	
	def maybe_limit_number_bars(self):
		if not isinstance(self.p.number_bars_stop, bool) and self.bar_executed + self.p.number_bars_stop < len(self):
			self.log('Bar Executed: {}. Bars to stop: {}. Current len {}.'.format(self.bar_executed, self.p.number_bars_stop, len(self)))
			self.sell()


	# Check if current bar datatime is greater than given date. Use [2020, 11, 12] as param
	def date_bar_greater_than(self, date_as_list):
		import datetime
		bar_datetime = datetime.datetime(*date_as_list)
		return bar_datetime < self.datetime.datetime()


	def stop(self):
		self.buyAndHoldReturn()
		if self.p.should_make_report:
			self.saveResults()


	def log(self, txt, dt = None, doprint = False):
		if self.params.printlog or doprint:
			dt = dt or self.datas[0].datetime.date(0)
			print('%s, %s' % (dt.isoformat(), txt))


	def notify_trade(self, trade):
		if not trade.isclosed:
			return

		self.log('OPERATION PROFIT, GROSS %.2f, NET %.2f' %
				 (trade.pnl, trade.pnlcomm))


	def notify_order(self, order):
		if order.status in [order.Submitted, order.Accepted]:
			# Buy/Sell order submitted/accepted to/by broker - Nothing to do
			return

		# Check if an order has been completed
		# Attention: broker could reject order if not enough cash
		if order.status in [order.Completed]:
			if order.isbuy():
				self.log(
					'BUY EXECUTED, Price: %.2f, Cost: %.2f, Comm %.2f' %
					(order.executed.price,
					 order.executed.value,
					 order.executed.comm))

				self.buyprice = order.executed.price
				self.buycomm = order.executed.comm

			else:  # Sell
				self.log('SELL EXECUTED, Price: %.2f, Cost: %.2f, Comm %.2f' %
						 (order.executed.price,
						  order.executed.value,
						  order.executed.comm))

			self.bar_executed = len(self)

		elif order.status in [order.Canceled, order.Margin, order.Rejected]:
			self.log('Order Canceled/Margin/Rejected')

		# Write down: no pending order
		self.order = None


	def buyAndHoldReturn(self, should_print = True):
		first_price = self.ltf_dataclose[+1-len(self.ltf_dataclose)]
		last_price = self.ltf_dataclose[0]
		total_return = round(100 * (last_price / first_price -1), 2)
		
		if should_print:
			#TODO: Apply same commission
			print('Buy and Hold Total Return {}%'.format(total_return))

		return total_return


	def saveResults(self):
		if not self.p.should_make_report:
			return

		data = self.getResults()

		file_path = self.params.results_file_path

		try:
			# Save data. Create file or append at the end
			if not os.path.exists(file_path):
				data.to_csv(file_path, sep = ',', encoding = 'cp1251', index = False) 
			else:
				data.to_csv(file_path, sep = ',', encoding = 'cp1251', index = False, mode='a', header=False)
		except Exception as e:
			print(e)


	# Override this method returning a dict with custom params to save into final report
	def getParamsForResult(self):
		return {}


	def getResults(self):
		buy_and_hold_return = self.buyAndHoldReturn(should_print=False)
		PnL_percent = round(100 * (self.broker.getvalue() / self.startcash -1), 2)

		results = {
			** self.getParamsForResult(),
			'Strategy Total PnL %' : [PnL_percent],
			'Buy and Hold %' : [buy_and_hold_return],
			'Total # Bars' : self.buflen(),
			'BnH/Bars Ratio' : round(buy_and_hold_return / self.buflen(), 5),
		}

		try:
			ta = self.analyzers[0].get_analysis()
			if ta.total.total > 0 and isinstance(ta.total.closed, int) and ta.total.closed > 0:
				results['# Open'] = ta.total.open
				results['# Closed'] = ta.total.closed
				results['# Won'] = ta.won.total
				results['# Lost'] = ta.lost.total
				results['Pnl Closed'] = round(ta.pnl.net.total, 2)
				pnl_closed_percentage = round(100 * (ta.pnl.net.total / self.startcash), 2)
				results['Pnl Closed %'] = pnl_closed_percentage
				results['Pnl/Bars Ratio'] = round(pnl_closed_percentage / ta.len.total, 5)
				results['Avg # Bars'] = round(ta.len.average, 2)
				results['# Bars'] = ta.len.total
				results['Min # Bars'] = ta.len.min
				results['Max # Bars'] = ta.len.max

				print('Strategy Won {}. Lost {}.'.format(ta.won.total, ta.lost.total))
		except Exception as e:
			print('Exception trying to get Trade Analysis. Error: {}'.format(e))
		
		return pd.DataFrame(results)
