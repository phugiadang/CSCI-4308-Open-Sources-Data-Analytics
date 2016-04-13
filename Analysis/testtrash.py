from cassandra.cluster import Cluster

keyspace = 'candidates'
cluster = Cluster(
        contact_points=['128.138.202.110','128.138.202.117'],)
#connect to our Cassandra Keyspace
session = cluster.connect(keyspace)
session.default_timeout = 600



def main():

        file1=open("listOfTweetIds.txt","w+")
        
        final_result = session.execute("select tweet_id from trump");

        count=0
        for x in final_result:
            count += 1
            file1.write(str(x[0])+"\n")


        print count

main()
