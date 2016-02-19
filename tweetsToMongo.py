import sys
from pymongo import MongoClient





client = MongoClient()
db = client['MeanMapAppTest']
coll = db['Tweets']

f = open('trumpTweetCount.txt')
trumpTweets = f.read()
print trumpTweets
f.close()
f = open('rubioTweetCount.txt')
rubioTweets = f.read()
print rubioTweets
f.close()


coll.insert_one(
    {
        "candidate": "Rubio",
	"startDate": 20120201,
	"endDate": 20120214,
	"count": rubioTweets})
coll.insert_one(
    {
        "candidate": "Trump",
	"startDate": 20120201,
	"endDate": 20120214,
	"count": trumpTweets})
