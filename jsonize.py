import json
import sys

class jsonize():

    def __init__(self):
        return

    #Date formatted: "Jan 23", "Feb 2" etc..
    def makeJson(self, candidate, days, counts):
	str = '''
	{
          "chart": {
            "caption": "''' + candidate + ''' Tweets",
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
'''
	for i in range(0,len(days)-1):
	  str += '		{"label": "' + days[i] + '", "value": "' + counts[i] + '"},\n'
	str += '               {"label": "' + days[len(days)-1] + '", "value": "' + counts[len(days)-1] + '"}\n'
        str += '          ]}'
	return str
 
