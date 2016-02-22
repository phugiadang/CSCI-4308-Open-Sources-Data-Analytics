from sys import argv
import getDate
from cassandra.cluster import Cluster
from subprocess import call
import operator
import calculateDate

getCurrentDate = getDate.getDate
addMinute = calculateDate.changeMinute
keyspace = 'candidates'
cluster = Cluster(
        contact_points=['128.138.202.110','128.138.202.117'],)
#connect to our Cassandra Keyspace
session = cluster.connect(keyspace)
session.default_timeout = 100000

#list_of_candidates = ["trump", "rubio", "bush", "carson", "clinton", "kasich", "sanders", "cruz"]

list_of_candidates = ["trump"]

start_date = getCurrentDate()

end_date = start_date
for i in range(0, 10080):
    new_end_date = addMinute(end_date)
    end_date = new_end_date

print start_date
print end_date

#minute_count = session.execute('select * from kasichminuteaverages;')
#print minute_count[0][2]



for candidate in list_of_candidates:
    minute_count = session.execute('select count(*) from ' + candidate + ' where created_at >= ' + start_date + ' and created_at < ' + end_date + ' ALLOW FILTERING;')

    final_step = session.execute_async('insert into ' + candidate + 'WeeklyAverages ' + '(start_date, end_date, tweet_count) VALUES (%s, %s, %s)', (int(start_date), int(end_date), int(minute_count[0][0]) ))

