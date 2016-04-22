#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  TweetSentimentAnalysis.py
#  
#  Copyright 2016 user <user@cu-cs-vm>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  Reference: http://ravikiranj.net/posts/2012/code/how-build-twitter-sentiment-analyzer/

import subprocess
import re
import ast
import pandas as pd
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
from AnalysisObject import AnalysisObject
import unirest

class TweetSentimentAnalysis(AnalysisObject):
	
	#fixed_para_one: name of candidate
	#fixed_para_two:  list of dates
	#list_para_one: list of userids for x-values
	#list_para_two: list of list of tweets for y values
	def __init__(self,fixed_para_one,fixed_para_two,list_para_one,list_para_two):
		super(TweetSentimentAnalysis,self).__init__(fixed_para_one,fixed_para_two,list_para_one,list_para_two)
		
	def sentimentAnalysis(self):
		name = self.getfixed_para_one()
		date = self.getfixed_para_two()
		data_one = self.getlist_para_one()
		data_two = self.getlist_para_two()
		text_output = "TWEET SENTIMENT ANALYSIS FOR TOP 5 USERS\n"
		text_output = text_output + "Candidate Name: " + name + "\n"
		text_output = text_output + "Data is collected from " + date[0] + " to " + date[len(date)-1] + "\n"
		text_output = text_output + "Top 5 users for this candidate are:\n"
		for i in range (0,len(data_one)):
			text_output = text_output + data_one[i] + " " +str(len(data_two[i])) + "\n"
		users_report = {}
		for i in range (0,len(data_one)):
			#print "data_one is " + str(data_one)
                        #print "length of data_one is " + str(len(data_one))
                        clean_tweet = []
			pos = 0
			neg = 0
			neutral = 0
			for stt in data_two[i]:
				clean_tweet.append(_cleanTweet(stt,name))
			for stt in clean_tweet:
				#p = subprocess.Popen("curl -d text='"+str(stt)+"' http://text-processing.com/api/sentiment/", shell=True,stdout=subprocess.PIPE).communicate()[0]
                                #print stt
                                try:
                                    stt = str(stt)
     
                                except:
                                    print 'bad tweet!'
                                    stt = 'bad'
                                good = 1
                                
                                try:
                                    
                                    p = unirest.post("https://japerk-text-processing.p.mashape.com/sentiment/",
  headers={
    "X-Mashape-Key": "eo2rOfIXzUmshGWmknOvJlkdceozp1oMJLYjsniKpR5UXjovLm",
    "Content-Type": "application/x-www-form-urlencoded",
    "Accept": "application/json"
  },
  params={
    "language": "english",
    "text": stt
  }
)
                                    		                
                                    good = 0

                                except:
                                    good = 1

                                #print p		
                                p1 = p.body
                               
                                
                                try:
				    if p1["label"] == "neg":
				        neg = neg +1
				    elif p1["label"] == "pos":
					pos = pos +1
                                    elif p1["label"] == "bad":
                                        neutral += 0
				    else:
					neutral = neutral +1
                                except:
                                    neutral += 1
                        
                             
                        print "USER REPORT: " + str(users_report)
			users_report[data_one[i]]={"pos":pos,"neg":neg,"neutral":neutral}
			data = pd.DataFrame(users_report)
			fig = plt.figure()
			fig.add_subplot(111)
			data.T.plot.bar(stacked=True)
		        plt.title("User Sentiment Analysis for " + name)
			plt.savefig('User_Sentiment_Analysis_'+name,bbox_inches='tight',dpi=100)
				 
		return text_output
				
	
	class Factory:
		def create(self,fixed_para_one,fixed_para_two,list_para_one,list_para_two):return TweetSentimentAnalysis(fixed_para_one,fixed_para_two,list_para_one,list_para_two)


def _cleanTweet(tweet,name):
    tweet = tweet.lower()
    #Convert www.* or https?://* to URL
    tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+))','',tweet)
    #Convert @username to AT_USER
    tweet = re.sub('@[^\s]+','',tweet)
    #Remove additional white spaces
    tweet = re.sub('[\s]+', ' ', tweet)
    #Replace #word with word
    tweet = re.sub(r'#([^\s]+)', r'\1', tweet)
    #trim
    tweet = tweet.strip('\'"')
    #tweet = tweet.replace(name,'')
    tweet = tweet.replace("'", "").replace("@","")
    tweet = tweet.replace(u"\u201c", "").replace(u'\u2026', "").replace(u'\u2014', "").replace(u'\u2019', "").replace(u'\u2018', "").replace(u'\u201d', "").replace(u'\xa0', "").replace(u'\u2022', "")
    return tweet
#end
