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


consumer_key = "SNzrQmsgZl3Y1obF5U0VzfJR3"
consumer_secret = "JTGc0f7lznwXLjWEwQPe6XKY1lLrS4kbinCvloZdkTi5Zs7GM8"

access_token = "3298946066-MnUVaCoTJQgxKuKL2NCqtb5cWImgxTrZAVKRCxp"
access_token_secret = "LR0igd7X609r3N0fdR5tWZCTF0TLOQqcArpWNAmL45ozN"



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





tweetCount = {"total": int(lines1[0]), "trump": {int(lines2[0]): [file12, "trumpTweetCount.txt"]}, "rubio": {int(lines3[0]): [file13, "rubioTweetCount.txt"]}, "carson": {int(lines4[0]): [file14,"carsonTweetCount.txt"]}, "sanders": {int(lines5[0]): [file15,"sandersTweetCount.txt"]}, "clinton": {int(lines6[0]): [file16,"clintonTweetCount.txt"]}, "bush": {int(lines7[0]): [file17,"bushTweetCount.txt"]}}

totalTweetCount = tweetCount["total"]



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
        global totalTweetCount
        totalTweetCount += 1 
        
        global tweetCount
        junkList = list(tweetCount[self.keyword[1]])
        
        #convert the tweet to json
        d = json.loads(data)
        hashTags = []
        try:
            for element in d["entities"]["hashtags"]:
                 #uncomment next line to print all hashtags
                 #print element["text"]
                 hashTags.append(element["text"])
        except:
	    print 'Tweet does not contain an entities field!'
        
        coord = []
        if (d["coordinates"] != None):
            coord = d["coordinates"]["coordinates"]
        prepStep = session.prepare("INSERT INTO %s(created_at, coordinates, favorite_count, hashtags, lang, quoted_status_id, retweet_count, tweet_id) VALUES (?,?,?,?,?,?,?,?)" % (self.keyword[1]))
        bindStep = prepStep.bind([d["created_at"], coord, d["favorite_count"], hashTags, d["lang"], int(d["is_quote_status"]), d["retweet_count"], d["id_str"]])
        finalStep = session.execute(bindStep)

        file1=open("totalTweetCount.txt",'w')
        
       
        
        
        file1.write(str(totalTweetCount))
        file1.close        

        badList = tweetCount[self.keyword[1]].itervalues().next()
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
        #print '%s has %d\n' % (self.keyword[1], curCount1)
	if (self.keyword[1] == 'trump'):
		print 'trump' 
        fil.close()
        
        


def start_stream(auth, track):
    tweepy.Stream(auth=auth, listener=StreamListener(track)).filter(track=[track])
    
def start_streamList(auth, listTrack):
    tweepy.Stream(auth=auth, listener=StreamListener(listTrack)).filter(track=[listTrack[0],listTrack[1],listTrack[2],listTrack[3]])
    
#auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
#auth.set_access_token(access_token, access_token_secret)


listTrump = ['Trump', 'trump','Donald Trump','the Donald']
listRubio = ['Rubio', 'rubio','Marco Rubio','Marco Antonio Rubio']
listSanders=['Sanders', 'sanders', 'Bernie Sanders','feel the bern']
listCarson =['Carson', 'carson', 'Ben Carson','Dr. Ben Carson']
listBush =  ['Bush', 'bush', 'Jeb', 'Jeb Bush']
listClinton = ['Clinton','clinton','Hillary','Hillary Clinton']

listOfLists = [listTrump,listRubio,listSanders,listCarson,listBush,listClinton]

track = ['clinton', 'bush', 'python']

i=0

consumer = []
consumer_secret = []
access_token = []
access_token_secret = []

line_count = 0

key_list = []

with open('/home/centos/CSCI-4308-Open-Sources-Data-Analytics/keys.txt', 'r') as key_text:
	for each_key in key_text:
 		key_list.append(str(each_key).rstrip('\n'))

c = 0
for x in range(0, 6):

    consumer.append(key_list[0+c])

    consumer_secret.append(key_list[1+c])

    access_token.append(key_list[2+c])

    access_token_secret.append(key_list[3+c])
    c = c+4


for item in listOfLists:
    auth = tweepy.OAuthHandler(consumer[i], consumer_secret[i])
    auth.set_access_token(access_token[i], access_token_secret[i])
    thread = Thread(target=start_streamList, args=(auth, item))
    thread.start()
    i = i + 1


#for item in track:
#    thread = Thread(target=start_stream, args=(auth, item))
#    thread.start()
