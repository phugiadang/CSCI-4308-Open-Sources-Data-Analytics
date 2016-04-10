from AnalysisObjectFactory import AnalysisObjectFactory
import numpy as np
from sklearn import linear_model
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
import GetHourlyTweetsDayRange
from RegressionReadyPolls import RegressionReadyPolls
from GetPollsFromDatabase import DatabasePolls
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

def getPolls(candidate, start, end):
    #get the polls
    polls = DatabasePolls(start, end, [candidate.capitalize()])
    polls.queryDatabase()
    polls.cleanPolls()
    clean_polls = polls.getCleanedPolls()
    
    reg_polls = RegressionReadyPolls(clean_polls, candidate.capitalize(), start, end)
    reg_polls.makeSimplePollNumbers()
    reg_polls.fillGapsWithAvg()
    reg_polls = reg_polls.getPollNumbers()

    return reg_polls

def getGDELT(candidate, start, end):
    counts, dates = GetDailyGDELTCounts.getGDELTCounts(candidate, start, end)
    return counts

def predictPollsWithTwitter(candidate, start, end):
    
    tweets, dates = getTweets(candidate, start, end)
    polls = getPolls(candidate, start, end)
    gdelt = getGDELT(candidate, start, end)

    types = AnalysisObjectFactory.createObject("LinearRegressionObject", candidate, dates, ("Tweets", tweets),("GDELT", gdelt))
    (text,data)= types.linearRegressionAnalysis()
    print text
    print data

predictPollsWithTwitter(sys.argv[1], sys.argv[2], sys.argv[3])
