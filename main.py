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


def open_session():
	# Init Chrome Driver
	options = webdriver.ChromeOptions()
	options.add_argument("--disable-blink-features")
	options.add_argument("--disable-blink-features=AutomationControlled")
	options.add_argument("--start-maximized")
	options.add_argument("--kiosk")
	driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH, options=options)

	try:
		eToro = EToro(driver, credentials, IS_VIRTUAL_PORTFOLIO)
		eToro.init()

		while True:
			if SHOULD_PERFORM_TRADE:

				ticker_to_close = order_queues.get_ticker_to_close()
				if ticker_to_close is not None:
					print('Ticker to Close: {}'.format(ticker_to_close))
					is_close = eToro.close_position(ticker_to_close)
					if is_close:
						order_queues.remove_ticker_from_close()

				ticker_to_open = order_queues.get_ticker_to_open()
				if ticker_to_open is not None:
					print('Ticker to Open: {}'.format(ticker_to_open))
					position = Position(ticker = ticker_to_open.lower(),
										amount = 100,
										stopLoss = -10,
										takeProfit = 10,
										isBuyingPosition = True)
					is_open = eToro.open_position(position)
					if is_open:
						order_queues.remove_ticker_from_open()
      
	except Exception as e:
		print('Exception {}'.format(e))
		driver.quit()
  
while True:
	try:
		open_session()
	except Exception as e:
		print('Exception {}'.format(e))
		pass
 
