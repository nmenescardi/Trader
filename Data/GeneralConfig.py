from Data.DB import DB
from Data.AbstractDAO import AbstractDAO
from datetime import datetime
import numpy as np

class GeneralConfig(AbstractDAO):

	def get_last_portfolio_positions_update(self):
		cursor = self.execute("SELECT last_portfolio_positions_update FROM general_config;")

		for (last_portfolio_positions_update) in cursor:
			return last_portfolio_positions_update[0]


	def update_last_portfolio_positions_flag(self):
		cursor = self.execute(
			"UPDATE general_config SET last_portfolio_positions_update = %s;", 
			(datetime.now().date(),)
		)
		self.db.commit()


	def should_update_positions(self, days_between_updates = 1):
		last_positions_update = self.get_last_portfolio_positions_update()

		if last_positions_update is None:
			return True

		current_timestamp = datetime.now()

		days_since_last_update = np.busday_count(last_positions_update.date(), current_timestamp.date())
		#print('Days passed since last portfolio positions update: {}'.format(days_since_last_update))

		if days_since_last_update >= days_between_updates:
			return True

		return False
