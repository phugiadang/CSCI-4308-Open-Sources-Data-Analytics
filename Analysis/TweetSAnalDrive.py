from cassandra.cluster import Cluster

keyspace = 'candidates'
cluster = Cluster(
        contact_points=['128.138.202.110','128.138.202.117'],)
#connect to our Cassandra Keyspace
session = cluster.connect(keyspace)
session.default_timeout = 600

#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  TweetSAnalDrive.py
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


def main():
	AnalysisObjectFactory.initialFactory()

        list_of_userids = []
        list_of_list_of_tweets = []
        list_of_candidates = ["sanders","trump"]
        for candidate in list_of_candidates:
            list_of_userids = []
            list_of_list_of_tweets = []
            final_result = session.execute("select * from topTweeters where candidate_name = '" + candidate + "'");
            for user in final_result:
                list_of_userids.append(str(getattr(user, "user_id")))
                list_of_list_of_tweets.append(getattr(user, "list_of_tweets"))
            #print [[list_of_list_of_tweets[0][0]]]
            types = AnalysisObjectFactory.createObject("TweetSentimentAnalysis",candidate,["3/6/2016", "4/5/2016"],list_of_userids, list_of_list_of_tweets)
        #types = AnalysisObjectFactory.createObject("TweetSentimentAnalysis","kasich",["3/6/2016", "4/5/2016"],[list_of_userids[0]], [[u"I fell da bernz mutilate fun happy"]])

#[[list_of_list_of_tweets[0][0]]]

	#types = AnalysisObjectFactory.createObject("TweetSentimentAnalysis","trump",["2/17/2016","2/18/2016","2/19/2016","2/20/2016","2/21/2016","2/22/2016","2/23/2016"],['123','234'],[["Trump is a motherfucking Genius! Ban all Muslims is the best thing ever!","RT @kateloving: KING: Bill Clinton almost sounds like Donald Trump with jab https://t.co/5a2ze5YTc4","This is an exercise in taking Donald Trump at his word"," @GlobeIdeas editor @katiekings... https://t.co/vEa1mhKVDz via @jorgeramosnews"],["The TRUMP Fight Song [unofficial] - TRUMP 2016 https://t.co/9AnOeQV83V via @YouTube","Cheats abd liars in GOPe - time to write in Trump! #StopTheSteal help Trump #BurnDownTheGOP https://t.co/3z8qY8IW5Q","Trump nomination up to 200 people","Trump nomination up to 200 people"]])
	    output = types.sentimentAnalysis()
	    print output
	return 0

if __name__ == '__main__':
	main()

