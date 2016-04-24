import json
import sys
from sys import argv
import operator
import QueryingDavid
from AnalysisObject import AnalysisObject
from cassandra.cluster import Cluster
import time
import datetime
from calendar import monthrange
from GetPollsFromDatabase import DatabasePolls
from RegressionReadyPolls import RegressionReadyPolls
import matplotlib
#USAGE: python jsonize.py Twitter/GDELT CANDIDATE MONTH START_DAY END_DAY hourly/daily
#Enter one of the slashes (Twitter or GDELT, hourly or daily)
#Candidate name or all for all of them
#MONTH is the number for the month of the end date (march would be 3)
#START_DAY is just number of day of month
#hourly/daily only applies if Twitter was chosen


datasource = argv[1]
candidate_read = argv[2]
month_end_number = int(argv[3])
start_day = int(argv[4])
end_day = int(argv[5])
if datasource == "Twitter":
	timeframe = argv[6]




def getTwitterObjectsHourly():
	candidate_list = []
	for candidate_name in candidate_names:
		this_candidate_counts = QueryingDavid.candidateCountRangeDay(candidate_name, month_start_number, days[0], current_hour, month_end_number, days[len(days)-1], current_hour)
		#append 0's if missing data MAY BE ONE TOO MANY
		for i in range(len(this_candidate_counts),len(days)*24):
			this_candidate_counts.append(0)
		candidate = AnalysisObject(candidate_name, datasource, dates, this_candidate_counts)
		candidate_list.append(candidate)
	return candidate_list


def getTwitterObjectCandidate(candidate_name):
	this_candidate_counts = QueryingDavid.candidateCountRangeDayFull(candidate_name.lower(), month_start_number, days[0], 1, month_end_number, days[len(days)-1], 1)
	print len(this_candidate_counts)
	print this_candidate_counts
	#append 0's if missing data THIS MAY NOT WORK, MAY BE ONE TOO MANY
	return AnalysisObject(candidate_name, datasource, dates, this_candidate_counts[0:len(days)])


def getGDELTObjects():
	candidate_list = []
	for candidate_name in candidate_names:
		candidate_counts = []
		for day in days:
			if day >= end_day:
				this_day_count = QueryingDavid.candidateGDELTCount(candidate_name, 2016, month_start_number, day)
			else:
				this_day_count = QueryingDavid.candidateGDELTCount(candidate_name, 2016, month_end_number, day)
			#for row in this_day_count:
				#print "u"
				#print "count is " +  str(row.count)
			candidate_counts.append(this_day_count[0][1])
		candidate = AnalysisObject(candidate_name, datasource, [], candidate_counts)
		candidate_list.append(candidate)

	return candidate_list



def getGDELTObjectCandidate(candidate_name):
	candidate_counts = []
	for day in days:
		if day >= end_day:
			this_day_count = QueryingDavid.candidateGDELTCount(candidate_name, 2016, month_start_number, day)
		else:
			this_day_count = QueryingDavid.candidateGDELTCount(candidate_name, 2016, month_end_number, day)
		candidate_counts.append(this_day_count[0][1])
	return  AnalysisObject(candidate_name, "GDELT", [], candidate_counts)

def getPollObjectCandidate(candidate_name):
	start_date = ""
	end_date = ""
	poll_days = []
	for day in days:
		if len(str(day)) < 2:
			#first month
			if day > end_day:
				poll_days.append("20160" + str(month_start_number) + "0" + str(day))
			#end month
			else:
				poll_days.append("20160" + str(month_end_number) + "0" + str(day))
		else:
			#first month
			if day > end_day:
				poll_days.append("20160" + str(month_start_number) + str(day))
			#end month
			else:
				poll_days.append("20160" + str(month_end_number) + str(day))
	poll_days_copy = poll_days[:]
	print poll_days_copy
	dp = DatabasePolls(poll_days_copy[0], poll_days_copy[len(poll_days_copy)-1], [candidate_name.capitalize()])
	dp.queryDatabase()
	dp.cleanPolls()
	poll_data = dp.getCleanedPolls()
	
	rrp = RegressionReadyPolls(poll_data, candidate_name.capitalize(), poll_days_copy[0], poll_days_copy[len(poll_days_copy)-1])
	rrp.makeSimplePollNumbers()
	rrp.fillGapsWithAvg()
	return AnalysisObject(candidate_name, "Polls", [], rrp.getPollNumbers())
	
def getPollObjectCandidate1(candidate_name):
	start_date = ""
	end_date = ""
	poll_days = []
	for day in days:
		if len(str(day)) < 2:
			#first month
			if day > end_day:
				poll_days.append("20160" + str(month_start_number) + "0" + str(day))
			#end month
			else:
				poll_days.append("20160" + str(month_end_number) + "0" + str(day))
		else:
			#first month
			if day > end_day:
				poll_days.append("20160" + str(month_start_number) + str(day))
			#end month
			else:
				poll_days.append("20160" + str(month_end_number) + str(day))
	poll_days_copy = poll_days[:]
	dp = DatabasePolls(poll_days_copy[0], poll_days_copy[len(poll_days_copy)-1], candidate_name.title())
	dp.queryDatabase()
	dp.cleanPolls()
	poll_data = dp.getCleanedPolls()
	list_of_data = []
	while poll_days_copy:
		still_searching = True
		does_exist = False
		for poll in poll_data:
			if poll[0] == int(poll_days_copy[0]) and still_searching == True:
				i = 0
				does_exist = False
				for candidateInPoll in poll[1]:
					if candidateInPoll == candidate_name.title():
						does_exist = True
						list_of_data.append(poll[2][i])
					i += 1
				still_searching = False
		if does_exist == False:
			list_of_data.append("None")	

		poll_days_copy.remove(poll_days_copy[0])


	return AnalysisObject(candidate_name, "Polls", [], list_of_data)


current_hour = 01

#get todays date and set start_date
if month_end_number == 0:
	date = time.strftime("%d,%m,%y")
	current_time = datetime.datetime.now()
	
	current_hour = str(current_time)[11:13]
	end_day = int(date[0:2]) - 1
	month_end_number = int(date[3:5])
	start_day = end_day - 2


if start_day > end_day:
	month_start_number = month_end_number - 1
else:
	month_start_number = month_end_number
#get month name from number
month_end = datetime.date(1900, month_end_number, 1).strftime('%B')
month_start = datetime.date(1900, month_start_number, 1).strftime('%B')
#candidate_names = ['trump', 'clinton', 'sanders', 'cruz', 'rubio', 'kasich']
candidate_names = ['trump', 'clinton', 'sanders', 'cruz',  'kasich']

if end_day > start_day:
	days = range(start_day, end_day + 1)
else:
	days = range(start_day, monthrange(2016,month_start_number)[1] + 1) + range(1, end_day + 1)

#hours adjusted from GMT to MST
hours = ["19","20","21","22","23","00","01","02","03","04","05","06","07","08","09", "10", "11","12","13","14","15","16","17","18"]
dates_hours = [] #empty list to be filled in with readable dates and times
dates = []
chart_caption = "Candidate " + datasource + "  Counts"
chart_sub_caption = ""


#FIX TO MAKE HOURS START FROM CURRENT HOUR
for day in days:
	#first month
	if day > end_day:
		for hour in hours:
			dates_hours.append(month_start + ', ' + str(day) + ': ' + str(hour))
	else:
		for hour in hours:
			dates_hours.append(month_end + ', ' + str(day) + ': ' + str(hour))

for day in days:
	#first month
	if day > end_day:
		dates.append(month_start + ', ' + str(day))
	else:
		dates.append(month_end + ', ' + str(day))

if candidate_read == "all" and datasource == "GDELT":
	candidate_list =  getGDELTObjects()
	json_string = '''
	{
		    "chart": {
			"caption": "'''
	json_string += chart_caption
	json_string +=		'''",
			"subCaption": "'''
	json_string += chart_sub_caption
	json_string +=		'''",
			"captionFontSize": "14",
			"subcaptionFontSize": "14",
			"subcaptionFontBold": "0",
			"paletteColors": "#FF0000,#0000FF,#000033,#9D1309,#FF6A6A,#330000",
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
			"showValues": "0",
			"showRealTimeValue": "0",
			"refreshinterval": "86400",
			"datastreamurl": "../FrontEnd/NGC-FrontEnd/public/GDELTAll.json"
		    },
		    "categories": [
			{
			    "category": ['''
	for i in range(0,len(dates)-1):
		json_string += '{ "label": "' + dates[i] + '" },'
	json_string += '{ "label": "' + dates[len(dates)-1] + '" }'
	json_string += '''
			    ]
			}
		    ],
		    "dataset": ['''
	for i in range (0, len(candidate_list)-1):
		json_string += str(candidate_list[i].createJson())
		json_string += ','
	json_string += str(candidate_list[len(candidate_list)-1].createJson())

	json_string +=  '''
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
	f = open('../FrontEnd/NGC-FrontEnd/public/GDELTAll.json', 'w')
	f.write(json_string)


	print candidate_list
elif candidate_read == "all" and datasource == "Twitter" and timeframe == "hourly":
	candidate_list = getTwitterObjectsHourly()

	json_string = '''
	{
		    "chart": {
			"caption": "'''
	json_string += chart_caption
	json_string +=		'''",
			"subCaption": "'''
	json_string += chart_sub_caption
	json_string +=		'''",
			"captionFontSize": "14",
			"subcaptionFontSize": "14",
			"subcaptionFontBold": "0",
			"paletteColors": "#FF0000,#0000FF,#000033,#9D1309,#FF6A6A,#330000",
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
			"showValues": "0",
			"datastreamurl": "../FrontEnd/NGC-FrontEnd/public/TwitterAll.json"
		    },
		    "categories": [
			{
			    "category": ['''
	k = 0
	for i in range(0,len(dates)-1):
		for j in range(0,len(hours)-1):
			if k % 3 == 0:
				json_string += '{ "label": "' + dates[i] + ' ' + str(hours[j]) + ':00" },'
			else:
				json_string += '{ "label": "" },'
			k += 1
		#json_string += '{ "label": "' + dates[i] + ' ' + str(hours[len(hours)-1]) + ':00" },'
		json_string += '{ "label": "" },'
		k += 1
	for j in range(0, len(hours)-1):
		if k % 3 == 0:
			json_string += '{ "label": "' + dates[len(dates)-1] + ' ' + str(hours[j]) + ':00" },'
		else:
			json_string += '{ "label": "" },'
		k += 1
	#json_string += '{ "label": "' + dates[len(dates)-1] + ' ' + str(hours[len(hours)-1]) + ':00" }'
	json_string += '{ "label": "" }'
	json_string += '''
			    ]
			}
		    ],
		    "dataset": ['''
	for i in range (0, len(candidate_list)-1):
		json_string += str(candidate_list[i].createJson())
		json_string += ','
	json_string += str(candidate_list[len(candidate_list)-1].createJson())

	json_string +=  '''
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
	f = open('../FrontEnd/NGC-FrontEnd/public/TwitterAll.json', 'w')
	f.write(json_string)
elif candidate_read == "all" and datasource == "Twitter" and timeframe == "daily":
	candidate_list = []
	for candidate in candidate_names:
		candidate_list.append(getTwitterObjectCandidate(candidate))
	json_string = '''
	{
		    "chart": {
			"caption": "'''
	json_string += chart_caption
	json_string +=		'''",
			"subCaption": "'''
	json_string += chart_sub_caption
	json_string +=		'''",
			"captionFontSize": "14",
			"subcaptionFontSize": "14",
			"subcaptionFontBold": "0",
			"paletteColors": "#FF0000,#0000FF,#000033,#9D1309,#FF6A6A,#330000",
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
		json_string += '{ "label": "' + dates[i] + '" },'
	json_string += '{ "label": "' + dates[len(dates)-1] + '" }'
	json_string += '''
			    ]
			}
		    ],
		    "dataset": ['''
	for i in range (0, len(candidate_list)-1):
		json_string += str(candidate_list[i].createJson())
		json_string += ','
	json_string += str(candidate_list[len(candidate_list)-1].createJson())

	json_string +=  '''
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

	f = open('../FrontEnd/NGC-FrontEnd/public/TwitterAllDaily.json', 'w')
	#f = open('PollsAll.json', 'w')
	f.write(json_string)

elif candidate_read == "all" and datasource == "Polls":
	candidate_list = []
	for candidate_name in candidate_names:
		print "going in with " + str(candidate_name.title())
		candidate_list.append(getPollObjectCandidate(candidate_name.title()))
	print candidate_list
	json_string = '''
	{
		    "chart": {
			"caption": "'''
	json_string += chart_caption
	json_string +=		'''",
			"subCaption": "'''
	json_string += chart_sub_caption
	json_string +=		'''",
			"captionFontSize": "14",
			"subcaptionFontSize": "14",
			"subcaptionFontBold": "0",
			"paletteColors": "#FF0000,#0000FF,#000033,#9D1309,#FF6A6A,#330000",
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
		json_string += '{ "label": "' + dates[i] + '" },'
	json_string += '{ "label": "' + dates[len(dates)-1] + '" }'
	json_string += '''
			    ]
			}
		    ],
		    "dataset": ['''
	for i in range (0, len(candidate_list)-1):
		json_string += str(candidate_list[i].createJson())
		json_string += ','
	json_string += str(candidate_list[len(candidate_list)-1].createJson())

	json_string +=  '''
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

	f = open('../FrontEnd/NGC-FrontEnd/public/PollsAll.json', 'w')
	#f = open('PollsAll.json', 'w')
	f.write(json_string)

elif datasource == "all":
	candidate_polls = getPollObjectCandidate(candidate_read)
	candidate_gdelt = getGDELTObjectCandidate(candidate_read)
	candidate_twitter = getTwitterObjectCandidate(candidate_read) #need daily not hourly
	json_string = '''
{
    "chart": {
        "caption": "''' + candidate_read + ''' Counts",
        "xaxisname": "Days",
        "showvalues": "0",
        "divlinealpha": "100",
        "vdivlinealpha": "0",
        "showborder": "0",
        "bgcolor": "FFFFFF",
        "showalternatehgridcolor": "0",
        "labeldisplay": "WRAP",
        "divlinecolor": "CCCCCC",
        "showcanvasborder": "0",
        "showshadow": "0",
        "linethickness": "3",
        "legendshadow": "0",
        "legendborderalpha": "50"
    },
    "categories": [
        {
	    "category": ['''
	for i in range(0,len(dates)-1):
		json_string += '{ "label": "' + dates[i] + '" },'
	json_string += '{ "label": "' + dates[len(dates)-1] + '" }'
	json_string += '''
			    ]
        }
    ],
    "axis": [
        {
            "title": "Twitter",
            "titlepos": "left",
            "tickwidth": "10",
            "divlineisdashed": "1",
            "color": "008ee4",
            "dataset": [
                {
                    "seriesname": "Tweets",
                    "data": ['''
	for i in range (0,len(dates)-1):
		json_string += '{ "value": "' + str(candidate_twitter.getlist_para_two()[i]) + '" },'
	json_string += '{ "value": "' + str(candidate_twitter.getlist_para_two()[len(dates)-1]) + '" }'
	json_string += '''
                    ]
                }
            ]
        },
        {
            "title": "Polls",
            "titlepos": "right",
            "numdivlines": "14",
            "tickwidth": "10",
	    "axisonleft": "0",
            "sdivlineisdashed": "1",
            "color": "f8bd19",
            "divlinealpha": "30",
            "dataset": [
                {
                    "seriesname": "Poll Percentage",
                    "data": ['''
	for i in range (0,len(candidate_polls.getlist_para_two())-1):
		json_string += '{ "value": "' + str(candidate_polls.getlist_para_two()[i]) + '" },'
	json_string += '{ "value": "' + str(candidate_polls.getlist_para_two()[len(candidate_polls.getlist_para_two())-1]) + '" }'
	json_string += '''
                    ]
                }
            ]
        },
        {
            "title": "GDELT",
            "titlepos": "left",
            "axisonleft": "1",
            "numdivlines": "10",
            "tickwidth": "10",
            "divlineisdashed": "1",
            "color": "6baa01",
            "dataset": [
                {
                    "seriesname": "Article Counts",
                    "data": ['''
	for i in range (0,len(candidate_gdelt.getlist_para_two())-1):
		json_string += '{ "value": "' + str(candidate_gdelt.getlist_para_two()[i]) + '" },'
	json_string += '{ "value": "' + str(candidate_gdelt.getlist_para_two()[len(candidate_gdelt.getlist_para_two())-1]) + '" }'
	json_string += '''
                    ]
                }
            ]
        }
    ]
}
	'''



	f = open('../FrontEnd/NGC-FrontEnd/public/' + candidate_read + '.json', 'w')
	#f = open(candidate_read + '.json','w')
	f.write(json_string)
