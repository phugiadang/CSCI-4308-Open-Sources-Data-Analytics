#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  happiness.py
#  
#  Phu Dang
#  
#  This script is used to form the idea how to track the happiness based on civilian in Switzerland
#  Copyright 2015 user <user@cu-cs-vm>
#  
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

import csv

def countHappinessBasedOnCivilian():
	listCountry=[]
	with open('20151008172731.28282.events.csv', 'rb') as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			if (float(row[30]) < 0.0): #Make sure the event doesn't impact too much based on Goldstrein scale
				k=0
				for i in listCountry:
					if i[0] == row[7]:
						i[1] = i[1]+1
						k=1
				if (k==0) and (row[7] != ''):
					listCountry.append([row[7],1])
	return listCountry
			

def main():
	listCountry = countHappinessBasedOnCivilian()
	for i in listCountry:
		print i[0],i[1]
	return 0

if __name__ == '__main__':
	main()

