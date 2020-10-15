import time, random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, TimeoutException

class EToro:

	def __init__(self, driver, credentials, logger, is_virtual_portfolio = True):
		self.driver = driver
		self.credentials = credentials
		self.is_virtual_portfolio = is_virtual_portfolio
		self.open_positions = set()
		self.logger = logger

	
	def init(self):
		self.log_in()
		
		self.check_proper_portfolio_is_selected()
   
		self.update_open_orders()


	def log_in(self):
		self.driver.get("https://www.etoro.com/login")
		self.wait()
		self.send_keys("//input[@automation-id='login-sts-username-input']", self.credentials.username)
		self.send_keys("//input[@automation-id='login-sts-password-input']", self.credentials.password)
		self.click("//button[@automation-id='login-sts-btn-sign-in']")


	def switch_portfolio_type(self):
		portfolio_type = 'Virtual' if self.is_virtual_portfolio else 'Real'
		self.logger.info('0009 - Portfolio type to select: {}'.format(portfolio_type))
  
		menu = self.get_menu_element()
		self.click(self.get_portfolio_type_path(), menu)
		self.click("//span[contains(text(),'{} Portfolio')]".format(portfolio_type), menu)
		dial = self.driver.find_element_by_xpath("//div[@class='cdk-overlay-container']")
		self.click("//a[contains(text(),'Go to {} Portfolio')]".format(portfolio_type), dial)


	def get_menu_element(self):
		WebDriverWait(self.driver, 20).until(ec.visibility_of_element_located((By.XPATH, "//div[@automation-id='menu-layout']")))
		return self.driver.find_element_by_xpath("//div[@automation-id='menu-layout']")


	def get_portfolio_type_path(self):
		return "//div[contains(@class,'header-text')]"


	def check_proper_portfolio_is_selected(self):
		menu = self.get_menu_element()
		portfolio_type_elem = menu.find_element_by_xpath(self.get_portfolio_type_path())
		portfolio_type = str(portfolio_type_elem.text).lower()
  
		if (
      		(self.is_virtual_portfolio and ('real' in portfolio_type))
			or (not self.is_virtual_portfolio and ('virtual' in portfolio_type))
    	): 
			self.switch_portfolio_type()


	def open_position(self, position):
		if position.ticker in self.open_positions:
			self.logger.info('0009 - There is an open position for {} already'.format(position.ticker))
			return True # Open only one order per ticker at a time

		if position.amount > self.get_available_balance():
			self.logger.info('0010 - insufficient funds')
			return False
   
		self.check_proper_portfolio_is_selected()

		# Go to stock url
		self.driver.get("https://www.etoro.com/markets/" + position.ticker)
		
 		# Perform trade
		self.wait_for_element("//div[@automation-id='trade-button']", 0)
		self.wait()

		self.click_trade_button(times = 4)
  
		self.wait()
		self.send_keys("//input[@data-etoro-automation-id='input']", self.backspace(), 0)
		self.send_keys("//input[@data-etoro-automation-id='input']", str(position.amount) + Keys.ENTER, 0)
		self.click("//div[@data-etoro-automation-id='execution-stop-loss-tab-title-value']")
	
		self.click("//a[@data-etoro-automation-id='execution-stop-loss-rate-editing-switch-to-amount-button']")

		self.send_keys("//input[@data-etoro-automation-id='input']", self.backspace(), 1)
		self.send_keys("//input[@data-etoro-automation-id='input']", str(position.stopLoss) + Keys.ENTER, 1)

		self.click("//div[@data-etoro-automation-id='execution-leverage-tab-title-value']")
		self.click("//div[@data-etoro-automation-id='execution-take-profit-tab-title-value']")

		self.click("//a[@data-etoro-automation-id='execution-take-profit-rate-editing-switch-to-amount-button']")

		self.send_keys("//input[@data-etoro-automation-id='input']", self.backspace(), 1)
		self.send_keys("//input[@data-etoro-automation-id='input']", str(position.takeProfit) + Keys.ENTER, 1)

		try:
			self.click(
				xPath = "//button[@data-etoro-automation-id='execution-open-entry-order-button']",
				should_raise_exception = True
			)
			self.logger.info('0011 - Open position for {} finished without exceptions'.format(position.ticker))
		except NoSuchElementException:
			self.click("//button[@data-etoro-automation-id='execution-open-position-button']")

		self.update_open_orders()
   
		return self.is_ticker_open(position.ticker)


	def get_available_balance(self):
		balance_elem = self.driver.find_element_by_xpath('//span[@automation-id="account-balance-availible-unit-value"]')
		self.logger.info('0013 - Available balance: {}'.format(balance_elem.text))
		balance_str = str(balance_elem.text).replace('$', '').replace(',', '')
		balance_rounded_str = balance_str.split(".")[0] 
		balance = int(balance_rounded_str)
		return balance		


	def click(self, xPath, container = None, should_raise_exception = False):
		try:
			if container is None:
				self.driver.find_element_by_xpath(xPath).click()
			else:
				container.find_element_by_xpath(xPath).click()
		except NoSuchElementException as e:
			self.logger.exception('0014 - Error trying to click on element with xPath: {}'.format(xPath))
			if should_raise_exception:
				self.logger.info('0015 - Raising exception after trying to click on element with xPath: {}'.format(xPath))
				raise NoSuchElementException
		
		self.wait()
  
  
	def click_trade_button(self, times = 3):
		try:
			self.click("//div[@automation-id='trade-button']")
			WebDriverWait(self.driver, 8).until(ec.presence_of_element_located((By.XPATH, "//input[@data-etoro-automation-id='input']")))
		except (NoSuchElementException, TimeoutException):
			self.logger.exception('0016 - Error trying to click on trade button. Times left: {}'.format(str(times)))
			if times > 0:
				self.wait()
				self.click_trade_button(times - 1)
 
 
	def send_keys(self, xPath, keys, index = None):
		try:
			if not index:
				self.driver.find_element_by_xpath(xPath).send_keys(keys)
			else:
				self.driver.find_elements_by_xpath(xPath)[index].send_keys(keys)
		except (NoSuchElementException, IndexError):
			self.logger.exception('0017 - Error trying to send keys for element with xPath: {}'.format(xPath))
		self.wait()


	def backspace(self):
		return str(Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE)


	def close_position(self, ticker):
		self.check_proper_portfolio_is_selected()

		target_url = "https://www.etoro.com/portfolio/" + ticker
		self.driver.get(target_url)
		self.wait(factor = 2.5)
		
		if self.driver.current_url != target_url:
			self.logger.info('0018 - There is no open position for {}.'.format(ticker))
			return True #TODO: returning True to avoid infinite loops. Send notification when it happens
 
		try:
			self.click("//div[@data-etoro-automation-id='open-trades-table-body-cell-user-actions-close-button']")
			self.click("//button[@data-etoro-automation-id='close-position-close-button']")

			self.logger.info('0019 - Position close for {} without exceptions.'.format(ticker))
			self.update_open_orders()
			return not self.is_ticker_open(ticker)

		except NoSuchElementException:
			self.logger.exception('0020 - Error trying to close position for: {}'.format(ticker))
			return False


	def is_ticker_open(self, ticker):
		return ticker in self.open_positions
		

	def go_to_portfolio(self):
		self.driver.get("https://www.etoro.com/portfolio/")
		self.wait_for_element("//div[@data-etoro-automation-id='portfolio-overview']", 0)
		self.wait()


	def update_open_orders(self):
		self.go_to_portfolio()
  
		elements = self.driver.find_elements_by_xpath("//div[@data-etoro-automation-id='portfolio-overview-table-body-cell-market-name']")

		self.open_positions.clear()

		for element in elements:
			ticker = str(element.text).lower()
			self.open_positions.add(ticker)

		self.logger.info('0012 - Positions opened: {}'.format(', '.join(str(e) for e in self.open_positions)))


	def wait_for_element(self, xPath, times = 0, action = None):
		try:
			WebDriverWait(self.driver, 20).until(ec.presence_of_element_located((By.XPATH, xPath)))
		except TimeoutException:
			# let's refresh and try again 
			if times > 0:
				self.driver.refresh()
				self.wait()
				if action is not None:
					action()

			# No luck
			return False
		# Return success
		return True
    
  
	def wait(self, factor = 1):
		time.sleep(random.uniform(0.5 * factor, 1.2 * factor))
