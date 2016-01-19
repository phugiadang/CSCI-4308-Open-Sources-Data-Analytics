#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import signal
#import pandas as pd
#import matplotlib.pyplot as plt






#to access Twitter API 
consumer_key = "43b4urzsW8nMY3oGzB5tIIM8B"
consumer_secret = "fbGLMhkFyipYbTAz0s0S6yrN6cDGGWnEMmNaciceYjr4sgEdP2"

access_token = "2990432317-eYMpYm2Ck2G1YBPvWEq7Mf9wdgzBlOydabaxmzN"
access_token_secret = "lQYcmiMlFdic9KSdmd6PClGQ3Swq8y9BgvVPOmqwhHjV2"


#List of Current candidates
#Hillary Clinton, Governor Martin O'Malley, Senator Bernie Sanders
#Jeb Bush,Ben Carson  Chris Christie, Ted Cruz, Carly Fiorina,
# Jim Gilmore, Lindsey Graham
#Mike Huckabee, Bobby Jindal, John Kasich, George Pataki
# Rand Paul, Marco Rubio, Rick Santorum, Donald Trump
#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        d = json.loads(data)
        
        #UNCOMMENT BELOW TO SEE THE FIRST LEVEL OF KEYS
        #print(data)
        #for key in d.keys(): print key
        
        #uncomment to just print the text.
        #print(d["text"])
        print(d["text"])
        return True

    def on_error(self, status):
        print status.text


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=["Donald Trump","Trump", "trump", "donald trump"])


#List of Current candidates
#Hillary Clinton, Governor Martin O'Malley, Senator Bernie Sanders
#Jeb Bush,Ben Carson  Chris Christie, Ted Cruz, Carly Fiorina,
# Jim Gilmore, Lindsey Graham
#Mike Huckabee, Bobby Jindal, John Kasich, George Pataki
# Rand Paul, Marco Rubio, Rick Santorum, Donald Trump
#This is a basic listener that just prints received tweets to stdout.


