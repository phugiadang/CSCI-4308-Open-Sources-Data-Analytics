import datetime
import os



today = str(datetime.date.today()).replace('-', '')
candidates = ['clinton', 'sanders', 'trump', 'cruz', 'kasich']

for candidate in candidates:
    os.system('python home/centos/CSCI-4308-Open-Sources-Data-Analytics/Analysis/TwitterGDELTGraphAnalysis.py ' + candidate + ' 20160301 ' + today + ' cronjob')
