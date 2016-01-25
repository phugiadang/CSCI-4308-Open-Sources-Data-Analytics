from pollster import Pollster 
from datetime import date
from cassandra.cluster import Cluster
import sys

cluster = Cluster(['128.138.202.110', '128.138.202.117'])
session = cluster.connect('junk')

cql = "SELECT name FROM junk.polls"
print cql
session.execute(cql)

cql = "SELECT name FROM junk.polls WHERE startDate = '2014-01-10'"
print cql
session.execute(cql)

cql = "SELECT name FROM junk.polls WHERE name = 'Obama Job Approval'"
print cql
try:
	session.execute(cql)
except:
	print "This throws an error because we're restricting part of the primary key without restricting a previous part. The primary key is (startDate, endDate, name) so we have to restrict them in that order."
