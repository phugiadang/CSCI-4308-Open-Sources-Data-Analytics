
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import signal
#import pandas as pd
#import matplotlib.pyplot as plt

from pyspark_cassandra import CassandraSparkContext, Row
from pyspark import SparkContext, SparkConf
from subprocess import call
import subprocess
import commands
aa=commands.getstatusoutput("b=0")


conf = SparkConf() \
    .setAppName("User Food Migration") \
    .setMaster("spark://128.138.202.110:7077") \
    .set("spark.cassandra.connection.host", "128.138.202.117")

sc = CassandraSparkContext(conf=conf)

users = sc.cassandraTable("junk", "trump2")
trump = users.map(lambda x:
	       {"tweet_id":x['tweet_id'],
		"tweet":x['tweet']} )





#to access Twitter API
consumer_key = "43b4urzsW8nMY3oGzB5tIIM8B"
consumer_secret = "fbGLMhkFyipYbTAz0s0S6yrN6cDGGWnEMmNaciceYjr4sgEdP2"
garbage = 0

access_token = "2990432317-eYMpYm2Ck2G1YBPvWEq7Mf9wdgzBlOydabaxmzN"
access_token_secret = "lQYcmiMlFdic9KSdmd6PClGQ3Swq8y9BgvVPOmqwhHjV2"
epic_garbage = "0"


#This codes inits the tweet count to whatever it was before the program started




class StdOutListener(StreamListener):
    
    
    def on_data(self, data):
        d = json.loads(data)
       
        #UNCOMMENT BELOW TO SEE THE FIRST LEVEL OF KEYS
        #print(data)
        #for key in d.keys(): print key

        #uncomment to just print the text.
        print(d["text"])
        
        #global happy

	file11=open("trumpTweetCount.txt",'r')

	lines = file11.read()
        lines = lines.splitlines()

        happy = int(lines[0])
        happy = happy + 1
        RDD = sc.parallelize([{ "tweet_id": str(happy), "tweet": d["text"] }])
        RDD.saveToCassandra("junk", "trump2")
        #Now write the new tweet count
        file1=open("trumpTweetCount.txt",'w')
        file1.write(str(happy))
        file11.close()
	file1.close()
        return True

    def on_error(self, status):
        print status.text


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
    happy = 0
    trumpKeys = ["Donald Trump","Trump", "trump", "donald trump"]
    bernieKeys = ["feelthebern","bernie2016", "sanders2016"]
    hillaryKeys = ["clinton2016","hillary","readyforhillary","hillary2016"]
    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=["Donald Trump","Trump", "trump", "donald trump"])
