from subprocess import call
from cassandra.cluster import Cluster
import sys

cluster = Cluster(['128.138.202.110, 128.138.202.117'])
session = cluster.connect('polls')

cql = "SELECT COUNT(*) FROM polls.presidentbydate"

count = session.execute(cql)[0].count

call("echo " + str(count) + " | mail -s \"New Poll Count\" bryan.connelly@colorado.edu", shell=True)
