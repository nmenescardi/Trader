from DB import DB
from abc import ABC, abstractmethod

class AbstractDAO:

	def __init__(self):
		self.db = DB()


	def execute(self, query, params = None, multi = False):
		try:
			cursor = self.db.cursor(buffered=True)
			cursor.execute(query, params, multi)
			#print(cursor.statement)
			return cursor

		except Exception as e:
			#print(cursor.statement)
			print("Error while querying the DB", e)
			self.db.close()
			return None
