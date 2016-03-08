from cassandra.cluster import Cluster
keyspace = 'candidates'
cluster = Cluster(contact_points=['128.138.202.110','128.138.202.117'],)
session = cluster.connect(keyspace)


#rows = session.execute('select count(*) from sanders where created_at > 20160210000000 and created_at < 20160214000000 ALLOW FILTERING;')




month = "02"
day = 13
candidate = "sanders"
date = "select count(*) from "+candidate+" where created_at > 2016"+month+str(day)+"000000 and created_at < 2016"+ month + str(day+1) + "000000 ALLOW FILTERING;"
#string2 = 'select count(*) from sanders where created_at > 20160210000000 and created_at < 20160214000000 ALLOW FILTERING;'
print date
#print string2
rows = session.execute(date)
for user_row in rows:
    for count in rows:
        print count.count
        
