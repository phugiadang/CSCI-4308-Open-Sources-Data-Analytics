import sys
import GetHourlyTweetsDayRange
import GetDailyGDELTCounts
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from AnalysisObjectFactory import AnalysisObjectFactory

AnalysisObjectFactory.initialFactory()

def plotTwitter(candidate, start, end):
    twitter_counts = GetHourlyTweetsDayRange.hourlyTweets(candidate, start, end)
    
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
        
    #normalize counts
    types = AnalysisObjectFactory.createObject("GraphAnalysisNormalized", candidate, "twitter", 'dates go here', daily_counts)
    daily_counts = types.getlist_para_two()
    
    print 'Normalized: ' + str(daily_counts) + '\n'
    
    #generate x-axis
    x = list(range(0, len(twitter_counts)))
    plt.plot(x, twitter_counts, 'ro')
    return daily_counts

def plotGDELT(candidate, start, end):
    GDELT_counts = GetDailyGDELTCounts.getGDELTCounts(candidate, start, end)

    #change Nones to 0's
    i = 0
    for count in GDELT_counts:
        if count == None:
            GDELT_counts[i] = 0
        i += 1
    
    #normalize counts
    types = AnalysisObjectFactory.createObject("GraphAnalysisNormalized", candidate, "twitter", 'dates go here', GDELT_counts)
    GDELT_counts = types.getlist_para_two()

    print 'Normalized: ' + str(GDELT_counts) + '\n'
    
    #generate x-axis
    x = list(range(0, len(GDELT_counts)))
    plt.plot(x, GDELT_counts, 'bo')
    return GDELT_counts

def main():

    if len(sys.argv) != 4:
        print 'Usage: python TwitterGDELTGraphAnalysis.py <candidate, lower case> <start date> <end date>'
        print 'where date format is YYYYMMDD'
    else:
        tweets = plotTwitter(sys.argv[1], sys.argv[2], sys.argv[3])
        print len(tweets)
        articles = plotGDELT(sys.argv[1], sys.argv[2], sys.argv[3])
        print len(articles)
        plt.savefig('Twitter_vs_GDELT.png')
main()
