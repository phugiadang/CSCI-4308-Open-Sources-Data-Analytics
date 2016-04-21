#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  ClsuteringAnalysisDrive.py
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
#  

from AnalysisObjectFactory import AnalysisObjectFactory
import GetHourlyTweetsDayRange
from RegressionReadyPolls import RegressionReadyPolls
from GetPollsFromDatabase import DatabasePolls
import GetDailyGDELTCounts
import sys
from datetime import date, timedelta


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
    
    return daily_counts

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

def main():
    
    #check if it's being run locally or by the cronjob
    delt = 1
    if len(sys.argv) == 1:
        delt = 2
    yesterday = date.today() - timedelta(delt)
    Date =  yesterday.strftime('%Y%m%d')
    print Date

    clinton_tweet = float(getTweets('clinton', Date, Date)[0])
    clinton_poll = float(getPolls('clinton', '20160301', Date)[-1])
    clinton_gdelt = getGDELT('clinton', Date, Date)[0]
    
    sanders_tweet = float(getTweets('sanders', Date, Date)[0])
    sanders_poll = float(getPolls('sanders', '20160301', Date)[-1])
    sanders_gdelt = float(getGDELT('sanders', Date, Date)[0])
    
    trump_tweet = float(getTweets('trump', Date, Date)[0])
    trump_poll = float(getPolls('trump', '20160301', Date)[-1])
    trump_gdelt = float(getGDELT('trump', Date, Date)[0])
    
    cruz_tweet = float(getTweets('cruz', Date, Date)[0])
    cruz_poll = float(getPolls('cruz', '20160301', Date)[-1])
    cruz_gdelt = float(getGDELT('cruz', Date, Date)[0])

    kasich_tweet = float(getTweets('kasich', Date, Date)[0])
    kasich_poll = float(getPolls('kasich', '20160301', Date)[-1])
    kasich_gdelt = float(getGDELT('kasich', Date, Date)[0])
    
    AnalysisObjectFactory.initialFactory()
    
    pretty_date = Date[4] + Date[5] + '/' + Date[6] + Date[7] + '/' + Date[0:4]
    types = AnalysisObjectFactory.createObject("ClusteringAnalysis",pretty_date,3, ['Clinton','Sanders','Trump','Cruz', 'Kasich'],[{'Poll':clinton_poll,'GDELT':clinton_gdelt,'Twitter':clinton_tweet},{'Poll':sanders_poll,'GDELT':sanders_gdelt,'Twitter':sanders_tweet},{'Poll':trump_poll,'GDELT':trump_gdelt,'Twitter':trump_tweet},{'Poll':cruz_poll,'GDELT':cruz_gdelt,'Twitter':cruz_tweet},{'Poll':kasich_poll,'GDELT':kasich_gdelt,'Twitter':kasich_tweet}])
    types.clusterAnalysis()
    return 0

if __name__ == '__main__':
	main()

