import os, redis
from dotenv import load_dotenv

class Order_Queues:
	def __init__(self):
		load_dotenv()
  
		self.redisClient = redis.StrictRedis(
			host=os.getenv("REDIS_HOST"),
			port=os.getenv("REDIS_PORT"),
			db=os.getenv("REDIS_DB"),
			password=os.getenv("REDIS_PASSWORD")
		)
		self.orders_to_open_queue = os.getenv("REDIS_OPEN_QUEUE_KEY")
		self.orders_to_close_queue = os.getenv("REDIS_CLOSE_QUEUE_KEY")

	def get_ticker_to_open(self):
		ticker = self.redisClient.spop(self.orders_to_open_queue)
		return self.maybe_decode_utf8(ticker)

	def get_ticker_to_close(self):
		ticker = self.redisClient.spop(self.orders_to_close_queue)
		return self.maybe_decode_utf8(ticker)

	def add_ticker_to_open(self, ticker):
		self.redisClient.sadd(self.orders_to_open_queue, ticker.encode('utf-8'))

	def add_ticker_to_close(self, ticker):
		self.redisClient.sadd(self.orders_to_close_queue, ticker.encode('utf-8'))
  
	def maybe_decode_utf8(self, payload):
		try:
			str = payload.decode('utf-8')
			str = str.strip()
			str = str.lower()
		except (UnicodeDecodeError, AttributeError):
			str = None
		return str
