import sys
sys.path.append('/home/centos/CSCI-4308-Open-Sources-Data-Analytics')
import gdelt
import getDate
import calculateDate
from subprocess import call

date=getDate.getDate()
date=calculateDate.subDay(date+"000000")
date=date[:8]
print '\napples'+date+'oranges'
a="python gdelt.py -n \"kasich, rubio, sanders, clinton, bush, carson, cruz, trump\" -e " + str(date.replace("\n",""))

print a

call(a, shell=True) 


