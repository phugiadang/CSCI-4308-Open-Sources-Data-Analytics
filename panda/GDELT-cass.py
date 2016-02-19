from cassandra.cluster import Cluster

cluster = Cluster(['128.138.202.110', '128.138.202.117'])
session = cluster.connect('demo')

result = session.execute("select * from users where lastname='Jones' ")[0]
print result.firstname, result.age;
