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
#  Reference: https://districtdatalabs.silvrback.com/modern-methods-for-sentiment-analysis
#  Data sources: http://thinknook.com/twitter-sentiment-analysis-training-corpus-dataset-2012-09-22/

import re
import pandas as pd
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
from AnalysisObject import AnalysisObject
import csv
from sklearn.cross_validation import train_test_split
from gensim.models.word2vec import Word2Vec
from sklearn.preprocessing import scale
import numpy as np
from sklearn.linear_model import SGDClassifier
import unicodedata


def buildModel(size):
	with open('Sentiment Analysis Dataset.csv', 'rb') as csvfile:
		pos_tweets =[]
		neg_tweets =[]
		spamreader = csv.reader(csvfile, delimiter=',')
		for row in spamreader:
			if row[1] == '1':
				if not (len(pos_tweets) > size):
					pos_tweets.append(_cleanTweet(row[3]))
			else:
				if not (len(neg_tweets) > size):
					neg_tweets.append(_cleanTweet(row[3]))
	y = np.concatenate((np.ones(len(pos_tweets[0:size])), np.zeros(len(neg_tweets[0:size]))))
	x_train, x_test, y_train, y_test = train_test_split(np.concatenate((pos_tweets[0:size], neg_tweets[0:size])), y, test_size=0.2)
	x_train = _cleanText(x_train)
	x_test = _cleanText(x_test)
	n_dim = 100
	#Initialize model and build vocab
	imdb_w2v = Word2Vec(size=n_dim, min_count=10)
	imdb_w2v.build_vocab(x_train)
	imdb_w2v.train(x_train)
	train_vecs = np.concatenate([buildWordVector(z, n_dim,imdb_w2v) for z in x_train])
	train_vecs = scale(train_vecs)
	#Train word2vec on test tweets
	imdb_w2v.train(x_test)
	#Build test tweet vectors then scale
	test_vecs = np.concatenate([buildWordVector(z, n_dim,imdb_w2v) for z in x_test])
	test_vecs = scale(test_vecs)
	lr = SGDClassifier(loss='log', penalty='l1')
	lr.fit(train_vecs, y_train)
	imdb_w2v.save("imdb_w2v")
	f = open("Accuracy.txt","w")
	f.write(str(lr.score(test_vecs, y_test))+" "+str(size*2))
	f.close()

			
def buildWordVector(text, size,imdb_w2v):
    vec = np.zeros(size).reshape((1, size))
    count = 0.
    for word in text:
        try:
            vec += imdb_w2v[word].reshape((1, size))
            count += 1.
        except KeyError:
            continue
    if count != 0:
        vec /= count
    return vec
    
def testingTweet(list_tweet,model,train_vecs,y_train):
	n_dim =100
	x_clean = []
	for z in list_tweet:
		x_clean.append(_cleanTweet(z))
	x_tweet = []
	for z in x_clean:
		x_tweet.append(z.split())
	model.train(x_tweet)
	#Build test tweet vectors then scale
	test_vecs = np.concatenate([buildWordVector(z, n_dim,model) for z in x_tweet])
	test_vecs = scale(test_vecs)
	lr = SGDClassifier(loss='log', penalty='l1')
	lr.fit(train_vecs, y_train)
	a=lr.predict(test_vecs)
	return a
	
	

class TweetAnalWord2Vec(AnalysisObject):
	
	#fixed_para_one: name of candidate
	#fixed_para_two:  list of dates
	#list_para_one: list of userids for x-values
	#list_para_two: list of list of tweets for y values
	def __init__(self,fixed_para_one,fixed_para_two,list_para_one,list_para_two):
		super(TweetAnalWord2Vec,self).__init__(fixed_para_one,fixed_para_two,list_para_one,list_para_two)
		
	def sentimentAnalysis(self):
		name = self.getfixed_para_one()
		date = self.getfixed_para_two()
		data_one = self.getlist_para_one()
		data_two = self.getlist_para_two()
		text_output = "TWEET SENTIMENT ANALYSIS FOR TOP 5 USERS USING WORD2VEC\n"
		text_output = text_output+"This model is built to implement the sentiment analysis using deep learning technique Gensim (Word2Vec built-in in python)\n"
		text_output = text_output+"Training data is from: https://districtdatalabs.silvrback.com/modern-methods-for-sentiment-analysis\n"
		f = open('Accuracy.txt','r')
		a=f.read()
		f.close()
		(ac,num_train)=a.split()
		text_output = text_output + "Testing initial model: The accuracy is " + str(int(float(ac)*100)) +"%\n"
		text_output = text_output + "Number of initial training data: " + num_train+"\n"
		text_output = text_output + "Candidate Name: " + name + "\n"
		text_output = text_output + "Data is collected from " + date[0] + " to " + date[len(date)-1] + "\n"
		text_output = text_output + "Top 5 users for this candidate are:\n"
		for i in range (0,len(data_one)):
			text_output = text_output + data_one[i] + " " +str(len(data_two[i])) + "\n"
		users_report = {}
		model = Word2Vec.load("imdb_w2v")
		num_train = int(num_train)/2
		n_dim=100
		with open('Sentiment Analysis Dataset.csv', 'rb') as csvfile:
			pos_tweets =[]
			neg_tweets =[]
			spamreader = csv.reader(csvfile, delimiter=',')
			for row in spamreader:
				if row[1] == '1':
					if not (len(pos_tweets) > num_train):
						pos_tweets.append(_cleanTweet(row[3]))
				else:
					if not (len(neg_tweets) > num_train):
						neg_tweets.append(_cleanTweet(row[3]))
		y = np.concatenate((np.ones(len(pos_tweets[0:num_train])), np.zeros(len(neg_tweets[0:num_train]))))
		x_train, x_test, y_train, y_test = train_test_split(np.concatenate((pos_tweets[0:num_train], neg_tweets[0:num_train])), y, test_size=0.2)
		train_vecs = np.concatenate([buildWordVector(z, n_dim,model) for z in x_train])
		train_vecs = scale(train_vecs)
		for i in range (0,len(data_one)):
			clean_tweet = []
			pos = 0
			neg = 0
			for t in data_two[i]:
				t=unicodedata.normalize('NFKD', t).encode('ascii','ignore')
				clean_tweet.append(t)
			a = testingTweet(clean_tweet,model,train_vecs,y_train)
			for x in a:
				if x == 0.0:
					neg=neg+1
				if x == 1.0:
					pos=pos+1
			users_report[data_one[i]]={"pos":pos,"neg":neg}
			data = pd.DataFrame(users_report)
			fig = plt.figure()
			fig.add_subplot(111)
			data.T.plot.bar(stacked=True)
			plt.title("User Sentiment Analysis using Word2Vec model for " + name)
		plt.savefig('../FrontEnd/NGC-FrontEnd/public/analysis-images/Tweet_Word2Vec_Analysis_'+name,bbox_inches='tight',dpi=100)
		f = open('../FrontEnd/NGC-FrontEnd/public/analysis-images/Tweet_Word2Vec_Analysis_'+name+'.txt','w')
		f.write(text_output)
		f.close()
				
	
	class Factory:
		def create(self,fixed_para_one,fixed_para_two,list_para_one,list_para_two):return TweetAnalWord2Vec(fixed_para_one,fixed_para_two,list_para_one,list_para_two)


def _cleanTweet(tweet):
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
    tweet = tweet.replace("!","")
    #tweet = tweet.replace(name,'')
    return tweet

def _cleanText(corpus):
    corpus = [z.lower().replace('\n','').split() for z in corpus]
    return corpus

