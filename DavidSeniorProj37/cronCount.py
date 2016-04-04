
from cassandra.cluster import Cluster
from time import gmtime, strftime


keyspace = 'candidates'
cluster = Cluster(contact_points=['128.138.202.110','128.138.202.117'],)
session = cluster.connect(keyspace)
session.default_timeout = 2000.00

#for months in listOfMonths:
#    print months
 #date = "select count(*) from "+candidate+" where created_at > 2016"+month+str(day)+"000000 and created_at < 2016"+ month + str(day+1) + "000000 ALLOW FILTERING;"
hour = int(strftime("%H",  gmtime()))-1
if hour < 0:
	hour = 23
day = int(strftime("%d",  gmtime()))
if hour == 23:
	day = day - 1
year =  int(strftime("%Y", gmtime()))
month = int(strftime("%m", gmtime()))
monthInt = month
if month < 10:
    stringMonth = "0"+str(month)
if month >= 10:
    stringMonth = str(month)
month = stringMonth

#candidate = "sanders"
#trump still needs doing
#candidates = ["sanders"]
candidates = ["trump","sanders","clinton","bush","kasich","cruz","rubio"]
#candidates = ["trump"]
#for day in range (1,listOfMonths[1]+1):
#for day in range (1,29):
#day = 20
for candidate in candidates:
    if day < 10:
        dayOfMonth = "0" + str(day)
        dayPlusOne = "0" + str(day+1)
    if day == 9:
        dayPlusOne = str(day+1)
    if day > 10:
        dayOfMonth = str(day)
        dayPlusOne = str(day+1)
    if hour == 9:
        date = "select count(*) from "+candidate+" where created_at > 2016"+month+dayOfMonth+"0"+str(hour)+"0000 and created_at < 2016"+ month + dayOfMonth+str(hour+1)+"0000 ALLOW FILTERING;"
        print date
    else:
	    if hour < 9:
	        date = "select count(*) from "+candidate+" where created_at > 2016"+month+dayOfMonth+"0"+str(hour)+"0000 and created_at < 2016"+ month + dayOfMonth + "0"+str(hour+1)+"0000 ALLOW FILTERING;"
	        print date
	    else: 
	        if hour <23:
	            date = "select count(*) from "+candidate+" where created_at > 2016"+month+dayOfMonth+str(hour)+"0000 and created_at < 2016"+ month + dayOfMonth+str(hour+1)+"0000 ALLOW FILTERING;"
	            print date
	        if hour==23:
	            date = "select count(*) from "+candidate+" where created_at > 2016"+month+dayOfMonth+str(hour)+"0000 and created_at < 2016"+ month + dayOfMonth+str(hour)+"5900 ALLOW FILTERING;"
	            print date

    rows = session.execute(date)
    for user_row in rows:
        for count in rows:
            print str(count.count) + " The candidate is "+candidate 
            myCount = count.count
    insertString = "INSERT INTO counts (candidate, year, month, day,hour,count)VALUES (%s,%s,%s,%s,%s,%s)"""
    if myCount != 0:
		session.execute(insertString,(candidate,year,monthInt,day,hour,myCount))
    print "completed INsert"
        #print date
#day = 13

month = 2

#insertString = "INSERT INTO users (candidate, year, month, day,hour,count)"+"VALUES ("+candidate+", "+str(year)+", "+str(month)+", "+str(day)+", "+str(hour)+", "+str(myCount) +");"

#print insertString




#date = "select count(*) from "+candidate+" where created_at > 2016"+month+str(day)+"000000 and created_at < 2016"+ month + str(day+1) + "000000 ALLOW FILTERING;"
#for x in range(1,31):
#    if x < 10:
        

