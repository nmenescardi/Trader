import os
from dotenv import load_dotenv
import mysql.connector
from mysql.connector import Error

class DB():
	def __init__(self):
		load_dotenv()
		credentials = {
			'host' : os.getenv("DB_HOST"),
			'database' : os.getenv("DB_NAME"),
			'user' : os.getenv("DB_USER"),
			'password' : os.getenv("DB_PASSWORD"),
		}

		try:
			self.connection = mysql.connector.connect( **credentials )
		except Error as e:
			print("Error while connecting to MySQL", e)
			self.close()


	def cursor(self):
		if (self.connection.is_connected()):
			self.inner_cursor = self.connection.cursor()
			return self.inner_cursor

		#TODO: reconnect
		return False


	def close(self):
		if (self.connection.is_connected()):
				self.inner_cursor.close()
				self.connection.close()
