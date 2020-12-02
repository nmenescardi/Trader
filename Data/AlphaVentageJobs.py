from Data.AbstractDAO import AbstractDAO

class AlphaVentageJobs(AbstractDAO):

	def insert_job(self, ticker, data_month, data_year):
		self.execute(
			"""
				INSERT IGNORE INTO alphaventage_jobs 
					(ticker, data_month, data_year)
				VALUES 
					(%s,%s,%s);
			""",
			(ticker, data_month, data_year, )
		)
		self.db.commit()


	def get_single_job(self):

		iterator = self.execute(
			"""
				SELECT job_id, ticker, data_month, data_year
				FROM alphaventage_jobs
				WHERE deleted = 0 
				AND attempts < 3
				ORDER BY created_date ASC, attempts ASC
				LIMIT 1;
			"""
		)

		for job in iterator:
			if len(job) < 1:
				return None

			print(job)
			return {
				'job_id': job[0],
				'ticker': job[1],
				'data_month': job[2],
				'data_year': job[3],
			}


	def mark_as_failed(self, job_id):

		self.execute(
			"""
				UPDATE alphaventage_jobs
				SET attempts = attempts + 1
				WHERE job_id = %s;
			""",
			(job_id,)
		)
		self.db.commit()


	def mark_as_finished(self, job_id):

		self.execute(
			"""
				DELETE FROM alphaventage_jobs
				WHERE job_id = %s;
			""",
			(job_id,)
		)
		self.db.commit()
