import sys
from Order_Queues.Order_Queues import Order_Queues

order_queues = Order_Queues()

payload = sys.stdin.read()

order_queues.add_ticker_to_open(payload)
