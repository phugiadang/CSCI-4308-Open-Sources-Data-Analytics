import json
import sys
from sys import argv
import operator
import queryCounts
from AnalysisObject import AnalysisObject
from cassandra.cluster import Cluster
import datetime
from calendar import monthrange
from GetPollsFromDatabase import DatabasePolls
#USAGE: python jsonize.py Twitter/GDELT CANDIDATE MONTH START_DAY END_DAY hourly/daily
#Enter one of the slashes (Twitter or GDELT, hourly or daily)
#Candidate name or all for all of them
#MONTH is the number for the month of start date (march would be 3)
#START_DAY is just number of day of month
#hourly/daily only applies if Twitter was chosen

def jsonizeFunc():
	datasource = argv[1]
	candidateRead = argv[2]
	monthNumber = int(argv[3])
	startDay = int(argv[4])
	endDay = int(argv[5])
	if datasource == "Twitter":
			timeframe = argv[6]


	#get month name from number
	month = datetime.date(1900, monthNumber, 1).strftime('%B')
	candidateNames = ['trump', 'clinton', 'sanders', 'cruz', 'rubio', 'kasich']
	if endDay > startDay:
			days = range(startDay, endDay + 1)
	else:
			days = range(startDay, monthrange(2016,monthNumber)[1]) + range(1, endDay + 1)
	hours = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
	datesHours = [] #empty list to be filled in with readable dates and times
	dates = []
	chartCaption = "Candidate " + datasource + "  Counts"
	chartSubCaption = ""

	dp = DatabasePolls(20160307, 20160308, 'Trump')
	dp.queryDatabase()
	dp.cleanPolls()
	pollData = dp.getCleanedPolls()



	def getTwitterObjects():
			candidateList = []
			for candidateName in candidateNames:
					thisCandidateCounts = queryCounts.candidateCountRangeDay(candidateName, monthNumber, days[0], 1, monthNumber, days[1], 1)
					#append 0's if missing data
					for i in range(len(thisCandidateCounts),47):
							thisCandidateCounts.append(0)
					candidate = AnalysisObject(candidateName, datasource, dates, thisCandidateCounts)
					candidateList.append(candidate)
			return candidateList


	def getGDELTObjects():
		candidateList = []
		for candidateName in candidateNames:
			candidateCounts = []
			for day in days:
				thisDayCount = queryCounts.candidateGDELTCount(candidateName, 2016, monthNumber, day)
				candidateCounts.append(thisDayCount)
				candidate = AnalysisObject(candidateName, datasource, [], candidateCounts)
				candidateList.append(candidate)
		return candidateList

	for day in days:
			for hour in hours:
					datesHours.append(month + ', ' + str(day) + ': ' + str(hour))
	for day in days:
			dates.append(month + ', ' + str(day))
	#print datesHours


	#candidateList = getTwitterObjects()
			#print candidateList

	if candidateRead == "all" and datasource == "GDELT":
			candidateList =  getGDELTObjects()
			
			jsonString = '''
			{
						"chart": {
							"caption": "'''
			jsonString += chartCaption
			jsonString +=           '''",
							"subCaption": "'''
			jsonString += chartSubCaption
			jsonString +=           '''",
							"captionFontSize": "14",
							"subcaptionFontSize": "14",
							"subcaptionFontBold": "0",
							"paletteColors": "#0075c2,#1aaf5d",
							"bgcolor": "#ffffff",
							"showBorder": "0",
							"showShadow": "0",
							"showCanvasBorder": "0",
							"usePlotGradientColor": "0",
							"legendBorderAlpha": "0",
							"legendShadow": "0",
							"showAxisLines": "0",
							"showAlternateHGridColor": "0",
							"divlineThickness": "1",
							"divLineIsDashed": "1",
							"divLineDashLen": "1",
							"divLineGapLen": "1",
							"xAxisName": "Day",
							"showValues": "0"               
						},
						"categories": [
							{
								"category": ['''
			for i in range(0,len(dates)-1):
					jsonString += '{ "label": "' + dates[i] + '" },'
			jsonString += '{ "label": "' + dates[len(dates)-1] + '" }'
			jsonString += '''
								]
							}
						],
						"dataset": ['''
			for i in range (0, len(candidateList)-1):
					jsonString += str(candidateList[i].createJson())
					jsonString += ','
			jsonString += str(candidateList[len(candidateList)-1].createJson())

			jsonString +=  '''      
						], 
						"trendlines": [
							{
								"line": [
									{
										"startvalue": "17022",
										"color": "#6baa01",
										"valueOnRight": "1",
										"displayvalue": "Average"
									}
								]
							}
						]
					}
			'''
			f = open('GDELTAll.json', 'w')
			f.write(jsonString)

	elif candidateRead == "all" and datasource == "Twitter":
			if timeframe == "hourly":
					candidateList = getTwitterObjects()
			
			jsonString = '''
			{
						"chart": {
							"caption": "'''
			jsonString += chartCaption
			jsonString +=           '''",
							"subCaption": "'''
			jsonString += chartSubCaption
			jsonString +=           '''",
							"captionFontSize": "14",
							"subcaptionFontSize": "14",
							"subcaptionFontBold": "0",
							"paletteColors": "#0075c2,#1aaf5d",
							"bgcolor": "#ffffff",
							"showBorder": "0",
							"showShadow": "0",
							"showCanvasBorder": "0",
							"usePlotGradientColor": "0",
							"legendBorderAlpha": "0",
							"legendShadow": "0",
							"showAxisLines": "0",
							"showAlternateHGridColor": "0",
							"divlineThickness": "1",
							"divLineIsDashed": "1",
							"divLineDashLen": "1",
							"divLineGapLen": "1",
							"xAxisName": "Day",
							"showValues": "0"               
						},
						"categories": [
							{
								"category": ['''
			for i in range(0,len(dates)-1):
					for j in range(0,len(hours)-1):
						jsonString += '{ "label": "' + dates[i] + ' ' + str(hours[j]) + ':00" },'

					jsonString += '{ "label": "' + dates[i] + ' ' + str(hours[len(hours)-1]) + ':00" },'
			for j in range(0, len(hours)-1):
					jsonString += '{ "label": "' + dates[len(dates)-1] + ' ' + str(hours[j]) + ':00" },'

			jsonString += '{ "label": "' + dates[len(dates)-1] + ' ' + str(hours[len(hours)-1]) + ':00" }'
			jsonString += '''
								]
							}
						],
						"dataset": ['''
			for i in range (0, len(candidateList)-1):
					jsonString += str(candidateList[i].createJson())
					jsonString += ','
			jsonString += str(candidateList[len(candidateList)-1].createJson())

			jsonString +=  '''      
						], 
						"trendlines": [
							{
								"line": [
									{
										"startvalue": "17022",
										"color": "#6baa01",
										"valueOnRight": "1",
										"displayvalue": "Average"
									}
								]
							}
						]
					}
				'''
			f = open('TwitterAll.json', 'w')
			f.write(jsonString)

	if candidateRead == "all" and datasource == "Polls":
			startDate = ""
			endDate = ""
			pollDays = []
			if len(str(startDay)) < 2:
					startDate = "20160" + str(monthNumber) + "0" + str(startDay)
			if len(str(endDay)) < 2:
					endDate = "20160" + str(monthNumber) + "0" + str(endDay) 
			for day in days:
					if len(str(day)) < 2:
							pollDays.append("20160" + str(monthNumber) + "0" + str(day))
			for candidate in candidateNames:
					dp = DatabasePolls(startDate, endDate, candidate.title())
					dp.queryDatabase()
					dp.cleanPolls()
					pollData = dp.getCleanedPolls()
					for poll in pollData:
							print poll


        
