import logging

class Logger:
	def __init__(self):
		self.logger = logging
		logging.basicConfig(
			filename='app.log',
			filemode='a', # append
			format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
			datefmt='%d-%b-%y %H:%M:%S',
			level=logging.INFO
		)

	def get_logger(self):
		return self.logger
