import os
from dotenv import load_dotenv
import mysql.connector
from mysql.connector import Error
from distutils.util import strtobool

class DB():
	def __init__(self):
		load_dotenv()
		credentials = {
			'host' : os.getenv("DB_HOST"),
			'database' : os.getenv("DB_NAME"),
			'user' : os.getenv("DB_USER"),
			'password' : os.getenv("DB_PASSWORD"),
		}

		self.debug_mode = bool(strtobool(os.getenv("DEBUG_MODE")))

		try:
			self.connection = mysql.connector.connect( **credentials )
		except Error as e:
			print("Error while connecting to MySQL", e)
			self.close()


	def cursor(self, buffered = False):
		if (self.connection.is_connected()):
			self.inner_cursor = self.connection.cursor(buffered=buffered)
			return self.inner_cursor

		#TODO: reconnect
		return False


	def close(self):
		if (self.connection.is_connected()):
				self.inner_cursor.close()
				self.connection.close()

	def commit(self):
		self.connection.commit()
