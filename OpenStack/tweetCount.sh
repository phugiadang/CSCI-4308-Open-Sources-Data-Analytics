#!/bin/bash

#PATH=/sbin:/bin:/usr/sbin:/usr/bin:/home/centos/CSCI-4308-Open-Sources-Data-Analytics/OpenStack
PATH=/sbin:/bin:/usr/sbin:/usr/bin:/home/centos/CSCI-4308-Open-Sources-Data-Analytics/OpenStack:/home/centos/dse-4.8.1/bin:/home/centos/spark-1.5.1-bin-hadoop2.6
HOME=/


c=$(ps aux | grep trump.py | wc | cut -d ' ' -f 7)
if [ $c -eq 1 ]
then
        /home/centos/spark-1.5.1-bin-hadoop2.6/trump.py &
fi


tweetcount=$(echo "USE junk; select count(*) from trump;" | /home/centos/dse-4.8.1/bin/cqlsh 128.138.202.117 | tail -n 3 | head -n 1 | cut -d ' ' -f 2)

b="\#Number of Trump Tweets: $tweetcount"

sudo sh -c "echo $b > tweetCount.md"
git add tweetCount.md &> /dev/null
git commit -m "updated tweet count" &> /dev/null
git config credential.helper store
git push &> /dev/null
#"Username for 'https://github.com': "
#expect -exact "Username for 'https://github.com': "
#send "commandoscorch16"
#expect "Password for 'https://commandoscorch16@github.com':"
#send "$password"
