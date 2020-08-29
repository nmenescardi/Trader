from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import sys
import os
from dotenv import load_dotenv

# Load Env variables:
load_dotenv()

CHROME_DRIVER_PATH = os.getenv("CHROME_DRIVER_PATH")
IS_PRODUCTION_MODE_SET = os.getenv("IS_PRODUCTION_MODE_SET")

if IS_PRODUCTION_MODE_SET == 'true':
  login_username = os.getenv("PRODUCTION_USERNAME")
  login_password = os.getenv("PRODUCTION_PASSWORD")
else:
  login_username = os.getenv("TESTING_USERNAME")
  login_password = os.getenv("TESTING_PASSWORD")


amount = str(50)
stopLoss = str(-2.0)
takeProfit = str(0.50)
options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--start-maximized")
options.add_argument("--kiosk")
driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH, options=options)
#driver = webdriver.Chrome(options=options)
driver.get("https://www.etoro.com/login")

time.sleep(1)
driver.find_element_by_xpath("//input[@automation-id='login-sts-username-input']").send_keys(login_username)
time.sleep(1)
driver.find_element_by_xpath("//input[@automation-id='login-sts-password-input']").send_keys(login_password)
time.sleep(1)
driver.find_element_by_xpath("//button[@automation-id='login-sts-btn-sign-in']").click()
WebDriverWait(driver, 20).until(ec.visibility_of_element_located((By.XPATH, "//div[@automation-id='menu-layout']")))
driver.get("https://www.etoro.com/markets/nvda")


time.sleep(5)
driver.quit()


WebDriverWait(driver, 20).until(ec.visibility_of_element_located((By.XPATH, "//div[@automation-id='menu-layout']")))
menu = driver.find_element_by_xpath("//div[@automation-id='menu-layout']")
menu.find_element_by_xpath("//div[contains(text(),'Real')]").click()
menu.find_element_by_xpath("//span[contains(text(),'Virtual Portfolio')]").click()
dial = driver.find_element_by_xpath("//div[@class='cdk-overlay-pane']")
dial.find_element_by_xpath("//a[contains(text(),'Go to Virtual Portfolio')]").click()
time.sleep(5)
WebDriverWait(driver, 20).until(ec.presence_of_element_located((By.XPATH, "//div[@automation-id='trade-button']")))
head = driver.find_element_by_xpath("//div[@class='user-market-head']")
head.find_element_by_xpath("//div[@automation-id='trade-button']").click()
time.sleep(5)
driver.find_element_by_xpath("//div[@data-etoro-automation-id='minus-button']").click()
driver.find_element_by_xpath("//div[@data-etoro-automation-id='plus-button']").click()
time.sleep(1)
driver.find_elements_by_xpath("//input[@data-etoro-automation-id='input']")[0].send_keys(Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE)
time.sleep(1)
driver.find_elements_by_xpath("//input[@data-etoro-automation-id='input']")[0].send_keys(amount + Keys.ENTER)
time.sleep(1)
time.sleep(1)
driver.find_element_by_xpath("//div[@data-etoro-automation-id='execution-stop-loss-tab-title-value']").click()
time.sleep(1)
#driver.find_element_by_xpath("//a[@data-etoro-automation-id='execution-stop-loss-rate-editing-switch-to-amount-button']").click()
time.sleep(1)
driver.find_elements_by_xpath("//input[@data-etoro-automation-id='input']")[1].send_keys(Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE)
time.sleep(1)
driver.find_elements_by_xpath("//input[@data-etoro-automation-id='input']")[1].send_keys(stopLoss + Keys.ENTER)
time.sleep(1)
driver.find_element_by_xpath("//div[@data-etoro-automation-id='execution-leverage-tab-title-value']").click()
time.sleep(1)
driver.find_element_by_xpath("//div[@data-etoro-automation-id='execution-take-profit-tab-title-value']").click()
time.sleep(1)
#driver.find_element_by_xpath("//a[@data-etoro-automation-id='execution-take-profit-rate-editing-switch-to-amount-button']").click()
time.sleep(1)
driver.find_elements_by_xpath("//input[@data-etoro-automation-id='input']")[1].send_keys(Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE)
time.sleep(1)
driver.find_elements_by_xpath("//input[@data-etoro-automation-id='input']")[1].send_keys(takeProfit + Keys.ENTER)
time.sleep(1)
driver.find_element_by_xpath("//button[@data-etoro-automation-id='execution-open-entry-order-button']").click()
time.sleep(5)
driver.quit()


