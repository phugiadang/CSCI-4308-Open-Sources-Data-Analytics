from pollster import Pollster 
from datetime import date
import sys

pollster = Pollster()

def presPollsByDate(start, end):
	try:
		start = start.split('-', 2)
		start = date(int(start[0]), int(start[1]), int(start[2]))
		end = end.split('-', 2)
		end = date(int(end[0]), int(end[1]), int(end[2]))
	except:
		print 'Date could not be parsed correctly'
		print 'Make sure it is in the format YYYY-MM-DD'
		return
	pollCat = pollster.charts()[0].estimates_by_date()
	for x in range(1, len(pollCat)):
		poll = pollCat[x]
		pollDate = poll['date'].split('-', 2)
		pollDate = date(int(pollDate[0]), int(pollDate[1]), int(pollDate[2]))
		if(pollDate > start and pollDate < end):
			#print '\nPoll:\n' + str(poll) + '\n'
			#figure out who the winner was
			highestVal = 0
			winner = ''
			print 'Poll Values:'
			for y in poll['estimates']:
				print y
				if(y['value'] > highestVal):
					highestVal = y['value']
					winner = y['choice']
			print('Winner: ' + winner)

def pollsByPollster(Pollster):
	pollCat = pollster.charts()
	#iterate through every category of polls
	for x in pollCat:
		#iterate through all the polls in the category
		for y in x.polls():
			if(y.pollster == Pollster):
				print y

def pollsByTopic(name):
	for x in pollster.charts(topic = name):
		print x

def main():
	#usage message if there are no arguments
	if(len(sys.argv) == 1):
		print('Usage: python QueryPolls.py <queryType> <arguments>')
		print('where <queryType> is \'topic\', \'pollster\' or \'date\'')
		print('Try each queryType with no arguments to see usage messages')
	elif(sys.argv[1] == 'pollster' or sys.argv[1] == 'Pollster'):
		#sanity check argument length
		if(len(sys.argv) != 3):
			print 'Usage: python PollByPollster <pollster>'
			print 'If the pollster includes a space character, put it in quotes'
			print 'eg. <PPP (D)> won\'t work but <"PPP (D)"> will'
			print 'Pollsters are listed in Pollsters.txt'
		else:
			pollsByPollster(sys.argv[2])
	elif(sys.argv[1] == 'topic' or sys.argv[1] == 'Topic'):
		#sainty check argument length
		if(len(sys.argv) != 3):
			print 'Usage: python PollByTopic.py <poll_topic>'
			print 'Use \"python QueryPolls.py topic -showall\" to see all topics'
		elif(sys.argv[2] == '-showall'):
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
			pollsByTopic(sys.argv[2])
	elif(sys.argv[1] == 'date' or sys.argv[1] == 'Date'):
		#sanity check argument length
		if(len(sys.argv) != 4):
			print 'Usage: python PollByDate.py <start_date> <end_date>'
			print 'Date format: YYYY-MM-DD'
		else:
			presPollsByDate(sys.argv[2], sys.argv[3])
	else:
		print('Unknown query type, please try again')


if __name__ == "__main__":
    main()