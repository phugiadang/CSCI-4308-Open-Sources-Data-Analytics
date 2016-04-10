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
import sys

def predictPolls(candidate, start, end):
    AnalysisObjectFactory.initialFactory()
    
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
    
    #get the polls
    polls = DatabasePolls(start, end, [candidate.capitalize()])
    polls.queryDatabase()
    polls.cleanPolls()
    clean_polls = polls.getCleanedPolls()
    
    reg_polls = RegressionReadyPolls(clean_polls, candidate.capitalize(), start, end)
    reg_polls.makeSimplePollNumbers()
    reg_polls.fillGapsWithAvg()
    reg_polls = reg_polls.getPollNumbers()

    print 'Polls: ' + str(reg_polls)
    print 'Tweets: ' + str(daily_counts)
    
    types = AnalysisObjectFactory.createObject("LinearRegressionObject", candidate, dates, ("Tweets", daily_counts),("Polls", reg_polls))
    (text,data)= types.linearRegressionAnalysis()
    print text
    print data

predictPolls(sys.argv[1], sys.argv[2], sys.argv[3])
#predictPolls('sanders', '20160301', '20160330')
