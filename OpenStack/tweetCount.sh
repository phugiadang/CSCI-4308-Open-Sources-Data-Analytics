#!/bin/bash

#PATH=/sbin:/bin:/usr/sbin:/usr/bin:/home/centos/CSCI-4308-Open-Sources-Data-Analytics/OpenStack
PATH=/sbin:/bin:/usr/sbin:/usr/bin:/home/centos/CSCI-4308-Open-Sources-Data-Analytics/OpenStack:/home/centos/dse-4.8.1/bin:/home/centos/spark-1.5.1-bin-hadoop2.6
HOME=/

cd /home/centos/CSCI-4308-Open-Sources-Data-Analytics/OpenStack


password=$(python hash.py)
#c=$(ps aux | grep trump.py | wc | cut -d ' ' -f 7)
#if [ $c -eq 1 ]
#then
#        sudo sh -c "/home/centos/spark-1.5.1-bin-hadoop2.6/bin/pyspark --packages com.datastax.spark:spark-cassandra-connector_2.11:1.5.0-M2 --packages TargetHolding:pyspark-cassandra:0.1.5 /home/centos/spark-1.5.1-bin-hadoop2.6/trump.py"
#fi


#tweetcount=$(echo "USE junk; select count(*) from trump;" | /home/centos/dse-4.8.1/bin/cqlsh 128.138.202.117 | tail -n 3 | head -n 1 | cut -d ' ' -f 2)

tweetcount=$(cat /home/centos/spark-1.5.1-bin-hadoop2.6/trumpTweetCount.txt)


b="\#Number of Trump Tweets: $tweetcount"


sudo sh -c "echo $b > tweetCount.md"
git add tweetCount.md &> /dev/null
git commit -m "updated tweet count" &> /dev/null
sudo git push https://CommandoScorch16:dogworm16@github.com/phugiadang/CSCI-4308-Open-Sources-Data-Analytics
#git config credential.helper store
#git push &> /dev/null
#"Username for 'https://github.com': "
#expect -exact "Username for 'https://github.com': "
#send "commandoscorch16"
#expect "Password for 'https://commandoscorch16@github.com': "


#/usr/bin/expect -c 'expect "Password for 'https://commandoscorch16@github.com': " {git push &> /dev/null;send $password}'

#send "$password"
