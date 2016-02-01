#http://stackoverflow.com/questions/16602483/filtering-of-tweets-received-from-statuses-filter-streaming-api
#need to edit so that we have sets of tracked strings for names
#
from threading import Thread
from cassandra.cluster import Cluster
import tweepy
import json
import os

keyspace = 'candidates'
cluster = Cluster(
	contact_points=['128.138.202.110','128.138.202.117'],)
#connect to our Cassandra Keyspace
session = cluster.connect(keyspace)


consumer_key = "43b4urzsW8nMY3oGzB5tIIM8B"
consumer_secret = "fbGLMhkFyipYbTAz0s0S6yrN6cDGGWnEMmNaciceYjr4sgEdP2"

access_token = "2990432317-eYMpYm2Ck2G1YBPvWEq7Mf9wdgzBlOydabaxmzN"
access_token_secret = "lQYcmiMlFdic9KSdmd6PClGQ3Swq8y9BgvVPOmqwhHjV2"



file11=open("totalTweetCount.txt",'r+')
lines1 = file11.read()
lines1 = lines1.splitlines()

file12=open("trumpTweetCount.txt",'r+')
lines2 = file12.read()
lines2 = lines2.splitlines()

file13=open("rubioTweetCount.txt",'r+')
lines3 = file13.read()
lines3 = lines3.splitlines()

file14=open("carsonTweetCount.txt",'r+')
lines4 = file14.read()
lines4 = lines4.splitlines()

file15=open("sandersTweetCount.txt",'r+')
lines5 = file15.read()
lines5 = lines5.splitlines()


file16=open("clintonTweetCount.txt",'r+')
lines6 = file16.read()
lines6 = lines6.splitlines()

file17=open("bushTweetCount.txt",'r+')
lines7 = file17.read()
lines7 = lines7.splitlines()





tweet_count = {"total": int(lines1[0]), "trump": {int(lines2[0]): [file12, "trumpTweetCount.txt"]}, "rubio": {int(lines3[0]): [file13, "rubioTweetCount.txt"]}, "carson": {int(lines4[0]): [file14,"carsonTweetCount.txt"]}, "sanders": {int(lines5[0]): [file15,"sandersTweetCount.txt"]}, "clinton": {int(lines6[0]): [file16,"clintonTweetCount.txt"]}, "bush": {int(lines7[0]): [file17,"bushTweetCount.txt"]}}

total_tweet_count = tweet_count["total"]



class StreamListener(tweepy.StreamListener):
    def __init__(self, keyword, api=None):
        super(StreamListener, self).__init__(api)
        self.keyword = keyword

    def on_status(self, tweet):
        print 'Ran on_status'

    def on_error(self, status_code):
        print 'Error: ' + repr(status_code)
        os._exit(1)
        return False

    def on_data(self, data):
        #print self.keyword, data
        #print 'Ok, this is actually running'
        global total_tweet_count, tweet_count
        #global tweet_count
        total_tweet_count += 1

        
        #convert the tweet to json
        d = json.loads(data)
        hash_tags = []
        for element in d["entities"]["hashtags"]:
             #uncomment next line to print all hashtags
             #print element["text"]
             hash_tags.append(element["text"])
        print 'coordinates is: \n'
        
        coord = []
        if (d["coordinates"] != None):
            coord = d["coordinates"]["coordinates"]

        prepStep = session.prepare("INSERT INTO %s(created_at, coordinates, favorite_count, hashtags, lang, quoted_status_id, retweet_count, tweet_id) VALUES (?,?,?,?,?,?,?,?)" % (self.keyword[1]))
        bindStep = prepStep.bind([d["created_at"], coord, d["favorite_count"], hash_tags, d["lang"], int(d["is_quote_status"]), d["retweet_count"], d["id_str"]])
        finalStep = session.execute(bindStep)

        file1=open("totalTweetCount.txt",'w')
        
       
        
        
        file1.write(str(total_tweet_count))
        file1.close        

        badList = tweet_count[self.keyword[1]].itervalues().next()
        filth = badList[0]
        filth.close()
        fil=open(badList[1], "r")
        lin = fil.read()
        lin = lin.splitlines()
        curCount1 = int(lin[0])
        fil.close()
        curCount1+=1
        fil=open(badList[1], "w")
        fil.write(str(curCount1))
        print '%s has %d\n' % (self.keyword[1], curCount1) 
        fil.close()
        
        


def start_stream(auth, track):
    tweepy.Stream(auth=auth, listener=StreamListener(track)).filter(track=[track])
    
def start_streamList(auth, list_track):
    tweepy.Stream(auth=auth, listener=StreamListener(list_track)).filter(track=[list_track[0],list_track[1],list_track[2],list_track[3]])
    
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)


list_trump = ['Trump', 'trump','Donald Trump','the Donald']
list_rubio = ['Rubio', 'rubio','Marco Rubio','Marco Antonio Rubio']
list_sanders=['Sanders', 'sanders', 'Bernie Sanders','feel the bern']
list_carson =['Carson', 'carson', 'Ben Carson','Dr. Ben Carson']
list_bush =  ['Bush', 'bush', 'Jeb', 'Jeb Bush']
list_clinton = ['Clinton','clinton','Hillary','Hillary Clinton']

list_of_lists = [list_trump,list_rubio,list_sanders,list_carson,list_bush,list_clinton]
list_of_items1 = [list_of_lists]
track = ['clinton', 'bush', 'python']

i=0

for item in list_of_lists:
    if ((i == 0)):
    	thread = Thread(target=start_streamList, args=(auth, item))
    	thread.start()
    i = i + 1


#for item in track:
#    thread = Thread(target=start_stream, args=(auth, item))
#    thread.start()
