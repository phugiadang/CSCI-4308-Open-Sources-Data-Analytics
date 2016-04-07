#!/bin/bash

old_trump=$(cat /home/centos/CSCI-4308-Open-Sources-Data-Analytics/candidateCounts/oldTrumpCount.txt)
old_carson=$(cat /home/centos/CSCI-4308-Open-Sources-Data-Analytics/candidateCounts/oldCarsonCount.txt)
old_sanders=$(cat /home/centos/CSCI-4308-Open-Sources-Data-Analytics/candidateCounts/oldSandersCount.txt)
old_clinton=$(cat /home/centos/CSCI-4308-Open-Sources-Data-Analytics/candidateCounts/oldClintonCount.txt)
old_cruz=$(cat /home/centos/CSCI-4308-Open-Sources-Data-Analytics/candidateCounts/oldCruzCount.txt)
old_kasich=$(cat /home/centos/CSCI-4308-Open-Sources-Data-Analytics/candidateCounts/oldKasichCount.txt)
old_rubio=$(cat /home/centos/CSCI-4308-Open-Sources-Data-Analytics/candidateCounts/oldRubioCount.txt)
old_bush=$(cat /home/centos/CSCI-4308-Open-Sources-Data-Analytics/candidateCounts/oldBushCount.txt)

trump=$(cat /home/centos/CSCI-4308-Open-Sources-Data-Analytics/candidateCounts/trumpTweetCount.txt)
carson=$(cat /home/centos/CSCI-4308-Open-Sources-Data-Analytics/candidateCounts/carsonTweetCount.txt)
sanders=$(cat /home/centos/CSCI-4308-Open-Sources-Data-Analytics/candidateCounts/sandersTweetCount.txt)
clinton=$(cat /home/centos/CSCI-4308-Open-Sources-Data-Analytics/candidateCounts/clintonTweetCount.txt)
cruz=$(cat /home/centos/CSCI-4308-Open-Sources-Data-Analytics/candidateCounts/cruzTweetCount.txt)
kasich=$(cat /home/centos/CSCI-4308-Open-Sources-Data-Analytics/candidateCounts/kasichTweetCount.txt)
rubio=$(cat /home/centos/CSCI-4308-Open-Sources-Data-Analytics/candidateCounts/rubioTweetCount.txt)
bush=$(cat /home/centos/CSCI-4308-Open-Sources-Data-Analytics/candidateCounts/bushTweetCount.txt)

bad=0
cand=''

echo $old_clinton
echo $clinton

if [ "$old_trump" -eq "$trump" ]
then
    bad=1
    cand="trump"
    echo "bad trump"
elif [ "$old_carson" -eq "$carson" ]
then
    bad=1
    cand="carson"
    echo "bad carson"
elif [ "$old_sanders" -eq "$sanders" ]
then
    bad=1
    cand="sanders"
    echo "bad sanders"
elif [ "$old_clinton" -eq "$clinton" ]
then
    bad=1
    cand="clinton"
    echo "bad clinton"
elif [ "$old_cruz" -eq "$cruz" ]
then
    bad=1
    cand="cruz"
elif [ "$old_kasich" -eq "$kasich" ]
then
    bad=1
    cand="kasich"
elif [ "$old_bush" -eq "$bush" ]
then
    bad=1
    cand="kasich"
elif [ "$old_rubio" -eq "$rubio" ]
then
    bad=1
    cand="rubio"

else


#Update the old values
cat /home/centos/CSCI-4308-Open-Sources-Data-Analytics/candidateCounts/trumpTweetCount.txt > /home/centos/CSCI-4308-Open-Sources-Data-Analytics/candidateCounts/oldTrumpCount.txt

cat /home/centos/CSCI-4308-Open-Sources-Data-Analytics/candidateCounts/carsonTweetCount.txt > /home/centos/CSCI-4308-Open-Sources-Data-Analytics/candidateCounts/oldCarsonCount.txt

cat /home/centos/CSCI-4308-Open-Sources-Data-Analytics/candidateCounts/cruzTweetCount.txt > /home/centos/CSCI-4308-Open-Sources-Data-Analytics/candidateCounts/oldCruzCount.txt

cat /home/centos/CSCI-4308-Open-Sources-Data-Analytics/clintonTweetCount.txt > /home/centos/CSCI-4308-Open-Sources-Data-Analytics/candidateCounts/oldClintonCount.txt

cat /home/centos/CSCI-4308-Open-Sources-Data-Analytics/candidateCounts/sandersTweetCount.txt > /home/centos/CSCI-4308-Open-Sources-Data-Analytics/candidateCounts/oldSandersCount.txt

cat /home/centos/CSCI-4308-Open-Sources-Data-Analytics/candidateCounts/rubioTweetCount.txt > /home/centos/CSCI-4308-Open-Sources-Data-Analytics/candidateCounts/oldRubioCount.txt

cat /home/centos/CSCI-4308-Open-Sources-Data-Analytics/candidateCounts/bushTweetCount.txt > /home/centos/CSCI-4308-Open-Sources-Data-Analytics/candidateCounts/oldBushCount.txt

cat /home/centos/CSCI-4308-Open-Sources-Data-Analytics/candidateCounts/kasichTweetCount.txt > /home/centos/CSCI-4308-Open-Sources-Data-Analytics/candidateCounts/oldKasichCount.txt
 
fi #End ugly if 



if [ $bad -eq 1 ]
then
echo 'Killing threadCass.py'
#pid=$(ps aux | grep threadCass.py | cut -d ' ' -f 4)
#pid=$(ps aux | grep threadCass.py | head -1 | cut -d ' ' -f 5)
pid=$(ps aux | grep "[p]ython threadCass.py" | head -1 | tr -s " " | cut -d ' ' -f 2)
echo $pid
sudo kill $pid
cd /home/centos/CSCI-4308-Open-Sources-Data-Analytics 
sudo ./zero.sh
echo "Bad $cand" | mail -s "$cand stopped streaming, killing threadCass.py" captainrex1995@gmail.com
#kill threadCass.py

else
echo 'Everything Good!'

fi

