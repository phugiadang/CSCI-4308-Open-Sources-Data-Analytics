#####################
# Senior PRoject
# Basic Tweet Streaming into database
#####################

#To use: sudo pip install tweepy
#        sudo pip install yahoo-finance
#        sudo easy_install mongod
#        sudo service mongod start (sudo servic mongod stop)
#        Make sure to download the constituents.csv file from GitHub
import time
import csv
import tweepy
import json
import pymongo
from pymongo import MongoClient
consumer_key = "43b4urzsW8nMY3oGzB5tIIM8B"
consumer_secret = "fbGLMhkFyipYbTAz0s0S6yrN6cDGGWnEMmNaciceYjr4sgEdP2"

access_token = "2990432317-eYMpYm2Ck2G1YBPvWEq7Mf9wdgzBlOydabaxmzN"
access_token_secret = "lQYcmiMlFdic9KSdmd6PClGQ3Swq8y9BgvVPOmqwhHjV2"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#Change count to change the number of tweets returned

tweetCount = 100
tweets = []
ticker = ""
client = MongoClient('localhost',27017) #default port
db = client['test-database'] #name of database
results = [status._json for status in tweepy.Cursor(api.search,  q=("#turnt")).items(tweetCount)] #convert tweepy to json

#insert into collection called tweets, data stored for me in "/var/lib/mongodb/"
#large size (1000 tweets was around 3.6 GB!!)
resultDB = db.tweets.insert_many(results) 

print resultDB.inserted_ids

