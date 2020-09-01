import sys
import redis
import time
from dotenv import load_dotenv
import os

# Load Env variables:
load_dotenv()

redisClient = redis.StrictRedis(host=os.getenv("REDIS_HOST"),
                                port=os.getenv("REDIS_PORT"),
                                db=os.getenv("REDIS_DB"),
                                password=os.getenv("REDIS_PASSWORD"))

tickersSet = "tickersSet"

payload = sys.stdin.read()

redisClient.sadd(tickersSet,payload.encode('utf-8'))
