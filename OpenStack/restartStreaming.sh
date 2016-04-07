cd /home/centos/CSCI-4308-Open-Sources-Data-Analytics/OpenStack

c=$(ps aux | grep trump.py | wc | cut -d ' ' -f 7)
d=$(ps aux | grep threadCass.py | wc | cut -d ' ' -f 7)

if [ $c -eq 1 ]
then
         cd /home/centos/spark-1.5.1-bin-hadoop2.6
         
        # bin/pyspark --packages com.datastax.spark:spark-cassandra-connector_2.11:1.5.0-M2 --packages TargetHolding:pyspark-cassandra:0.1.5 trump.py

#        sudo sh -c "/home/centos/spark-1.5.1-bin-hadoop2.6/bin/pyspark --packages com.datastax.spark:spark-cassandra-connector_2.11:1.5.0-M2 --packages TargetHolding:pyspark-cassandra:0.1.5 /home/centos/spark-1.5.1-bin-hadoop2.6/trump.py"
fi

if [ $d -eq 1 ]
then
	cd /home/centos/CSCI-4308-Open-Sources-Data-Analytics/candidateCounts
        python threadCass.py
        pid=$(ps aux | grep "[p]ython threadCass.py" | head -1 | tr -s " " | cut -d ' ' -f 2)
        echo "Tweet Streaming Stopped, restarted with pid $pid!" | mail -s "Tweet Streaming Stopped, successfully restarted with pid $pid!" captainrex1995@gmail.com

fi

