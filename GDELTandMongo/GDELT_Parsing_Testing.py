import csv

#GDELT format documentation and CAMEO codes: http://www.gdeltproject.org/data.html#documentation
#GDELT data format:
#GlobalEventID, date(YYYYMMDD), date(YYYYMM), date(YYYY), date(YYYY.FFFF)
#Actor1Code, Actor1Name, Actor1CountryCode, Actor1KnownGroupCode, Actor1EthnicCode,
#Actor1ReligionCode, Actor1ReligionCode2, Actor1Type1Code, Actor1Type2Code, 
#Actor1Type3Code (15 fields)
#Repeat for Actor 2
#IsRootEvent, EventCode, EventBaseCode, EventRootCode, QuadClass, GoldsteinScale, 
#NumMentions, NumSources, NumArticles, AvgTone
#Actor1Geo_Type, Actor1GeoFullname, Actor1Geo_CountryCode, Actor1Geo_ADM1Code, 
#Actor1Geo_Lat, Actor1Geo_Long, Actor1Geo_FeatureID
#DATEADDED, SOURCEURL

def patriotismSimulator():
	with open('20150923.export.CSV', 'rb') as csvfile:
		reader = csv.reader(csvfile, delimiter='	', quotechar='|')
		for row in reader:
			if(row[7] == 'USA'):
				print row[7]

def printRiots():
	with  open('20150923.export.CSV', 'rb') as csvfile:
		reader = csv.reader(csvfile, delimiter='	', quotechar='|')
		for row in reader:
			#row[33] is the EventRootCode, 145 is the code for violent protest/riot
			if(row[33] == '145'):
				print row[6]

def printUSRiots():
	with  open('20150923.export.CSV', 'rb') as csvfile:
		reader = csv.reader(csvfile, delimiter='	', quotechar='|')
		for row in reader:
			#row[33] is the EventRootCode, 145 is the code for violent protest/riot
			if(row[33] == '145' and row[7] == 'USA'):
				print ('Riot/violent protest occured in/by ' + str(row[6]))
				print(row[57])

def printIncreasePoliceAlertness():
	with  open('20150923.export.CSV', 'rb') as csvfile:
		reader = csv.reader(csvfile, delimiter='	', quotechar='|')
		goldstein = 0
		eventsFound = 0
		for row in reader:
			if(row[33] == '151'):
				print('Increased Police Alertness in ' + str(row[7]))
				#print avg Goldstein Scale rating around these events
				goldstein += int(row[35])
				eventsFound += 1
		print('Average Goldstein Rating of Events: ' + str(goldstein/eventsFound))

def printIncreaseMilitaryAlertness():
	with  open('20150923.export.CSV', 'rb') as csvfile:
		reader = csv.reader(csvfile, delimiter='	', quotechar='|')
		goldstein = 0
		eventsFound = 0
		for row in reader:
			if(row[33] == '152'):
				print('Increased Military Alertness in ' + str(row[7]))
				goldstein += int(row[35])
				eventsFound += 1
		print('Average Goldstein Rating of Events: ' + str(goldstein/eventsFound))

# printRiots()
# print patriotismSimulator()
# printUSRiots()
# printIncreasePoliceAlertness()
printIncreaseMilitaryAlertness()