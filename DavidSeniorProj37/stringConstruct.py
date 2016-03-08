from cassandra.cluster import Cluster
import datetime
def UtcNow():
    now = datetime.datetime.utcnow()
    return now

keyspace = 'candidates'
cluster = Cluster(contact_points=['128.138.202.110','128.138.202.117'],)
session = cluster.connect(keyspace)
session.default_timeout = 2000.00

January = 31
February = 29
March = 31
April = 30
May = 31
June = 30
July = 31
August = 31
September = 30
October = 31
November = 30
December = 31

listOfMonths = []
listOfMonths.append(January)
listOfMonths.append(February)
listOfMonths.append(March)
listOfMonths.append(April)
listOfMonths.append(May)
listOfMonths.append(June)
listOfMonths.append(July)
listOfMonths.append(August)
listOfMonths.append(September)
listOfMonths.append(October)
listOfMonths.append(November)
listOfMonths.append(December)

#for months in listOfMonths:
#    print months
 #date = "select count(*) from "+candidate+" where created_at > 2016"+month+str(day)+"000000 and created_at < 2016"+ month + str(day+1) + "000000 ALLOW FILTERING;"
year = 2016
date = ""
month = "03"
monthInt = 3
#candidate = "sanders"
#trump still needs doing
#candidates = ["sanders"]

candidates = ["trump","sanders","clinton","bush","kasich","cruz","rubio"]
#candidates = []
#for day in range (1,listOfMonths[1]+1):
#for day in range (1,29):
day = 20
for candidate in candidates:
    for day in range (7,9):
        if day < 10:
            dayOfMonth = "0" + str(day)
            dayPlusOne = "0" + str(day+1)
        if day == 9:
            dayPlusOne = str(day+1)
        if day > 10:
            dayOfMonth = str(day)
            dayPlusOne = str(day+1)
        for hour in range(0,24):
            #print hour
            if hour == 9:
                date = "select count(*) from "+candidate+" where created_at > 2016"+month+dayOfMonth+"0"+str(hour)+"0000 and created_at < 2016"+ month + dayOfMonth+str(hour+1)+"0000 ALLOW FILTERING;"
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
                    print str(count.count) + " The candidate is " + candidate 
                    myCount = count.count
            insertString = "INSERT INTO counts (candidate, year, month, day,hour,count)VALUES (%s,%s,%s,%s,%s,%s)"""
            if myCount != 0:
                session.execute(insertString,(candidate,year,monthInt,day,hour,myCount))
            print "completed Insert"

