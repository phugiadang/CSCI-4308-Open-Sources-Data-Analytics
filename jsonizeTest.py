from jsonize import jsonize
from types import *

jsonizer = jsonize()

days = ['from 20160213000000 to 20160213010000', 'from 20160213010000 to 20160213020000', 'from 20160213020000 to 20160213030000', 'from 20160213030000 to 20160213040000', 'from 20160213040000 to 20160213050000', 'from 20160213050000 to 20160213060000', 'from 20160213060000 to 20160213070000', 'from 20160213070000 to 20160213080000', 'from 20160213080000 to 20160213090000', 'from 20160213090000 to 20160213100000', 'from 20160213100000 to 20160213110000', 'from 20160213110000 to 20160213120000', 'from 20160213120000 to 20160213130000', 'from 20160213130000 to 20160213140000', 'from 20160213140000 to 20160213150000', 'from 20160213150000 to 20160213160000', 'from 20160213160000 to 20160213170000', 'from 20160213170000 to 20160213180000', 'from 20160213180000 to 20160213190000', 'from 20160213190000 to 20160213200000', 'from 20160213200000 to 20160213210000', 'from 20160213210000 to 20160213220000', 'from 20160213220000 to 20160213230000', 'from 20160213230000 to 20160214000000']

counts = ['0', '0', '0', '0', '0', '952', '5630', '4228', '3361', '3086', '2735', '4267', '4751', '6239', '7852', '8901', '10201', '9896', '10367', '9656', '10099', '10451', '13129', '11405']

string = '''
	{
          "chart": {
            "caption": "Sanders Tweets",
            "subCaption": "Counts",
            "xAxisName": "Day",
            "yAxisName": "Count",
          
          
            "lineThickness" : "2",
            "paletteColors" : "#0075c2",
            "baseFontColor" : "#333333",
            "baseFont" : "Helvetica Neue,Arial",
            "captionFontSize" : "14",
            "subcaptionFontSize" : "14",
            "subcaptionFontBold" : "0",
            "showBorder" : "0",
            "bgColor" : "#ffffff",
            "showShadow" : "0",
            "canvasBgColor" : "#ffffff",
            "canvasBorderAlpha" : "0",
            "divlineAlpha" : "100",
            "divlineColor" : "#999999",
            "divlineThickness" : "1",
            "divLineIsDashed" : "1",
            "divLineDashLen" : "1",
            "divLineGapLen" : "1",
            "showXAxisLine" : "1",
            "xAxisLineThickness" : "1",
            "xAxisLineColor" : "#999999",
            "showAlternateHGridColor" : "0"
          },

          "data": [
		{"label": "from 20160213000000 to 20160213010000", "value": "0"},
		{"label": "from 20160213010000 to 20160213020000", "value": "0"},
		{"label": "from 20160213020000 to 20160213030000", "value": "0"},
		{"label": "from 20160213030000 to 20160213040000", "value": "0"},
		{"label": "from 20160213040000 to 20160213050000", "value": "0"},
		{"label": "from 20160213050000 to 20160213060000", "value": "952"},
		{"label": "from 20160213060000 to 20160213070000", "value": "5630"},
		{"label": "from 20160213070000 to 20160213080000", "value": "4228"},
		{"label": "from 20160213080000 to 20160213090000", "value": "3361"},
		{"label": "from 20160213090000 to 20160213100000", "value": "3086"},
		{"label": "from 20160213100000 to 20160213110000", "value": "2735"},
		{"label": "from 20160213110000 to 20160213120000", "value": "4267"},
		{"label": "from 20160213120000 to 20160213130000", "value": "4751"},
		{"label": "from 20160213130000 to 20160213140000", "value": "6239"},
		{"label": "from 20160213140000 to 20160213150000", "value": "7852"},
		{"label": "from 20160213150000 to 20160213160000", "value": "8901"},
		{"label": "from 20160213160000 to 20160213170000", "value": "10201"},
		{"label": "from 20160213170000 to 20160213180000", "value": "9896"},
		{"label": "from 20160213180000 to 20160213190000", "value": "10367"},
		{"label": "from 20160213190000 to 20160213200000", "value": "9656"},
		{"label": "from 20160213200000 to 20160213210000", "value": "10099"},
		{"label": "from 20160213210000 to 20160213220000", "value": "10451"},
		{"label": "from 20160213220000 to 20160213230000", "value": "13129"},
               {"label": "from 20160213230000 to 20160214000000", "value": "11405"}
          ]}'''

assert type(jsonizer.makeJson("Sanders", days, counts)) is StringType, "jsoinzer is not a string" 
assert jsonizer.makeJson("Sanders", days, counts) == string, "jsonizer doesn't match given string"
