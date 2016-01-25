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
		self.allPolls = []

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
			# pollsByDate = chart.estimates_by_date()
			polls = chart.polls()
			for poll in polls:

				#grab and format the current poll's date
				pollStart = poll.start_date.split('-', 2)
		 		pollStart = date(int(pollStart[0]), int(pollStart[1]), int(pollStart[2]))
		 		pollEnd = poll.end_date.split('-', 2)
		 		pollEnd = date(int(pollEnd[0]), int(pollEnd[1]), int(pollEnd[2]))
				#check if it's in the date range
				if(pollEnd < end and pollStart > start):
					new = {'pollster': '', 'startDate': '', 'endDate': '', 'name': '', 'observations': '', 'responses': []}
					new['pollster'] = poll.pollster
					new['startDate'] = poll.start_date
					new['endDate'] = poll.end_date
					new['name'] = poll.questions[0]['name']
					new['observations'] = poll.questions[0]['subpopulations'][0]['observations']
					new['responses'] = poll.questions[0]['subpopulations'][0]['responses']
					self.allPolls.append(new)

	def getPolls(self):
		if(self.allPolls == []):
			print "self.allPolls has not been populated. Run queryPolls first!"
		else:
			for result in self.allPolls:
				print "\n\nPOLL:\n" + str(result)
			return self.allPolls

	def pushToCassandra(self):
		if(self.allPolls == []):
			print "self.allPolls has not been populated. Run queryPolls first!"
		else:
			for poll in self.allPolls:
				tempPollster = poll['pollster']
				tempStartDate = poll['startDate']
				tempEndDate = poll['endDate']
				tempName = poll['name']
				tempObservations = poll['observations']
				tempResponses = poll['responses']

				session.execute("INSERT INTO polls (pollster, startDate, endDate, name, observations, responses) VALUES (%s, %s, %s, %s, %s, %s)", (tempPollster, tempStartDate, tempEndDate, tempName, tempObservations, tempResponses))
				print "Inserted a poll"

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
		pg.getPolls()
		pg.pushToCassandra()

if __name__ == "__main__":
    main()