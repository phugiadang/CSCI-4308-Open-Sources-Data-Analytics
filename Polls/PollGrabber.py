from pollster import Pollster 
from datetime import date
from cassandra.cluster import Cluster
import sys

cluster = Cluster(['128.138.202.110', '128.138.202.117'])
session = cluster.connect('junk')

pollster = Pollster()

class pollGrabber:
	def __init__(self, t, sd, ed):
		self.topic = t
		self.start_date = sd
		self.end_date = ed
		self.all_polls = []

	def queryPolls(self):
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
		charts = pollster.charts(topic = self.topic)
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
				if(poll_end < end and poll_start > start):
					new = {'pollster': '', 'start_date': '', 'end_date': '', 'name': '', 'observations': '', 'responses': []}
					new['pollster'] = poll.pollster
					new['startDate'] = int(poll.start_date.replace('-', ''))
					new['endDate'] = int(poll.end_date.replace('-', ''))
					new['name'] = poll.questions[0]['name']
					new['observations'] = poll.questions[0]['subpopulations'][0]['observations']
					new['responses'] = str(poll.questions[0]['subpopulations'][0]['responses'])
					self.all_polls.append(new)

	def dumpPolls(self):
		if(self.all_polls == []):
			print "self.all_polls has not been populated. Run queryPolls first!"
		else:
			for result in self.all_polls:
				print "\n\nPOLL:\n" + str(result)
			return self.all_polls

	def pushToCassandra(self):
		if(self.all_polls == []):
			print "self.all_polls has not been populated. Run queryPolls first!"
		else:
			#grab the last unique ID to increment it for the primary key
			f = open('PollID_DONOTTOUCH.txt', 'r+')
			ID = int(f.read())

			for poll in self.all_polls:
				temp_pollster = poll['pollster']
				temp_start_date = poll['startDate']
				temp_end_date = poll['endDate']
				temp_name = poll['name']
				temp_observations = poll['observations']
				temp_responses = poll['responses']
                
                                cql = "INSERT INTO polls (id, pollster, start_date, end_date, name, observations, responses) VALUES (%s, %s, %s, %s, %s, %s, %s)"
				session.execute(cql, (ID, temp_pollster, temp_start_date, temp_end_date, temp_name, temp_observations, temp_responses))
				
				ID += 1
                f.seek(0)
                f.write(str(ID))
def main():
	#usage message if there are no arguments
	if(len(sys.argv) < 4 or len(sys.argv) > 4):
		print 'Usage: python QueryPolls.py <topic> <start_date> <end_date>'
		print 'Date format: YYYY-MM-DD'
		print 'All topics:'
		print 'obama-job-approval'
		print 'favorable-ratings'
		print '2016-senate-dem-primary'
		print '2016-senate'
		print '2016-president-gop-primary'
		print '2016-president-dem-primary'
		print '2016-president'
		print '2016 governor'
		print '2014-senate-primary'
		print '2014-senate-gop-primary'
		print '2014-senate-dem-primary'
		print '2014-governor'
		print '2013-senate-gop-primary'
		print '2013-senate-dem-primary'
		print '2013-senate'
		print '2013-house'
		print '2013-governor'
		print '2012-senate-gop-primary'
		print '2012-senate-dem-primary'
		print '2012-senate'
		print '2012-president-gop-primary'
		print '2012-president'
		print '2012-house'
		print '2012-governor-gop-primary'
		print '2012-governor-dem-primary'
		print '2012-governor'


	else:
		pg = pollGrabber(sys.argv[1], sys.argv[2], sys.argv[3])
		pg.queryPolls()
		#pg.getPolls()
		#pg.pushToCassandra()

if __name__ == "__main__":
    main()
