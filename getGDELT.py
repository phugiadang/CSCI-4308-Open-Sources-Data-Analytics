import gdelt
import getDate
import calculateDate
from subprocess import call

date=getDate.getDate()
date=calculateDate.subDay(date+"000000")
date=date[:8]
call("python gdelt.py -n \"kasich, rubio, sanders, clinton, bush, carson, cruz, trump\" -e " + date, shell=True) 


