#Steps to start up the OpenStack

#1. Launch Spark
##Step 1: On Machine 1, navigate to the directory /home/centos/spark-1.5.1-bin-hadoop2.6/sbin
##Step 2: Now run the command ./start-all.sh
---
---
#2. Launch Cassandra
##Step 1: On Machine 2, navigate to the directory /home/centos/dse-4.8.1/bin
##Step 2: now run the command sudo ./dse cassandra -t, and wait a while until you see the last three following lines:
###INFO  05:06:59  SparkClusterInfo plugin using 1 async writers
###INFO  05:06:59  Initializing data object io tracker plugin
###INFO  05:06:59  Hive metastore version: 1
##Step 3: On Machine 2, navigate to the directory /home/centos/dse-4.8.1/bin
##Step 4: now run the command sudo ./dse cassandra, and wait a while until you see the last three following lines:
###INFO  05:06:59  SparkClusterInfo plugin using 1 async writers
###INFO  05:06:59  Initializing data object io tracker plugin
###INFO  05:06:59  Hive metastore version: 1
#
#Now you are ready to use Spark and Cassandra!
