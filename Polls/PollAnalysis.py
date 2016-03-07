#from pollster import Pollster 
#from datetime import date
from cassandra.cluster import Cluster
import sys

cluster = Cluster(['128.138.202.110', '128.138.202.117'])
session = cluster.connect('polls')

cql = "SELECT * FROM polls.president"
rows = session.execute(cql)



for row in rows:
    responses = eval(row.responses)
    name = row.name
    if 'Republican' in name:
        #get rid of options that aren't Clinton or Sanders
        for choice in responses:
            if choice['choice'] not in ['Undecided', 'Refused', 'Other', 'Wouldn\'t vote', 'Wouldn\'t Vote', 'No Answer', 'Other/undecided', 'Other/Undecided', 'Don\'t Know', 'Not Sure', 'Someone else/Not sure', 'Uncommitted', 'Not Voting', 'Not voting']:
                print choice['choice'] + ', Number of choices: ' + str(len(responses))

#save results for each candidate by number of responses, eg. ['Sanders', '4', '30'] where second argument is the number of options in that poll and 30 is the votes for Sanders
