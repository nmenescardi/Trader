from Data.DB import DB
from abc import ABC, abstractmethod

class AbstractDAO:

	def __init__(self):
		self.db = DB()


	def execute(self, query, params = None, multi = False, named_tuple = False, buffered = True):
		try:
			cursor = self.db.cursor(named_tuple=named_tuple, buffered=buffered)
			cursor.execute(query, params, multi)
			result = cursor

		except Exception as e:
			print("Error while querying the DB", e)
			self.db.close()
			result = None

		finally:
			if self.db.debug_mode:
				print(cursor.statement)

			return result
