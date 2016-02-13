#####################
# Senior PRoject
# Basic Tweet Streaming
#####################

#To use: sudo pip install tweepy
#        sudo pip install yahoo-finance
#        Make sure to download the constituents.csv file from GitHub
import time
import csv
import tweepy
import json
consumer_key = "43b4urzsW8nMY3oGzB5tIIM8B"
consumer_secret = "fbGLMhkFyipYbTAz0s0S6yrN6cDGGWnEMmNaciceYjr4sgEdP2"

access_token = "2990432317-eYMpYm2Ck2G1YBPvWEq7Mf9wdgzBlOydabaxmzN"
access_token_secret = "lQYcmiMlFdic9KSdmd6PClGQ3Swq8y9BgvVPOmqwhHjV2"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#Change count to change the number of tweets returned

tweetCount = 20
tweets = []
ticker = ""

results = api.search(q=("#pope"),count = tweetCount)

i = 0
for result in results:
	i = i + 1
	save_file = open('tweets.json', 'a')
	save_file.write(str(results))
	print ("TWEET NUMBER : " + str(i) + " " + result.text + "\n" +"Created at :" +  str(result.created_at) + "\n")
	

#print(results);
