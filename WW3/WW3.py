import time
import csv
import json
import pymongo
import json
from pymongo import MongoClient

#international codes:
#Africa - AFR
#Asia - ASA
#Balkans - BLK
#Caribbean - CRB
#Caucasus - CAU
#Central Africa - CFR
#Central Asia - CAS
#Central Europe - CEU
#East Indies - EIN
#Eastern Africa - EAF
#Eastern Europe - EEU
#Europe - EUR
#Latin America - LAM
#Middle East - MEA
#Mediterranean - MDT
#North Africa - NAF
#North America - NMR
#Persian Gulf - PGS
#Scandanavia - SCN
#South America - SAM
#South Asia - SAAS
#Southeast Asia - SEA
#Southern Africa - SAF
#West Africa - WAF
#"The West" - WST

def goldsteinByContinent():
	client = MongoClient()
	db = client.GDELT_database
	USA = db.posts.find({'actor1Code':{'$in': ['USA']}})
	USAgoldstein = 0
	USAdocsFound = 0
	Europe = db.posts.find({'actor1Code':{'$in':['BLK', 'CAU' 'CEU', 'EEU', 'EUR', 'MDT', 'SCN', '']}})
	EuropeGoldstein = 0
	EuropeDocsFound = 0
	
	for document in USA:
		USAgoldstein += float(document['goldsteinScale'])
		USAdocsFound += 1
		#print(document['goldsteinScale'])

	if(USAdocsFound == 0):
		print("ZERO USA DOCUMENTS FOUND")
	else:
		USAgoldstein = USAgoldstein/USAdocsFound
	print(USAgoldstein)
	
	for document in Europe:
		EuropeGoldstein += float(document['goldsteinScale'])
		EuropeDocsFound += 1

	if(EuropeDocsFound == 0):
		print("ZERO EUROPE DOCS FOUND")
	else:
		EuropeGoldstein = EuropeGoldstein/EuropeDocsFound
	print(EuropeGoldstein)


goldsteinByContinent()