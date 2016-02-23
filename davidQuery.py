from cassandra.cluster import Cluster
keyspace = 'candidates'
cluster = Cluster(
	contact_points=['128.138.202.110','128.138.202.117'],)
rows = session.execute('select count(*) from sanders where created_at > 20160210000000 and created_at < 20160214000000 ALLOW FILTERING;')

print rows
#for user_row in rows:
#    print user_row.name, user_row.age, user_row.email
#select count(*) from sanders where created_at > 20160210000000 and created_at < 20160214000000 ALLOW FILTERING;
