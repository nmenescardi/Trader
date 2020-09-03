from selenium import webdriver
import os
from dotenv import load_dotenv
from distutils.util import strtobool
from Position import Position
from Credentials import Credentials
from EToro import EToro
from Order_Queues import Order_Queues

# Load Env variables:
load_dotenv()

CHROME_DRIVER_PATH = os.getenv("CHROME_DRIVER_PATH")
IS_PRODUCTION_MODE_SET = bool(strtobool(os.getenv("IS_PRODUCTION_MODE_SET")))
SHOULD_PERFORM_TRADE = bool(strtobool(os.getenv("SHOULD_PERFORM_TRADE")))
IS_VIRTUAL_PORTFOLIO = bool(strtobool(os.getenv("IS_VIRTUAL_PORTFOLIO")))

if IS_PRODUCTION_MODE_SET:
	username = os.getenv("PRODUCTION_USERNAME")
	password = os.getenv("PRODUCTION_PASSWORD")
else:
	username = os.getenv("TESTING_USERNAME")
	password = os.getenv("TESTING_PASSWORD")

credentials = Credentials(username, password)

# Load Order Queues
order_queues = Order_Queues()

# Init Chrome Driver
options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--start-maximized")
options.add_argument("--kiosk")
driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH, options=options)

eToro = EToro(driver, credentials)

eToro.log_in()

if IS_VIRTUAL_PORTFOLIO:
	eToro.select_virtual_portfolio()

while True:

	if SHOULD_PERFORM_TRADE:

		ticker_to_close = order_queues.get_ticker_to_close()
		if ticker_to_close is not None:
  			eToro.close_position(ticker_to_close)

		ticker_to_open = order_queues.get_ticker_to_open()
		if ticker_to_open is not None:
			position = Position(ticker = ticker_to_open,
								amount = 100,
								stopLoss = -2,
								takeProfit = 0.5,
								isBuyingPosition = True)
			eToro.open_position(position)
