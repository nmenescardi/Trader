import time, random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

class EToro:

	def __init__(self, driver, credentials):
		self.driver = driver
		self.credentials = credentials

	def log_in(self):
		self.driver.get("https://www.etoro.com/login")
		self.wait()
		self.send_keys("//input[@automation-id='login-sts-username-input']", self.credentials.username)
		self.send_keys("//input[@automation-id='login-sts-password-input']", self.credentials.password)
		self.click("//button[@automation-id='login-sts-btn-sign-in']")


	def select_virtual_portfolio(self):
		WebDriverWait(self.driver, 20).until(ec.visibility_of_element_located((By.XPATH, "//div[@automation-id='menu-layout']")))
		menu = self.driver.find_element_by_xpath("//div[@automation-id='menu-layout']")
		self.click("//div[contains(text(),'Real')]", menu)
		self.wait(factor = 2)
		self.click("//span[contains(text(),'Virtual Portfolio')]", menu)
		dial = self.driver.find_element_by_xpath("//div[@class='cdk-overlay-pane']")
		self.click("//a[contains(text(),'Go to Virtual Portfolio')]", dial)
		self.wait(factor = 2)


	def open_position(self, position):
		# Go to stock url
		self.driver.get("https://www.etoro.com/markets/" + position.ticker)
		
  	# Perform trade
		WebDriverWait(self.driver, 20).until(ec.presence_of_element_located((By.XPATH, "//div[@automation-id='trade-button']")))
		self.wait(factor = 2)
		head = self.driver.find_element_by_xpath("//div[@class='user-market-head']")
		self.click("//div[@automation-id='trade-button']", head)
		self.wait(factor = 2)
  
		try:
			self.click("//div[@data-etoro-automation-id='minus-button']")
			self.click("//div[@data-etoro-automation-id='plus-button']")
		except NoSuchElementException:
			pass
 
		self.wait()
		WebDriverWait(self.driver, 20).until(ec.presence_of_element_located((By.XPATH, "//input[@data-etoro-automation-id='input']")))
		self.send_keys("//input[@data-etoro-automation-id='input']", self.backspace(), 0)
		self.send_keys("//input[@data-etoro-automation-id='input']", str(position.amount) + Keys.ENTER, 0)
		self.click("//div[@data-etoro-automation-id='execution-stop-loss-tab-title-value']")
		self.wait()
	
		try:
			self.click("//a[@data-etoro-automation-id='execution-stop-loss-rate-editing-switch-to-amount-button']")
			self.wait()
		except NoSuchElementException:
			pass

		self.send_keys("//input[@data-etoro-automation-id='input']", self.backspace(), 1)
		self.send_keys("//input[@data-etoro-automation-id='input']", str(position.stopLoss) + Keys.ENTER, 1)
		self.click("//div[@data-etoro-automation-id='execution-leverage-tab-title-value']")
		self.wait()
		self.click("//div[@data-etoro-automation-id='execution-take-profit-tab-title-value']")
		self.wait()
		
		try:
			self.click("//a[@data-etoro-automation-id='execution-take-profit-rate-editing-switch-to-amount-button']")
			self.wait()
		except NoSuchElementException:
			pass
 
		self.send_keys("//input[@data-etoro-automation-id='input']", self.backspace(), 1)
		self.send_keys("//input[@data-etoro-automation-id='input']", str(position.takeProfit) + Keys.ENTER, 1)
  
		try:
			self.click("//button[@data-etoro-automation-id='execution-open-entry-order-button']")
		except NoSuchElementException:
			self.click("//button[@data-etoro-automation-id='execution-open-position-button']")

		self.wait(factor = 2)


	def click(self, xPath, container = None):
		if container is None:
			self.driver.find_element_by_xpath(xPath).click()
		else:
			container.find_element_by_xpath(xPath).click()

 
	def send_keys(self, xPath, keys, index = None):
		if not index:
			self.driver.find_element_by_xpath(xPath).send_keys(keys)
		else:
			self.driver.find_elements_by_xpath(xPath)[index].send_keys(keys)
		self.wait()


	def backspace(self):
		return str(Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE)


	def close_position(self, position):
		pass


	def wait(self, factor = 1):
		time.sleep(random.uniform(0.9 * factor, 2.8  * factor))