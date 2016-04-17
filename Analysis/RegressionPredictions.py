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
    print 'With Nones: ' + str(reg_polls.getPollNumbers())
    reg_polls.fillGapsWithAvg()
    reg_polls = reg_polls.getPollNumbers()
#    print 'Without Nones: ' + str(reg_polls)
    return reg_polls
    
def getGDELT(candidate, start, end):
    counts, dates = GetDailyGDELTCounts.getGDELTCounts(candidate, start, end)
    return counts
    
def predictPollsWithTwitter(candidate, start, end, source1, source2):
    
    source1_name = ''
    source2_name = ''
    
    tweets, dates = getTweets(candidate, start, end)
    polls = getPolls(candidate, start, end)
    gdelt = getGDELT(candidate, start, end)

    if source1 == 'twitter':
        source1 = tweets
        source1_name = 'Twitter'
    elif source1 == 'gdelt':
        source1 = gdelt
        source1_name = 'GDELT'
    elif source1 == 'polls':
        source1 = polls
        source1_name = 'polls'
    else:
        print 'Unknown source ' + source1

    if source2 == 'twitter':
        source2 = tweets
        source2_name = 'Twitter'
    elif source2 == 'gdelt':
        source2 = gdelt
        source2_name = 'GDELT'
    elif source2 == 'polls':
        source2 = polls
        source2_name = 'Polls'
    else:
        print 'Unknown source ' + source2

    types = AnalysisObjectFactory.createObject("LinearRegressionObject", candidate, dates, (source1_name, source1),(source2_name, source2))
    (text,data)= types.linearRegressionAnalysis()
    print text
    print data

predictPollsWithTwitter(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
#candidate, start, end, source 1, source 2
