from Order_Queues.Order_Queues import Order_Queues
from StrategiesManager.Manager import Manager

manager = Manager(queuesHandler = Order_Queues())
manager.run()

