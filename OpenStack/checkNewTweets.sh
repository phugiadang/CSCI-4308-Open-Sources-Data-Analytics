#!/bin/bash

old_trump=$(cat /home/centos/oldTrumpCount.txt)
old_carson=$(cat /home/centos/oldCarsonCount.txt)
old_sanders=$(cat /home/centos/oldSandersCount.txt)
old_clinton=$(cat /home/centos/oldClintonCount.txt)
old_cruz=$(cat /home/centos/oldCruzCount.txt)
old_kasich=$(cat /home/centos/oldKasichCount.txt)
old_rubio=$(cat /home/centos/oldRubioCount.txt)
old_bush=$(cat /home/centos/oldBushCount.txt)

trump=$(cat /home/centos/CSCI-4308-Open-Sources-Data-Analytics/trumpTweetCount.txt)
carson=$(cat /home/centos/CSCI-4308-Open-Sources-Data-Analytics/carsonTweetCount.txt)
sanders=$(cat /home/centos/CSCI-4308-Open-Sources-Data-Analytics/sandersTweetCount.txt)
clinton=$(cat /home/centos/CSCI-4308-Open-Sources-Data-Analytics/clintonTweetCount.txt)
cruz=$(cat /home/centos/CSCI-4308-Open-Sources-Data-Analytics/cruzTweetCount.txt)
kasich=$(cat /home/centos/CSCI-4308-Open-Sources-Data-Analytics/kasichTweetCount.txt)
rubio=$(cat /home/centos/CSCI-4308-Open-Sources-Data-Analytics/rubioTweetCount.txt)
bush=$(cat /home/centos/CSCI-4308-Open-Sources-Data-Analytics/bushTweetCount.txt)

bad=0


echo $old_clinton
echo $clinton

if [ "$old_trump" -eq "$trump" ]
then
    bad=1
    echo "bad trump"
elif [ "$old_carson" -eq "$carson" ]
then
    bad=1
    echo "bad carson"
elif [ "$old_sanders" -eq "$sanders" ]
then
    bad=1
    echo "bad sanders"
elif [ "$old_clinton" -eq "$clinton" ]
then
    bad=1
    echo "bad clinton"
elif [ "$old_cruz" -eq "$cruz" ]
then
    bad=1
elif [ "$old_kasich" -eq "$kasich" ]
then
    bad=1
elif [ "$old_bush" -eq "$bush" ]
then
    bad=1
elif [ "$old_rubio" -eq "$rubio" ]
then
    bad=1

else
#Update the old values
cat /home/centos/CSCI-4308-Open-Sources-Data-Analytics/trumpTweetCount.txt > /home/centos/oldTrumpCount.txt

cat /home/centos/CSCI-4308-Open-Sources-Data-Analytics/carsonTweetCount.txt > /home/centos/oldCarsonCount.txt

cat /home/centos/CSCI-4308-Open-Sources-Data-Analytics/cruzTweetCount.txt > /home/centos/oldCruzCount.txt

cat /home/centos/CSCI-4308-Open-Sources-Data-Analytics/clintonTweetCount.txt > /home/centos/oldClintonCount.txt

cat /home/centos/CSCI-4308-Open-Sources-Data-Analytics/sandersTweetCount.txt > /home/centos/oldSandersCount.txt

cat /home/centos/CSCI-4308-Open-Sources-Data-Analytics/rubioTweetCount.txt > /home/centos/oldRubioCount.txt

cat /home/centos/CSCI-4308-Open-Sources-Data-Analytics/bushTweetCount.txt > /home/centos/oldBushCount.txt

cat /home/centos/CSCI-4308-Open-Sources-Data-Analytics/kasichTweetCount.txt > /home/centos/oldKasichCount.txt
 
fi #End ugly if 



if [ $bad -eq 1 ]
then
echo 'Killing threadCass.py'
#pid=$(ps aux | grep threadCass.py | cut -d ' ' -f 4)
#pid=$(ps aux | grep threadCass.py | head -1 | cut -d ' ' -f 5)
pid=$(ps aux | grep threadCass.py | head -1 | tr -s " " | cut -d ' ' -f 2)
echo $pid
sudo kill $pid
sudo ./home/centos/CSCI-4308-Open-Sources-Data-Analytics/zero.sh
echo "Bad" | mail -s "A thread stopped its streaming, killing threadCass.py" captainrex1995@gmail.com
#kill threadCass.py

else
echo 'Everything Good!'

fi

