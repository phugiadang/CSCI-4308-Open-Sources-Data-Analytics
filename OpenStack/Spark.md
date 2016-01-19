#How to run our tweet streaming program
---
##1. cd /home/centos/spark-1.5.1-bin-hadoop2.6
---
## Now run this command, where <name_of_python_file> is the name of the file to run, like trump.py for instance
##2. bin/pyspark --packages com.datastax.spark:spark-cassandra-connector_2.11:1.5.0-M2 --packages TargetHolding:pyspark-cassandra:0.1.5 <name_of_python_file>
