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
		self.driver.find_element_by_xpath("//input[@automation-id='login-sts-username-input']").send_keys(self.credentials.username)
		self.wait()
		self.driver.find_element_by_xpath("//input[@automation-id='login-sts-password-input']").send_keys(self.credentials.password)
		self.wait()
		self.driver.find_element_by_xpath("//button[@automation-id='login-sts-btn-sign-in']").click()


	def select_portfolio(self, isRealPortfolio = False):
		WebDriverWait(self.driver, 20).until(ec.visibility_of_element_located((By.XPATH, "//div[@automation-id='menu-layout']")))
		menu = self.driver.find_element_by_xpath("//div[@automation-id='menu-layout']")
		menu.find_element_by_xpath("//div[contains(text(),'Real')]").click() 
		self.wait(factor = 2)
		menu.find_element_by_xpath("//span[contains(text(),'Virtual Portfolio')]").click()
		dial = self.driver.find_element_by_xpath("//div[@class='cdk-overlay-pane']")
		dial.find_element_by_xpath("//a[contains(text(),'Go to Virtual Portfolio')]").click()	
		self.wait(factor = 2)

	def open_position(self, position):
		# Go to stock url
		self.driver.get("https://www.etoro.com/markets/" + position.ticker)
		
  	# Perform trade
		WebDriverWait(self.driver, 20).until(ec.presence_of_element_located((By.XPATH, "//div[@automation-id='trade-button']")))
		self.wait(factor = 2)
		head = self.driver.find_element_by_xpath("//div[@class='user-market-head']")
		head.find_element_by_xpath("//div[@automation-id='trade-button']").click()
		self.wait(factor = 2)
  
		try:
			self.driver.find_element_by_xpath("//div[@data-etoro-automation-id='minus-button']").click()
			self.driver.find_element_by_xpath("//div[@data-etoro-automation-id='plus-button']").click()
		except NoSuchElementException:
			pass
 
		self.wait()
		WebDriverWait(self.driver, 20).until(ec.presence_of_element_located((By.XPATH, "//input[@data-etoro-automation-id='input']")))
		self.driver.find_elements_by_xpath("//input[@data-etoro-automation-id='input']")[0].send_keys(Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE)
		self.wait()
		self.driver.find_elements_by_xpath("//input[@data-etoro-automation-id='input']")[0].send_keys(str(position.amount) + Keys.ENTER)
		self.wait()
		self.wait()
		self.driver.find_element_by_xpath("//div[@data-etoro-automation-id='execution-stop-loss-tab-title-value']").click()
		self.wait()
		self.driver.find_element_by_xpath("//a[@data-etoro-automation-id='execution-stop-loss-rate-editing-switch-to-amount-button']").click()
		self.wait()
		self.driver.find_elements_by_xpath("//input[@data-etoro-automation-id='input']")[1].send_keys(Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE)
		self.wait()
		self.driver.find_elements_by_xpath("//input[@data-etoro-automation-id='input']")[1].send_keys(str(position.stopLoss) + Keys.ENTER)
		self.wait()
		self.driver.find_element_by_xpath("//div[@data-etoro-automation-id='execution-leverage-tab-title-value']").click()
		self.wait()
		self.driver.find_element_by_xpath("//div[@data-etoro-automation-id='execution-take-profit-tab-title-value']").click()
		self.wait()
		self.driver.find_element_by_xpath("//a[@data-etoro-automation-id='execution-take-profit-rate-editing-switch-to-amount-button']").click()
		self.wait()
		self.driver.find_elements_by_xpath("//input[@data-etoro-automation-id='input']")[1].send_keys(Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE)
		self.wait()
		self.driver.find_elements_by_xpath("//input[@data-etoro-automation-id='input']")[1].send_keys(str(position.takeProfit) + Keys.ENTER)
		self.wait()
  
		try:
			self.driver.find_element_by_xpath("//button[@data-etoro-automation-id='execution-open-entry-order-button']").click()
		except NoSuchElementException:
			self.driver.find_element_by_xpath("//button[@data-etoro-automation-id='execution-open-position-button']").click()

		self.wait(factor = 2)
  
	def click(self, xPath):
		self.driver.find_element_by_xpath(xPath).click()
  
	def send_keys(self, xPath, keys, index = 1):
		self.driver.find_elements_by_xpath(xPath)[index].send_keys(keys)
  
	def backspace(self):
		return Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE

	def close_position(self, position):
		pass
  
	def wait(self, factor = 1):
		time.sleep(random.uniform(0.9 * factor, 2.8  * factor))