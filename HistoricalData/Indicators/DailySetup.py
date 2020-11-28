from HistoricalData.Indicators.SMA import SMA
from HistoricalData.Indicators.Is_Above_SMAs import Is_Above_SMAs
from HistoricalData.Indicators.Is_Trending_Above_SMAs import Is_Trending_Above_SMAs
from HistoricalData.Indicators.RSI import RSI

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

		Is_Trending_Above_SMAs : [
			{ 'fast_MA': '20', 'med_MA': '50', 'slow_MA': '200' },
		],

		RSI : [
			{ 'period': '2' },
			{ 'period': '14' },
		],

		
	}
