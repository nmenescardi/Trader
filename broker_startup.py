from selenium import webdriver
import os
from dotenv import load_dotenv
from distutils.util import strtobool
from Models.Position import Position
from Models.Credentials import Credentials
from Brokers.EToro import EToro
from Order_Queues.Order_Queues import Order_Queues
from Logger import Logger

# Load Env variables:
load_dotenv()

CHROME_DRIVER_PATH = os.getenv("CHROME_DRIVER_PATH")
IS_PRODUCTION_MODE_SET = bool(strtobool(os.getenv("IS_PRODUCTION_MODE_SET")))
SHOULD_PERFORM_TRADE = bool(strtobool(os.getenv("SHOULD_PERFORM_TRADE")))
IS_VIRTUAL_PORTFOLIO = bool(strtobool(os.getenv("IS_VIRTUAL_PORTFOLIO")))
SHOULD_OPEN_SINGLE_POSITION = bool(strtobool(os.getenv("SHOULD_OPEN_SINGLE_POSITION")))

if IS_PRODUCTION_MODE_SET:
	username = os.getenv("PRODUCTION_USERNAME")
	password = os.getenv("PRODUCTION_PASSWORD")
else:
	username = os.getenv("TESTING_USERNAME")
	password = os.getenv("TESTING_PASSWORD")

credentials = Credentials(username, password)

# Load Logger
logger = Logger().get_logger()

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
		eToro = EToro(driver, credentials, logger, IS_VIRTUAL_PORTFOLIO, SHOULD_OPEN_SINGLE_POSITION)
		eToro.init()

		while True:
			if SHOULD_PERFORM_TRADE:

				ticker_to_close = order_queues.get_ticker_to_close()
				if ticker_to_close is not None:
					logger.info('0001 - Ticker to Close: {}'.format(ticker_to_close))
					is_close = eToro.close_position(ticker_to_close)
					if is_close:
						order_queues.remove_ticker_from_close()
						logger.info('0002 - {} was successfully closed'.format(ticker_to_close))
					else:
						logger.info('0003 - Error trying to close position for: {}'.format(ticker_to_close))

				position = order_queues.get_position_to_open()
				if position is not None:
					logger.info('0004 - Ticker to Open: {}'.format(position.ticker))
     
					is_open = eToro.open_position(position)
					if is_open:
						order_queues.remove_position_from_open()
						logger.info('0005 - {} was successfully opened'.format(position.ticker))
					else:
						logger.info('0006 - Error trying to open a position for: {}'.format(position.ticker))

	except Exception as e:
		logger.exception('0007 - Exception trying to open a position')
		driver.quit()
  
while True:
	try:
		open_session()
	except Exception as e:
		logger.exception('0008 - Exception trying to open a position')
		pass
 
