#!/bin/bash

cd /home/centos/CSCI-4308-Open-Sources-Data-Analytics
a=$(python getDate.py)
a+="000000"
echo $a
a=$(python calculateDate.py -subDay $a)
#a="20160309000000"
b=${a::-6}

echo $b


python gdelt.py -n "kasich, rubio, sanders, clinton, bush, carson, cruz, trump" -e $b

python parseGDELT.py $b

