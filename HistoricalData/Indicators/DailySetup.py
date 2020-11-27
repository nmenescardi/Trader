from HistoricalData.Indicators.SMA import SMA
from HistoricalData.Indicators.RSI import RSI
from HistoricalData.Indicators.Is_Above_SMAs import Is_Above_SMAs

class DailySetup():
	
	config = {

		SMA : [
			{ 'period': '20' },
			{ 'period': '50' },
			{ 'period': '120' },
			{ 'period': '200' },
		],

		Is_Above_SMAs : [
			{ 'periods': ['50', '200'] },
			{ 'periods': ['20', '50', '120', '200'] },
		],

		RSI : [
			{ 'period': '2' },
			{ 'period': '14' },
		],

		
	}
