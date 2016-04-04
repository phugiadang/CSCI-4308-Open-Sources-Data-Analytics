from cassandra.cluster import Cluster
import datetime
def UtcNow():
    now = datetime.datetime.utcnow()
    return now

keyspace = 'candidates'
cluster = Cluster(contact_points=['128.138.202.110','128.138.202.117'],)
#cluster = Cluster(contact_points=['128.138.202.110'],)

#cluster = Cluster(contact_points=['128.138.202.110'],)
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
datehour8 = ""

monthInt = 3
#candidate = "sanders"
#trump still needs doing
#candidates = ["sanders"]
#"trump"
candidates = ["trump","sanders","clinton","bush","kasich","cruz","rubio"]


#candidates = []
#for day in range (1,listOfMonths[1]+1):
#for day in range (1,29):
day = 20
for candidate in candidates:
    for day in range (0,18):
        hour = 9
        date = "select count from counts where candidate = '"+candidate+ "' and year = 2016 and month = 3 and day = "+ str(day) + " and hour = "+str(hour) +";"
        #date = "select count(*) from "+candidate+" where created_at > 2016"+month+dayOfMonth+"0"+str(hour)+"0000 and created_at < 2016"+ month + dayOfMonth+str(hour+1)+"0000 ALLOW FILTERING;"
        hour = 8
        dateHour8 = "select count from counts where candidate = '"+candidate+ "' and year = 2016 and month = 3 and day = "+ str(day) + " and hour = "+str(hour) +";"
        #print dateHour8          
        myCount = 0
        myCount8 = 0
        rows = session.execute(date)
        for user_row in rows:
            for count in rows:
                #print str(count.count) + " The candidate is " + candidate
                myCount = count.count
                #print myCount
               
        rows = session.execute(dateHour8)
        for user_row in rows:
            for count in rows:
                #print str(count.count) + " The candidate is " + candidate 
                myCount8 = count.count
                print str(myCount8) + " wooooooo"
        
        if myCount8 ==0:
            hour = 10
            dateHour8 = "select count from counts where candidate = '"+candidate+ "' and year = 2016 and month = 3 and day = "+ str(day) + " and hour = "+str(hour) +";"
            rows = session.execute(dateHour8)
            for user_row in rows:
                for count in rows:
                #print str(count.count) + " The candidate is " + candidate 
                    myCount8 = count.count
                    print str(myCount8) + " wooooooo"
                    
        
        
        #if (myCount != None and myCount8 != None and 3*myCount8 < myCount):
        if(myCount != None and myCount8 != None and myCount ==0):
            print myCount
            print myCount8
        #    print myCount
            #insertString = "INSERT INTO counts (candidate, year, month, day,hour,count)VALUES (%s,%s,%s,%s,%s,%s)"""
            print str(myCount) + "should be huge"
            hour = 9
            #session.execute(insertString,(candidate,year,monthInt,day,hour,myCount8))
            #insertString = "INSERT INTO counts (candidate, year, month, day,hour,count)VALUES (%s,%s,%s,%s,%s,%s)"""
            #session.execute(insertString,(candidate,year,monthInt,day,hour,myCount8))
            print "completed Insert"

        #select count from c
