import os, redis, pickle
from dotenv import load_dotenv

class Order_Queues:
	def __init__(self):
		load_dotenv()
  
		self.redisClient = redis.Redis(
			host=os.getenv("REDIS_HOST"),
			port=os.getenv("REDIS_PORT"),
			db=os.getenv("REDIS_DB"),
			password=os.getenv("REDIS_PASSWORD")
		)
		self.orders_to_open_queue = os.getenv("REDIS_OPEN_QUEUE_KEY")
		self.orders_to_close_queue = os.getenv("REDIS_CLOSE_QUEUE_KEY")

	def get_position_to_open(self):
		position = self.redisClient.lindex(self.orders_to_open_queue, 0)
		return self.__maybe_deserialize(position)

	def add_position_to_open(self, position):
		self.redisClient.lpush(self.orders_to_open_queue, pickle.dumps(position))

	def remove_position_from_open(self):
		self.redisClient.lpop(self.orders_to_open_queue)

	def print_open_queue(self):
		#TODO: print tickers instead of binary
		self.__print_queue(self.orders_to_open_queue)

	def empty_open_queue(self):
		self.__empty_queue(self.orders_to_open_queue)


	def add_ticker_to_close(self, ticker):
		self.redisClient.lpush(self.orders_to_close_queue, ticker.encode('utf-8'))

	def get_ticker_to_close(self):
		ticker = self.redisClient.lindex(self.orders_to_close_queue, 0)
		return self.__maybe_decode_utf8(ticker)

	def remove_ticker_from_close(self):
		self.redisClient.lpop(self.orders_to_close_queue)

	def print_close_queue(self):
		self.__print_queue(self.orders_to_close_queue)

	def empty_close_queue(self):
		self.__empty_queue(self.orders_to_close_queue)


	def __maybe_decode_utf8(self, payload):
		try:
			str = payload.decode('utf-8')
			str = str.strip()
			str = str.lower()
		except (UnicodeDecodeError, AttributeError):
			str = None
		return str


	def __maybe_deserialize(self, payload):
		try:
			position = pickle.loads(payload)
		except (TypeError, UnicodeDecodeError, AttributeError):
			position = None
		return position


	def __print_queue(self, queue):
		for i in range(0, self.redisClient.llen(queue)):
			print(self.redisClient.lindex(queue, i))


	def __empty_queue(self, queue):
		while(self.redisClient.llen(queue)!=0):
			print(self.redisClient.lpop(queue))
