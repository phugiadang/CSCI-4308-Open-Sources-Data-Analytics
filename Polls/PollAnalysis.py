#from pollster import Pollster 
#from datetime import date
from cassandra.cluster import Cluster
import sys

cluster = Cluster(['128.138.202.110', '128.138.202.117'])
session = cluster.connect('polls')

# cql = "SELECT name FROM junk.polls"
# print cql
# rows = session.execute(cql)
# for row in rows:
# 	print row

# cql = "SELECT name FROM junk.polls WHERE startDate = '2014-01-10'"
# print cql
# rows = session.execute(cql)
# for row in rows:
# 	print row

# cql = "SELECT name FROM junk.polls WHERE name = 'Obama Job Approval'"
# print cql
# try:
# 	rows = session.execute(cql)
# 	for row in rows:
# 		print row
# except:
# 	print "This throws an error because we're restricting part of the primary key without restricting a previous part. The primary key is (startDate, endDate, name) so we have to restrict them in that order."

allResponses = []
averageResponses = {}
numResponses = {}

cql = "SELECT responses FROM polls.president"
rows = session.execute(cql)
numRows = 0
for row in rows:
	numRows += 1
	for item in row:
		response = eval(item)
		allResponses.append(response)

for response in allResponses:
	for candidate in response:
		if(candidate['choice'] not in averageResponses):
			averageResponses[candidate['choice']] = candidate['value']
			numResponses[candidate['choice']] = 1
		else:
			averageResponses[candidate['choice']] += candidate['value']
			numResponses[candidate['choice']] += 1

#divide the values in averageResponses (currently the sum of responses) by the
#actual number of responses about the candidate to get the average

for candidate in averageResponses:
        averageResponses[candidate] = averageResponses[candidate]/numResponses[candidate]

#print averageResponses

#cql = "SELECT responses FROM junk.polls WHERE startDate = '2014-01-10'"
#rows = session.execute(cql)
#for row in rows:
#        for item in row:
                #eval() turns the string back into the nested list and dictionary
                #There's probably a more efficient way to do this... eg saving the values as something other than a string
#		evaluated =  eval(item)
#                print evaluated[0]['first_name']


