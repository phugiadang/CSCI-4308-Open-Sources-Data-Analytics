from pyspark_cassandra import CassandraSparkContext, Row
from pyspark import SparkContext, SparkConf
import json
import sys
import time

#Example Usage(will get tweets from Jan 22 but not 24):
# *.py "Jan 22" "Jan 24" 

startDate = str(sys.argv[1])
endDate = str(sys.argv[2])

conf = SparkConf() \
    .setAppName("User Food Migration") \
    .setMaster("spark://128.138.202.110:7077") \
    .set("spark.cassandra.connection.host", "128.138.202.117")

sc = CassandraSparkContext(conf=conf)

if __name__ == '__main__': 

    rdd = sc.cassandraTable("junk", "bernie4") 
    temp = 0
    #returns list of tweets
    listBernie = rdd.filter(lambda row: row.created_at[4:] > startDate).filter(lambda row: row.created_at[4:] < endDate).collect()
    for tweet in listBernie:
        if tweet.retweet_count > 0:
	    print tweet.retweet_count
            temp += 1
        if tweet.favorite_count > 0:
            print tweet.favorite_count
            temp += 1
        if tweet.coordinates != None:
            print tweet.coordinates
            temp += 1
        if tweet.quoted_status_id != None:
            print tweet.quoted_status_id
            temp += 1
    #returns number ofabove things that aren't 0 or None
    print "temp is", temp	

    #returns count
    print rdd.filter(lambda row: row.created_at[4:] > startDate).filter(lambda row: row.created_at[4:] < endDate).count()

