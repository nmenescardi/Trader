
-- DROP DATABASE IF EXISTS trader;

CREATE DATABASE IF NOT EXISTS trader;
USE trader;


CREATE TABLE IF NOT EXISTS stocks (
	stock_id INT AUTO_INCREMENT PRIMARY KEY,
	ticker VARCHAR(20) NOT NULL,
	company VARCHAR(255) NULL DEFAULT NULL,
	exchanger VARCHAR(20) NULL DEFAULT NULL,
	description VARCHAR(255),
	created_date DATETIME NULL DEFAULT CURRENT_TIMESTAMP(),
	last_updated DATETIME NULL DEFAULT CURRENT_TIMESTAMP() ON UPDATE CURRENT_TIMESTAMP(),
	UNIQUE KEY stocks_ticker_company (ticker, company)
);


CREATE TABLE IF NOT EXISTS etoro_stocks (
	etoro_stock_id INT AUTO_INCREMENT PRIMARY KEY,
	stock_id INT,
	ticker VARCHAR(20) NOT NULL,
	company VARCHAR(255) NULL DEFAULT NULL,
	exchanger VARCHAR(20) NULL DEFAULT NULL,
	url VARCHAR(255) NULL DEFAULT NULL,
	is_manual_tp BOOLEAN NOT NULL DEFAULT FALSE,
	created_date DATETIME NULL DEFAULT CURRENT_TIMESTAMP(),
	last_updated DATETIME NULL DEFAULT CURRENT_TIMESTAMP() ON UPDATE CURRENT_TIMESTAMP(),
	FOREIGN KEY (stock_id) REFERENCES stocks (stock_id)
);


CREATE TABLE IF NOT EXISTS indicators (
	indicator_id INT AUTO_INCREMENT PRIMARY KEY,
	stock_id INT,
	indicator_key VARCHAR(255) NOT NULL,
	indicator_value VARCHAR(255) NULL DEFAULT NULL,
	main_timeframe VARCHAR(5) NULL DEFAULT NULL,
	date_time DATETIME NULL DEFAULT CURRENT_TIMESTAMP(),
	created_date DATETIME NULL DEFAULT CURRENT_TIMESTAMP(),
	last_updated DATETIME NULL DEFAULT CURRENT_TIMESTAMP() ON UPDATE CURRENT_TIMESTAMP(),
	FOREIGN KEY (stock_id) REFERENCES stocks (stock_id)
);


CREATE TABLE IF NOT EXISTS lists (
	list_id INT AUTO_INCREMENT PRIMARY KEY,
	title VARCHAR(255) NOT NULL,
	description VARCHAR(255) NULL DEFAULT NULL,
	created_date DATETIME NULL DEFAULT CURRENT_TIMESTAMP(),
	last_updated DATETIME NULL DEFAULT CURRENT_TIMESTAMP() ON UPDATE CURRENT_TIMESTAMP()
);


CREATE TABLE IF NOT EXISTS stock_list (
	stock_id INT,
	list_id INT,
	created_date DATETIME NULL DEFAULT CURRENT_TIMESTAMP(),
	last_updated DATETIME NULL DEFAULT CURRENT_TIMESTAMP() ON UPDATE CURRENT_TIMESTAMP(),
	FOREIGN KEY (stock_id) REFERENCES stocks (stock_id),
	FOREIGN KEY (list_id) REFERENCES lists (list_id),
	PRIMARY KEY (stock_id, list_id)
);


CREATE TABLE IF NOT EXISTS stock_prices (
	stock_price_id INT AUTO_INCREMENT PRIMARY KEY,
	stock_id INT,
	time_price DATETIME NOT NULL,
	open_price DECIMAL(11,6) NULL DEFAULT NULL,
	high_price DECIMAL(11,6) NULL DEFAULT NULL,
	low_price DECIMAL(11,6) NULL DEFAULT NULL,
	close_price DECIMAL(11,6) NULL DEFAULT NULL,
	volume BIGINT(20) NULL DEFAULT NULL,
	timeframe VARCHAR(5) NULL DEFAULT "5m",
	created_date DATETIME NULL DEFAULT CURRENT_TIMESTAMP(),
	last_updated DATETIME NULL DEFAULT CURRENT_TIMESTAMP() ON UPDATE CURRENT_TIMESTAMP(),
	UNIQUE KEY historical_price_stock_time (stock_id, time_price),
	FOREIGN KEY (stock_id) REFERENCES stocks (stock_id)
);


CREATE TABLE IF NOT EXISTS strategies (
	strategy_id INT AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(5) NULL DEFAULT NULL,
	version VARCHAR(5) NULL DEFAULT NULL,
	type VARCHAR(5) NULL DEFAULT NULL,
	created_date DATETIME NULL DEFAULT CURRENT_TIMESTAMP(),
	last_updated DATETIME NULL DEFAULT CURRENT_TIMESTAMP() ON UPDATE CURRENT_TIMESTAMP()
);


CREATE TABLE IF NOT EXISTS backtest_schedules (
	backtest_schedule_id INT AUTO_INCREMENT PRIMARY KEY,
	list_id INT,
	strategy_id INT,
	from_date DATETIME NOT NULL,
	to_date DATETIME NULL DEFAULT CURRENT_TIMESTAMP(),
	timeframe VARCHAR(5) NULL DEFAULT NULL,
	frecuency VARCHAR(5) NULL DEFAULT NULL,
	created_date DATETIME NULL DEFAULT CURRENT_TIMESTAMP(),
	last_updated DATETIME NULL DEFAULT CURRENT_TIMESTAMP() ON UPDATE CURRENT_TIMESTAMP(),
	FOREIGN KEY (list_id) REFERENCES lists (list_id),
	FOREIGN KEY (strategy_id) REFERENCES strategies (strategy_id)
);


CREATE TABLE IF NOT EXISTS backtest_reports (
	backtest_report_id INT AUTO_INCREMENT PRIMARY KEY,
	stock_id INT,
	backtest_schedule_id INT NULL DEFAULT NULL,
	strategy_id INT,
	from_date DATETIME NOT NULL,
	to_date DATETIME NULL DEFAULT CURRENT_TIMESTAMP(),
	main_timeframe VARCHAR(5) NULL DEFAULT NULL,
	tag VARCHAR(100) NULL DEFAULT NULL,
	created_date DATETIME NULL DEFAULT CURRENT_TIMESTAMP(),
	last_updated DATETIME NULL DEFAULT CURRENT_TIMESTAMP() ON UPDATE CURRENT_TIMESTAMP(),
	FOREIGN KEY (stock_id) REFERENCES stocks (stock_id),
	FOREIGN KEY (backtest_schedule_id) REFERENCES backtest_schedules (backtest_schedule_id),
	FOREIGN KEY (strategy_id) REFERENCES strategies (strategy_id)
);


CREATE TABLE IF NOT EXISTS report_meta (
	report_meta_id INT AUTO_INCREMENT PRIMARY KEY,
	backtest_report_id INT,
	meta_key VARCHAR(255) NOT NULL,
	meta_value VARCHAR(255) NULL DEFAULT NULL,
	created_date DATETIME NULL DEFAULT CURRENT_TIMESTAMP(),
	last_updated DATETIME NULL DEFAULT CURRENT_TIMESTAMP() ON UPDATE CURRENT_TIMESTAMP(),
	FOREIGN KEY (backtest_report_id) REFERENCES backtest_reports (backtest_report_id)
);


CREATE TABLE IF NOT EXISTS general_config (
	last_portfolio_positions_update DATETIME NULL DEFAULT CURRENT_TIMESTAMP(),
	should_reset BOOLEAN NOT NULL DEFAULT FALSE,
	last_updated DATETIME NULL DEFAULT CURRENT_TIMESTAMP() ON UPDATE CURRENT_TIMESTAMP()
);


-- *********************************
-- Insert Default Values
-- *********************************

-- Some pass value to force checking the portfolio amount
INSERT INTO general_config (last_portfolio_positions_update)
SELECT subdate(CURRENT_DATE, 5) FROM DUAL
WHERE NOT EXISTS (SELECT * FROM general_config);


-- *********************************
-- Insert Testing Data
-- *********************************
-- UPDATE general_config SET last_portfolio_positions_update = subdate(CURRENT_DATE, 5)

INSERT IGNORE INTO stocks 
	(ticker, company, exchanger)
VALUES 
	('AAPL','Apple Inc','NASDAQ'),  
	('NIO','NIO Inc','NYSE')
;


INSERT IGNORE INTO stock_prices 
	(stock_id, time_price, open_price, high_price, low_price, close_price, volume, timeframe)
VALUES 
	(1,'2018-11-14 09:30','47.437','47.476','47.403','47.466','123164','5m'),
	(8,'2018-11-14 09:30','47.437','47.476','47.403','47.466','123164','5m'),
	(1,'2018-11-14 09:35','47.437','47.476','47.403','47.466','123164','5m')
;

