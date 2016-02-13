#http://stackoverflow.com/questions/16602483/filtering-of-tweets-received-from-statuses-filter-streaming-api
#need to edit so that we have sets of tracked strings for names
#
from threading import Thread
import tweepy
consumer_key = "43b4urzsW8nMY3oGzB5tIIM8B"
consumer_secret = "fbGLMhkFyipYbTAz0s0S6yrN6cDGGWnEMmNaciceYjr4sgEdP2"

access_token = "2990432317-eYMpYm2Ck2G1YBPvWEq7Mf9wdgzBlOydabaxmzN"
access_token_secret = "lQYcmiMlFdic9KSdmd6PClGQ3Swq8y9BgvVPOmqwhHjV2"

class StreamListener(tweepy.StreamListener):
    def __init__(self, keyword, api=None):
        super(StreamListener, self).__init__(api)
        self.keyword = keyword

    def on_status(self, tweet):
        print 'Ran on_status'

    def on_error(self, status_code):
        print 'Error: ' + repr(status_code)
        return False

    def on_data(self, data):
        print self.keyword, data
        print 'Ok, this is actually running'
def start_stream(auth, track):
    tweepy.Stream(auth=auth, listener=StreamListener(track)).filter(track=[track])
    
def start_streamList(auth, listTrack):
    tweepy.Stream(auth=auth, listener=StreamListener(track)).filter(track=[listTrack[0],listTrack[1],listTrack[2],listTrack[3]])
    
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)


listTrump = ['Trump', 'trump','Donald Trump','the Donald']
listRubio = ['Rubio', 'rubio','Marco Rubio','Marco Antonio Rubio']
listSanders=['Sanders', 'sanders', 'Bernie Sanders','feel the bern']
listCarson =['Carson', 'carson', 'Ben Carson','Dr. Ben Carson']
listBush =  ['Bush', 'bush', 'Jeb', 'Jeb Bush']
listClinton = ['Clinton','clinton','Hillary','Hillary Clinton']

listOfLists = [listTrump,listRubio,listSanders,listCarson,listBush,listClinton]

track = ['clinton', 'bush', 'python']

i=0

for item in listOfLists:
    thread = Thread(target=start_streamList, args=(auth, listOfLists[0]))
    thread.start()
    i = i + 1


#for item in track:
#    thread = Thread(target=start_stream, args=(auth, item))
#    thread.start()
