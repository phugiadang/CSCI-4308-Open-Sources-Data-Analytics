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

#tweet_count=$(cat /home/centos/spark-1.5.1-bin-hadoop2.6/trumpTweetCount.txt)
total_tweet_count=$(cat /home/centos/CSCI-4308-Open-Sources-Data-Analytics/totalTweetCount.txt)
trump_tweet_count=$(cat /home/centos/CSCI-4308-Open-Sources-Data-Analytics/trumpTweetCount.txt | python commas.py)
sanders_tweet_count=$(cat /home/centos/CSCI-4308-Open-Sources-Data-Analytics/sandersTweetCount.txt | python commas.py)
cruz_tweet_count=$(cat /home/centos/CSCI-4308-Open-Sources-Data-Analytics/cruzTweetCount.txt | python commas.py)
clinton_tweet_count=$(cat /home/centos/CSCI-4308-Open-Sources-Data-Analytics/clintonTweetCount.txt | python commas.py)
rubio_tweet_count=$(cat /home/centos/CSCI-4308-Open-Sources-Data-Analytics/rubioTweetCount.txt | python commas.py)
carson_tweet_count=$(cat /home/centos/CSCI-4308-Open-Sources-Data-Analytics/carsonTweetCount.txt | python commas.py)
kasich_tweet_count=$(cat /home/centos/CSCI-4308-Open-Sources-Data-Analytics/kasichTweetCount.txt | python commas.py)
bush_tweet_count=$(cat /home/centos/CSCI-4308-Open-Sources-Data-Analytics/bushTweetCount.txt | python commas.py)

current_date=$(cat /home/centos/CSCI-4308-Open-Sources-Data-Analytics/startTime.txt)

#clinton_tweet_count=$(python commas.py $clinton_tweet_count)

#b=$"\#Total Tweets: $totalTweetCount \n\nNumber of Trump Tweets: $tweetcount"

#total_tweet_count=$(($bush_tweet_count + $kasich_tweet_count + $sanders_tweet_count + $clinton_tweet_count + $cruz_tweet_count + $carson_tweet_count + $rubio_tweet_count + $trump_tweet_count))

#sudo sh -c "echo $b > tweetCount.md"
sudo sh -c "printf \"#Current Stream Started at $current_date\n---\n---\n#Total Number of Tweets: $total_tweet_count \n---\n---\n#Number of Trump Tweets: $trump_tweet_count\n#Number of Sanders Tweets: $sanders_tweet_count\n#Number of Cruz Tweets: $cruz_tweet_count\n#Number of Clinton Tweets: $clinton_tweet_count\n#Number of Rubio Tweets: $rubio_tweet_count\n#Number of Carson Tweets: $carson_tweet_count\n#Number of Kasich Tweets: $kasich_tweet_count\n#Number of Jeb! Tweets: $bush_tweet_count\" > sortedNumbers.txt" 


sudo sh -c 'cat sortedNumbers.txt | sort -nrk5 > tempFiles.txt'

sudo python finalize.py

#sudo sh -c "printf \"#Total Tweets: $totalTweetCount \n---\n#Number of Trump Tweets: $trumpTweetCount\n#Number of Sanders Tweets: $sandersTweetCount\n#Number of Bush Tweets: $bushTweetCount\n#Number of Clinton Tweets: $clintonTweetCount\n#Number of Rubio Tweets: $rubioTweetCount\n#Number of Carson Tweets: $carsonTweetCount\n#Number of Kasich Tweets: $kasichTweetCount\n#Number of Jeb! Tweets: $bushTweetCount\" > tweetCount.md"


sudo git add * &> /dev/null #sortedNumbers.md &> /dev/null
sudo git commit -m "Updated candidate tweet count" &> /dev/null
sudo git push #https://CommandoScorch16:dogworm16@github.com/phugiadang/CSCI-4308-Open-Sources-Data-Analytics
#git config credential.helper store
#git push &> /dev/null
#"Username for 'https://github.com': "
#expect -exact "Username for 'https://github.com': "
#send "commandoscorch16"
#expect "Password for 'https://commandoscorch16@github.com': "


#/usr/bin/expect -c 'expect "Password for 'https://commandoscorch16@github.com': " {git push &> /dev/null;send $password}'

#send "$password"
