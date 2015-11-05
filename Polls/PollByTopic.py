from pollster import Pollster
from datetime import date
import sys

pollster = Pollster()

def pollByTopic(name):
	for x in pollster.charts(topic = name):
		print ('Poll Category:\n')
		for y in x.estimates_by_date():
			print y



if(len(sys.argv) != 2):
	print 'Usage: python PollByTopic.py <poll_topic>'
	print 'Use flag -showall in place of <poll_topic> to see all topics'
elif(sys.argv[1] == '-showall'):
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
	pollByTopic(sys.argv[1])
