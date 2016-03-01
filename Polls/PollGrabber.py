from pollster import Pollster 
from datetime import date, timedelta
from cassandra.cluster import Cluster
from operator import itemgetter
import sys
import time

cluster = Cluster(['128.138.202.110', '128.138.202.117'])
session = cluster.connect('polls')

pollster = Pollster()

class pollGrabber:
	def __init__(self, sd, ed):
		self.start_date = sd
		self.end_date = ed
		self.all_polls = []

        def restructurePoll(self, poll):
                new = {'pollster': '', 'start_date': '', 'end_date': '', 'name': '', 'observations': '', 'responses': []}
                new['pollster'] = poll.pollster
                new['start_date'] = int(poll.start_date.replace('-', ''))
                new['end_date'] = int(poll.end_date.replace('-', ''))
                new['name'] = poll.questions[0]['name']
                new['observations'] = poll.questions[0]['subpopulations'][0]['observations']
                new['responses'] = str(poll.questions[0]['subpopulations'][0]['responses'])                
                return new

        #run multiple queries to grab all possible relevant polls, then filter them by their name
        def getRelevantStatePolls(self):
                
                #parse out the inputted dates
                try:
			start = self.start_date.split('-', 2)
			start = date(int(start[0]), int(start[1]), int(start[2]))
			end = self.end_date.split('-', 2)
			end = date(int(end[0]), int(end[1]), int(end[2]))
		except:
			print 'Date could not be parsed correctly'
			print 'Make sure it is in the format YYYY-MM-DD'
			return
                
                #run every possible query to get all the charts
                all_polls = {}
                all_chart_groups = []
                states = ['AL', 'AK', 'AZ', 'AR', 'CA']#, 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY', 'DC']
                for st in states:
#                        all_chart_groups.append(pollster.charts(state = st))
                        state_polls = []
                        charts = pollster.charts(state = st)
                        for chart in charts:
                                polls = chart.polls()
                                for poll in polls:
                                        name = poll.questions[0]['name']
                                        #filter out stuff we don't want
                                        if ('2016' in name and ('Presidential' in name or 'President' in name)):
                                                #grab and format the current poll's date
                                                poll_end = poll.end_date.split('-', 2)
                                                poll_end = date(int(poll_end[0]), int(poll_end[1]), int(poll_end[2]))
                                                
                                                #check if it's in the date range
                                                if(poll_end < end and poll_end >= start):
                                                        poll = self.restructurePoll(poll)
                                                        state_polls.append(poll)
                        all_polls[st] = poll
                                
                return all_polls

        def getRelevantTopicPolls(self):
                all_polls = {'topic': []}
                try:
			start = self.start_date.split('-', 2)
			start = date(int(start[0]), int(start[1]), int(start[2]))
			end = self.end_date.split('-', 2)
			end = date(int(end[0]), int(end[1]), int(end[2]))
		except:
			print 'Date could not be parsed correctly'
			print 'Make sure it is in the format YYYY-MM-DD'
			return
		
		#get each chart in the given topic
		charts = pollster.charts(topic = '2016-president')
		for chart in charts:

			#grab all the polls in the current chart
			polls = chart.polls()
			for poll in polls:

				#grab and format the current poll's date
				poll_start = poll.start_date.split('-', 2)
		 		poll_start = date(int(poll_start[0]), int(poll_start[1]), int(poll_start[2]))
		 		poll_end = poll.end_date.split('-', 2)
		 		poll_end = date(int(poll_end[0]), int(poll_end[1]), int(poll_end[2]))
                                
				#check if it's in the date range
				if(poll_end < end and poll_end >= start):
                                        poll = self.restructurePoll(poll)
					all_polls['topic'].append(poll)
                return all_polls

	def queryPolls(self):
                self.all_polls = self.getRelevantStatePolls()
                self.all_polls.update(self.getRelevantTopicPolls())
                print self.all_polls
                #sort the lists in all_polls on the end_date before putting them in cassandra
                for state in self.all_polls:
                        poll_list =  self.all_polls[state]
                        poll_list = sorted(self.all_polls[state], key = itemgetter('end_date'))
                        self.all_polls[state] = poll_list
                #self.all_polls = sorted(self.all_polls, key=itemgetter('end_date'))
                #DEBUGGING
                print len(self.all_polls)
                

	def dumpPolls(self):
		if(self.all_polls == []):
			print "self.all_polls has not been populated. Run queryPolls first!"
		else:
			for result in self.all_polls:
				print "\n\nPOLL:\n" + str(result)
			return self.all_polls

	def pushToCassandra(self):
		if(self.all_polls == []):
			print "No polls were found for the specified date range"
		else:
			#grab the last unique ID to increment it for the primary key
			#f = open('PollID_DONOTTOUCH.txt', 'r+')
			#ID = int(f.read())
                        tempIDlist = list(session.execute("SELECT id FROM president"))
                        IDlist = []
                        for row in tempIDlist: IDlist.append(row.id)
                        if(len(IDlist) == 0):
                                ID = 0
                        else:
                                IDlist.sort()
                                IDlist.reverse()
                                ID = IDlist[0] + 1
                                
                        print("last ID: " + str(ID - 1))
                        
			for poll in self.all_polls:
				temp_pollster = poll['pollster']
				temp_start_date = poll['start_date']
				temp_end_date = poll['end_date']
				temp_name = poll['name']
				temp_observations = poll['observations']
				temp_responses = poll['responses']
                                
                                cql = "INSERT INTO president (pollster, id, start_date, end_date, name, observations, responses) VALUES (%s, %s, %s, %s, %s, %s, %s)"
				session.execute(cql, (temp_pollster, ID, temp_start_date, temp_end_date, temp_name, temp_observations, temp_responses))
				
				ID += 1
                #f.seek(0)
                #f.write(str(ID))
def main():
	#usage message if there are no arguments
	if(len(sys.argv) != 3 and len(sys.argv) != 2):
		print 'Usage: python PollGrabber.py <start_date> <end_date>'
                print 'OR'
                print 'Usage: python PollGrabber.py day'
                print 'Using the "day" argument gets the polls from yesterday'
		print 'Date format: YYYY-MM-DD'

        elif(len(sys.argv) == 2 and sys.argv[1] == 'yesterday'):
                #just check for polls during the last day
                today = time.strftime('%Y-%m-%d')
                yesterday = date.today() - timedelta(1)
                yesterday = yesterday.strftime('%Y-%m-%d')
                pg = pollGrabber(yesterday, today)
                pg.queryPolls()
#                pg.pushToCassandra()
	else:
		#get the current date so we can pass in yesterday's as the end date
                
                pg = pollGrabber(sys.argv[1], sys.argv[2])
		pg.queryPolls()
#		pg.pushToCassandra()

if __name__ == "__main__":
    main()
