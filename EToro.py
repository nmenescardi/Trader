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

  
	def wait(self, factor = 1):
		time.sleep(random.uniform(0.9 * factor, 2.8  * factor))