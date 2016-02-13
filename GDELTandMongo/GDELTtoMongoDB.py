import time
import csv
import tweepy
import json
import pymongo
import json
from pymongo import MongoClient


def dumpGDELTtoMongoDB():
	with  open('20150923.export.CSV', 'rb') as csvfile:
		reader = csv.reader(csvfile, delimiter='	', quotechar='|')

		client = MongoClient('localhost',27017) #default port
		db = client['GDELT_database'] #name of database
		#collection = db['test-collection']

		for row in reader:
			#grab data from the row

			data = {}
			data['eventID'] = row[0]
			data['date'] = row[1]
			data['actor1Code'] = row[5]
			data['actor1Name'] = row[6]
			data['actor1CountryCode'] = row[7]
			data['actor1KnownGroupCode'] = row[8]
			data['actor1EthnicCode'] = row[9]
			data['actor1Religion1Code'] = row[10]
			data['actor1Religion2Code'] = row[11]
			data['actor1Type1Code'] = row[12]
			data['actor1Type2Code'] = row[13]
			data['actor1Type3Code'] = row[14]

			data['actor2Code'] = row[15]
			data['actor2Name'] = row[16]
			data['actor2CountryCode'] = row[17]
			data['actor2KnownGroupCode'] = row[18]
			data['actor2EthnicCode'] = row[19]
			data['actor2Religion1Code'] = row[20]
			data['actor2Religion2Code'] = row[21]
			data['actor2Type1Code'] = row[22]
			data['actor2Type2Code'] = row[23]
			data['actor2Type3Code'] = row[24]

			data['eventCode'] = row[26]
			data['eventBaseCode'] = row[27]
			data['quadClass'] = row[29]

			data['goldsteinScale'] = row[30]

			data['numMentions'] = row[31]
			data['numSources'] = row[32]
			data['numArticles'] = row[33]
			data['avgTone'] = row[34]

			data['actor1Geo_Type'] = row[35]
			data['actor1Geo_Fullname'] = row[36]
			data['actor1Geo_CountryCode'] = row[37]
			data['actor1Geo_Lat'] = row[39]
			data['actor1Geo_Long'] = row[40]

			data['actor2Geo_Type'] = row[42]
			data['actor2Geo_Fullname'] = row[43]
			data['actor2Geo_CountryCode'] = row[44]
			data['actor2Geo_Lat'] = row[46]
			data['actor2Geo_Long'] = row[47]

			data['actionGeo_Type'] = row[49]
			data['actionGeo_Fullname'] = row[50]
			data['actionGeo_CountryCode'] = row[51]
			data['actionGeo_Lat'] = row[53]
			data['actionGeo_Long'] = row[54]

			data['dateAdded'] = row[56]

			#data = [data]
			
			#make it a JSON object
			entry = json.dumps(data)

			#put it into the database
			post_id = db.posts.insert_one(data).inserted_id
			print(post_id)


dumpGDELTtoMongoDB()



# client = MongoClient('localhost',27017) #default port
# db = client['GDELT-database'] #name of database