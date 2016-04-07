#!/bin/bash

python /home/centos/CSCI-4308-Open-Sources-Data-Analytics/Analysis/jsonize.py Twitter all 0 0 0 hourly
python /home/centos/CSCI-4308-Open-Sources-Data-Analytics/Analysis/jsonize.py GDELT all 0 0 0 
python /home/centos/CSCI-4308-Open-Sources-Data-Analytics/Analysis/jsonize.py Polls all 0 0 0

python /home/centos/CSCI-4308-Open-Sources-Data-Analytics/Analysis/jsonize.py all Clinton 0 0 0
python /home/centos/CSCI-4308-Open-Sources-Data-Analytics/Analysis/jsonize.py all Sanders 0 0 0
python /home/centos/CSCI-4308-Open-Sources-Data-Analytics/Analysis/jsonize.py all Rubio 0 0 0
python /home/centos/CSCI-4308-Open-Sources-Data-Analytics/Analysis/jsonize.py all Kasich 0 0 0
python /home/centos/CSCI-4308-Open-Sources-Data-Analytics/Analysis/jsonize.py all Cruz 0 0 0
python /home/centos/CSCI-4308-Open-Sources-Data-Analytics/Analysis/jsonize.py all Trump 0 0 0
