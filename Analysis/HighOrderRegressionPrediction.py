from AnalysisObjectFactory import AnalysisObjectFactory
import numpy as np
from sklearn import linear_model
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
import GetHourlyTweetsDayRange
from RegressionAnalysis import RegressionObject
import GetDailyGDELTCounts
import sys

AnalysisObjectFactory.initialFactory()

def getTweets(candidate, start, end):
    #get the tweets
    twitter_counts, dates = GetHourlyTweetsDayRange.hourlyTweets(candidate, start, end)
    
    #change Nones to 0's
    i = 0
    for count in twitter_counts:
        if count == None:
            twitter_counts[i] = 0
        i += 1

    #turn hourly counts into daily counts
    daily_counts = []
    i = 0
    while i < len(twitter_counts):
        daily_counts.append(sum(twitter_counts[i:i+23]))
        i += 24
    
    return daily_counts, dates

def getGDELT(candidate, start, end):
    counts, dates = GetDailyGDELTCounts.getGDELTCounts(candidate, start, end)
    return counts

def main():
    candidate = sys.argv[1]
    start = sys.argv[2]
    end = sys.argv[3]
    
    tweets, dates = getTweets(candidate, start, end)
    gdelt = getGDELT(candidate, start, end)
    print 'Tweets: ' + str(tweets)
    print 'GDELT: ' + str(gdelt)
    types = AnalysisObjectFactory.createObject("RegressionObject", candidate, dates, tweets, gdelt)


main()
