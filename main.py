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

# Load Env variables:
load_dotenv()

CHROME_DRIVER_PATH = os.getenv("CHROME_DRIVER_PATH")
IS_PRODUCTION_MODE_SET = os.getenv("IS_PRODUCTION_MODE_SET")
SHOULD_PERFORM_TRADE = os.getenv("SHOULD_PERFORM_TRADE")

if IS_PRODUCTION_MODE_SET == 'true':
  login_username = os.getenv("PRODUCTION_USERNAME")
  login_password = os.getenv("PRODUCTION_PASSWORD")
else:
  login_username = os.getenv("TESTING_USERNAME")
  login_password = os.getenv("TESTING_PASSWORD")

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


# Log In
driver.get("https://www.etoro.com/login")
time.sleep(random.uniform(0.9, 2.8))
driver.find_element_by_xpath("//input[@automation-id='login-sts-username-input']").send_keys(login_username)
time.sleep(random.uniform(0.9, 2.8))
driver.find_element_by_xpath("//input[@automation-id='login-sts-password-input']").send_keys(login_password)
time.sleep(random.uniform(0.9, 2.8))
driver.find_element_by_xpath("//button[@automation-id='login-sts-btn-sign-in']").click()


# Select portfolio type
driver.get("https://www.etoro.com/markets/nvda")
WebDriverWait(driver, 20).until(ec.visibility_of_element_located((By.XPATH, "//div[@automation-id='menu-layout']")))
menu = driver.find_element_by_xpath("//div[@automation-id='menu-layout']")
menu.find_element_by_xpath("//div[contains(text(),'Real')]").click()
menu.find_element_by_xpath("//span[contains(text(),'Virtual Portfolio')]").click()
dial = driver.find_element_by_xpath("//div[@class='cdk-overlay-pane']")
dial.find_element_by_xpath("//a[contains(text(),'Go to Virtual Portfolio')]").click()
time.sleep(random.uniform(3.01, 6.11))


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
