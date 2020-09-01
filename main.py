from selenium import webdriver
import time
import random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import sys
import os
from dotenv import load_dotenv
import redis
from Position import Position
from Credentials import Credentials
from EToro import EToro

# Load Env variables:
load_dotenv()

CHROME_DRIVER_PATH = os.getenv("CHROME_DRIVER_PATH")
IS_PRODUCTION_MODE_SET = os.getenv("IS_PRODUCTION_MODE_SET")
SHOULD_PERFORM_TRADE = os.getenv("SHOULD_PERFORM_TRADE")

if IS_PRODUCTION_MODE_SET == 'true':
  username = os.getenv("PRODUCTION_USERNAME")
  password = os.getenv("PRODUCTION_PASSWORD")
else:
  username = os.getenv("TESTING_USERNAME")
  password = os.getenv("TESTING_PASSWORD")

credentials = Credentials(username, password)

# Load Redis
redisClient = redis.StrictRedis(host=os.getenv("REDIS_HOST"),
                                port=os.getenv("REDIS_PORT"),
                                db=os.getenv("REDIS_DB"),
                                password=os.getenv("REDIS_PASSWORD"))
tickersSet = "tickersSet"

# Trade Params
position = Position(amount = 50, stopLoss = -2, takeProfit = 0.5, isBuyingPosition = True)

# Init Chrome Driver
options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--start-maximized")
options.add_argument("--kiosk")
driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH, options=options)

eToro = EToro(driver, credentials)

eToro.log_in()

eToro.select_portfolio(isRealPortfolio = False)

while True:
  ticker = redisClient.spop(tickersSet)
  if ticker is not None:
    # Go to stock url
    driver.get("https://www.etoro.com/markets/" + ticker.decode('utf-8'))
  
    # Maybe break exec
    if SHOULD_PERFORM_TRADE == 'false':
      time.sleep(random.uniform(3.01, 6.11))
      driver.quit()

    # Perform trade
    WebDriverWait(driver, 20).until(ec.presence_of_element_located((By.XPATH, "//div[@automation-id='trade-button']")))
    time.sleep(random.uniform(3.01, 6.11))
    head = driver.find_element_by_xpath("//div[@class='user-market-head']")
    head.find_element_by_xpath("//div[@automation-id='trade-button']").click()
    time.sleep(random.uniform(3.01, 6.11))
    driver.find_element_by_xpath("//div[@data-etoro-automation-id='minus-button']").click()
    driver.find_element_by_xpath("//div[@data-etoro-automation-id='plus-button']").click()
    time.sleep(random.uniform(0.9, 2.8))
    driver.find_elements_by_xpath("//input[@data-etoro-automation-id='input']")[0].send_keys(Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE)
    time.sleep(random.uniform(0.9, 2.8))
    driver.find_elements_by_xpath("//input[@data-etoro-automation-id='input']")[0].send_keys(str(position.amount) + Keys.ENTER)
    time.sleep(random.uniform(0.9, 2.8))
    time.sleep(random.uniform(0.9, 2.8))
    driver.find_element_by_xpath("//div[@data-etoro-automation-id='execution-stop-loss-tab-title-value']").click()
    time.sleep(random.uniform(0.9, 2.8))
    driver.find_element_by_xpath("//a[@data-etoro-automation-id='execution-stop-loss-rate-editing-switch-to-amount-button']").click()
    time.sleep(random.uniform(0.9, 2.8))
    driver.find_elements_by_xpath("//input[@data-etoro-automation-id='input']")[1].send_keys(Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE)
    time.sleep(random.uniform(0.9, 2.8))
    driver.find_elements_by_xpath("//input[@data-etoro-automation-id='input']")[1].send_keys(str(position.stopLoss) + Keys.ENTER)
    time.sleep(random.uniform(0.9, 2.8))
    driver.find_element_by_xpath("//div[@data-etoro-automation-id='execution-leverage-tab-title-value']").click()
    time.sleep(random.uniform(0.9, 2.8))
    driver.find_element_by_xpath("//div[@data-etoro-automation-id='execution-take-profit-tab-title-value']").click()
    time.sleep(random.uniform(0.9, 2.8))
    driver.find_element_by_xpath("//a[@data-etoro-automation-id='execution-take-profit-rate-editing-switch-to-amount-button']").click()
    time.sleep(random.uniform(0.9, 2.8))
    driver.find_elements_by_xpath("//input[@data-etoro-automation-id='input']")[1].send_keys(Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE)
    time.sleep(random.uniform(0.9, 2.8))
    driver.find_elements_by_xpath("//input[@data-etoro-automation-id='input']")[1].send_keys(str(position.takeProfit) + Keys.ENTER)
    time.sleep(random.uniform(0.9, 2.8))
    
    try:
        driver.find_element_by_xpath("//button[@data-etoro-automation-id='execution-open-entry-order-button']").click()
    except NoSuchElementException:
        driver.find_element_by_xpath("//button[@data-etoro-automation-id='execution-open-position-button']").click()
  
    time.sleep(random.uniform(3.01, 6.11))
    
driver.quit()
time.sleep(3)    
