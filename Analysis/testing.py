import json
import sys
from sys import argv
import operator
from AnalysisObject import AnalysisObject
from cassandra.cluster import Cluster
from calendar import monthrange
import jsonizeFunc
import time, datetime
from time import gmtime,strftime

hour = int(strftime("%H",  gmtime()))-1
if hour < 0:
        hour = 23
day = int(strftime("%d",  gmtime()))
yesterday = day -1
if hour == 23:
        day = yesterday
year =  int(strftime("%Y", gmtime()))
month = int(strftime("%m", gmtime()))
monthInt = month
if month < 10:
    stringMonth = "0"+str(month)
if month >= 10:
    stringMonth = str(month)
month = stringMonth
#We want to grab the the hours of the current day
#Then, we want to grab the previous day's hours

now = datetime.datetime.now()



previousDay = str(year) + stringMonth + str(day - 1) + str(hour) + str("0000")
currentDay = str(year) + stringMonth + str(day) + str(hour) + str("0000")
print previousDay
print currentDay

jsonizeFunc()
