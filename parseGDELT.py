import sys, csv
from cassandra.cluster import Cluster

keyspace = 'candidates'
cluster = Cluster(
        contact_points=['128.138.202.110','128.138.202.117'],)
#connect to our Cassandra Keyspace
session = cluster.connect(keyspace)


date = '20160101'
if (len(sys.argv) == 2):
    date = sys.argv[1]

list_of_candidates=["kasich","bush","trump","clinton","sanders","cruz","carson","rubio"]


for name in list_of_candidates:

    #ex. open carson20160306.tsv
    count = 0
    with open("/VOLUME/GDELT/"+name+date+".tsv") as tsv_file:
        for line in csv.reader(tsv_file, dialect="excel-tab"):
            count += int(line[1])
            print line[1]
        print "%s: %d" % (name, count)
    final_step = session.execute_async('insert into ' + name + 'gdelt' + '(date, count) VALUES (%s, %s)', (int(date), count))

