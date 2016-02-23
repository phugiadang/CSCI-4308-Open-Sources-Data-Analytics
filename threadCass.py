#http://stackoverflow.com/questions/16602483/filtering-of-tweets-received-from-statuses-filter-streaming-api
#need to edit so that we have sets of tracked strings for names
#
from threading import Thread
from cassandra.cluster import Cluster
from subprocess import call
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

file17=open("cruzTweetCount.txt",'r+')
lines7 = file17.read()
lines7 = lines7.splitlines()

file18=open("kasichTweetCount.txt",'r+')
lines8 = file18.read()
lines8 = lines8.splitlines()

file19=open("bushTweetCount.txt",'r+')
lines9 = file19.read()
lines9 = lines9.splitlines()

#call("sudo sh -c \"date | cut -d ' ' -f 1-5 > startTime.txt\"", shell=True)


tweet_count = {"total": int(lines1[0]), "trump": {int(lines2[0]): [file12, "trumpTweetCount.txt"]}, "rubio": {int(lines3[0]): [file13, "rubioTweetCount.txt"]}, "carson": {int(lines4[0]): [file14,"carsonTweetCount.txt"]}, "sanders": {int(lines5[0]): [file15,"sandersTweetCount.txt"]}, "clinton": {int(lines6[0]): [file16,"clintonTweetCount.txt"]}, "cruz": {int(lines7[0]): [file17,"cruzTweetCount.txt"]}, "kasich": {int(lines8[0]): [file18, "kasichTweetCount.txt"]}, "bush": {int(lines9[0]): [file19, "bushTweetCount.txt"]}}

total_tweet_count = tweet_count["total"]


month_dict = {'Jan' : '01', 'Feb' : '02', 'Mar' : '03', 'Apr' : '04', 'May' : '05', 'Jun' : '06', 'Jul' : '07', 'Aug' : '08', 'Sep' : '09', 'Oct' : '10', 'Nov' : '11', 'Dec' : '12'}


#This function converts a standard date to a date used by our database
#
#Ex.
#Input = "Feb 16 05:11:06 2016"
#Output = 20160216051106
#
def numerizeDate(real_date):
    if (real_date == -1):
        return real_date
    numerical_date = ''
    current_word = ''
    word_num = 1
    character_count = 0
    for character in real_date:
	character_count += 1
	if (character_count == len(real_date)):
	    current_word += character
	    numerical_date = current_word+numerical_date
            return numerical_date.replace(':','')
        elif (character != ' '):
            current_word += character
	else:
	    if (word_num == 2):
		numerical_date = month_dict[current_word]+numerical_date
	    elif ((word_num == 3) or (word_num == 4)):
		numerical_date += current_word
 
            current_word = ''
            word_num += 1
	    		

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
        
        global tweet_count, total_tweet_count
        total_tweet_count += 1 
           
        #convert the tweet to json
        d = json.loads(data)
        hash_tags = []
        try:
            #If tweet has an entities field, append all hashtags to the list
            for element in d["entities"]["hashtags"]:
                 #uncomment next line to print all hashtags
                 #print element["text"]
                 hash_tags.append(element["text"])
        except:
	    print 'Tweet for %s does not contain an entities field!' % (self.keyword[1])
      
        coord = []
        try:
            if (d["coordinates"] != None):
                coord = d["coordinates"]["coordinates"]
        except:
    	    print 'Tweet for %s does not contain a coordinates field!' % (self.keyword[1])


        c9,text_field = 'NULL', 'NULL'
        b9,d9,e9 = 0,0,0
	a9, f9, utc = -1, -1, -1
                
        try:
            #Make sure tweet has all needed fields
            utc = d["user"]["utc_offset"]
            a9 = d["created_at"]
            b9 = d["favorite_count"]        
            c9 = d["lang"]
            d9 = int(d["is_quote_status"])
            e9 = d["retweet_count"]
            f9 = d["id_str"]
            text_field = d["text"]
            
                     
        except:
	    print 'Tweet for %s is missing a field!' % (self.keyword[1])

        #Convert date into usable format
        numerical_date = numerizeDate(a9)
         
      
        if (utc != None):
            #Convert tweet time to user local time
            utc = int(utc)/3600
            actual_date = int(numerical_date) + utc
        
	
	#if (numerical_date != 'NULL'):
	#    f9 = int(numerical_date + str(f9))

        #Execute the Cassandra command to store the tweet fields into the database	    
        final_step = session.execute_async('insert into ' + self.keyword[1] + '(tweet_id, coordinates, created_at, favorite_count, hashtags, lang, quoted_status_id, retweet_count, tweet_text) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)', (int(f9),coord,int(numerical_date),b9,hash_tags,c9,d9,e9,text_field))



        #Uncomment this try/except block if you want to see if the tweet fields are getting stored properly
	
        #try:
            #if this prints a cassandra.cluster.ResultSet object, it was successfully stored in the database
        #    print final_step.result()
        #except:
	    
 	    #print 'fail\n'


        file1=open("totalTweetCount.txt",'w')
         
        file1.write(str(total_tweet_count))
        file1.close        

        #Read and update the candidate's tweet count and write to file
        bad_list = tweet_count[self.keyword[1]].itervalues().next()
        filth = bad_list[0]
        filth.close()
        fil=open(bad_list[1], "r")
        lin = fil.read().splitlines()
        cur_count1 = int(lin[0])
        fil.close()
        cur_count1+=1
        fil=open(bad_list[1], "w")
        fil.write(str(cur_count1))
        #print '%s has %d tweets\n' % (self.keyword[1], cur_count1)
	 
        fil.close()
        
        


def start_stream(auth, track):
    tweepy.Stream(auth=auth, listener=StreamListener(track)).filter(track=[track])
    
def start_streamList(auth, list_track):
    tweepy.Stream(auth=auth, listener=StreamListener(list_track)).filter(track=[list_track[0],list_track[1],list_track[2],list_track[3]])
    
#auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
#auth.set_access_token(access_token, access_token_secret)


list_trump = ['Trump', 'trump','Donald Trump','the Donald']
list_rubio = ['Rubio', 'rubio','Marco Rubio','Marco Antonio Rubio']
list_sanders=['Sanders', 'sanders', 'Bernie Sanders','feel the bern']
list_carson =['Carson', 'carson', 'Ben Carson','Dr. Ben Carson']
list_cruz =  ['Cruz', 'cruz', 'CruzCrew', 'TrusTED']
list_clinton = ['Clinton', 'clinton', 'Hillary', 'Hillary Clinton']
list_kasich = ['Kasich', 'kasich', 'John Kasich', 'Kasich4Us']
list_bush = ['Jeb!', 'bush', 'Jeb Bush', 'Bush']

list_of_lists = [list_trump,list_rubio,list_sanders,list_carson,list_cruz,list_clinton,list_kasich,list_bush]

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

#Append each key to its appropriate list for each of the 8 candidates
for x in range(0, 8):

    consumer.append(key_list[0+c])

    consumer_secret.append(key_list[1+c])

    access_token.append(key_list[2+c])

    access_token_secret.append(key_list[3+c])
    c = c+4


#Spawn a new thread for each of the 8 candidates 
for item in list_of_lists:

    auth = tweepy.OAuthHandler(consumer[i], consumer_secret[i])
    auth.set_access_token(access_token[i], access_token_secret[i])
    thread = Thread(target=start_streamList, args=(auth, item))
    thread.start()
    i = i + 1
