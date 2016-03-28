from cassandra.cluster import Cluster
import datetime
def UtcNow():
    now = datetime.datetime.utcnow()
    return now

keyspace = 'candidates'
#cluster = Cluster(contact_points=['128.138.202.110','128.138.202.117'],)
cluster = Cluster(contact_points=['128.138.202.110','128.138.202.117'],)
session = cluster.connect(keyspace)
session.default_timeout = 2000.00


def candidateGDELTCount(candidate,year, month, day):
    if len(str(month)) == 1:
        month = "0" + str(month)
    if len(str(day)) == 1:
        day = "0" + str(day)
        print day
    queryString = "select * from " + candidate + "GDELT where date = " + str(year) + str(month) + str(day) + ";"
    count = session.execute(queryString)
    print count[0][1]


def candidateCount(candidate, month,day,hour):
    queryString = "select count from counts where candidate = '"+str(candidate)+"' and year = 2016 and month = "+str(3)+" and day = "+str(day)+" and hour = "+str(hour)+";"
    count = session.execute(queryString )
    return count


def candidateCountRangeDay(candidate, monthStart,dayStart,hourStart,monthEnd,dayEnd,hourEnd,):
    countList = []
    if dayStart == dayEnd:

        queryString = ("select count from counts where candidate = '"
        +str(candidate)+"' and year = 2016 and month = "+str(monthStart)+
        " and day = "+str(dayStart)+";")
        print queryString
        count = session.execute(queryString)
        for row in count:
            #countSum+= row.count;
            countList.append(row.count);
    else:
        print str(dayStart) + " to " +str(dayEnd)

        queryString = ("select count from counts where candidate = '"
        +str(candidate)+"' and year = 2016 and month = "+str(monthStart)+
        " and day >= "+str(dayStart)+" and day <= "+str(dayEnd)+";")
        print queryString
        count = session.execute(queryString)
        for row in count:
            #countSum+= row.count;
            countList.append(row.count);
    return countList;


#def candidateCountRange(candidate, monthStart,dayStart,hourStart,monthEnd,dayEnd,hourEnd,):
    #countDictionary =
    #if dayStart == dayEnd:
        #queryString = ("select count from counts where candidate = '"
        #+str(candidate)+"' and year = 2016 and month = "+str(monthStart)+
        #" and day = "+str(dayStart)+" and hour >= "+str(hourStart)+" and hour <= "+str(hourEnd)+";")
        #count = session.execute(queryString)
    #else:
        #countSum = 0
        #queryString = ("select count from counts where candidate = '"
        #+str(candidate)+"' and year = 2016 and month = "+str(monthStart)+
        #" and day = "+str(dayStart)+" and hour >= "+str(hourStart)+" and hour <= 24;")
        #count = session.execute(queryString)
       ## countSum += count
        #print "AHHHHHH"
        #for row in count:
            #countSum+= row.count;
        #if dayEnd - 2 > dayStart:
            #print str(dayEnd-1) + " to " +str(dayEnd)
			#queryString = ("select count from counts where candidate = '"
            #+str(candidate)+"' and year = 2016 and month = "+str(monthStart)+
            #" and day >= "+str(dayStart+1)+" and day <= "+str(dayEnd)+";")
            #count = session.execute(queryString)
            #for row in count:
                #countSum+= row.count;

        #queryString = ("select count from counts where candidate = '"
        #+str(candidate)+"' and year = 2016 and month = "+str(monthStart)+
        #" and day = "+str(dayEnd)+" and hour <= "+str(hourEnd)+";")
        #count = session.execute(queryString)
        #for row in count:
            #countSum+= row.count;


#def candidateCountRangeD(candidate, monthStart,dayStart,hourStart,monthEnd,dayEnd,hourEnd,):
    #countDictionary = {}
    #if dayStart == dayEnd:
        #queryString = ("select count from counts where candidate = '"
        #+str(candidate)+"' and year = 2016 and month = "+str(monthStart)+
        #" and day = "+str(dayStart)+" and hour >= "+str(hourStart)+" and hour <= "+str(hourEnd)+";")
        #count = session.execute(queryString)
    #else:
        #countSum = 0
        #queryString = ("select count from counts where candidate = '"
        #+str(candidate)+"' and year = 2016 and month = "+str(monthStart)+
        #" and day = "+str(dayStart)+" and hour >= "+str(hourStart)+" and hour <= 24;")
        #count = session.execute(queryString)
       ## countSum += count
        #print "AHHHHHH"
        #for row in count:
            #countSum+= row.count;
        #if dayEnd - 2 > dayStart:
            #print str(dayEnd-1) + " to " +str(dayEnd)
			#queryString = ("select count from counts where candidate = '"
            #+str(candidate)+"' and year = 2016 and month = "+str(monthStart)+
            #" and day >= "+str(dayStart+1)+" and day <= "+str(dayEnd)+";")
            #count = session.execute(queryString)
            #for row in count:
                #countSum+= row.count;

        #queryString = ("select count from counts where candidate = '"
        #+str(candidate)+"' and year = 2016 and month = "+str(monthStart)+
        #" and day = "+str(dayEnd)+" and hour <= "+str(hourEnd)+";")
        #count = session.execute(queryString)
        #for row in count:
            #countSum+= row.count;

    #print queryString
    #return countSum

#for row in candidateCount("sanders",3,6,4):
    #print row.count;    

totalCount = 0
#for row in candidateCountRange("sanders",3,6,4,3,8,8):
    #totalCount += row.count
    #print row.count;
#print candidateCountRange("sanders",3,6,4,3,8,8)
print "The total count is " + str(totalCount)

print candidateCountRangeDay("sanders",3,7,4,3,8,8)
print len(candidateCountRangeDay("sanders",3,7,4,3,8,8))
