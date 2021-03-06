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





def candidateCount(candidate, month,day,hour):
    queryString = "select count from counts where candidate = '"+str(candidate)+"' and year = 2016 and month = "+str(3)+" and day = "+str(day)+" and hour = "+str(hour)+";"
    count = session.execute(queryString )
    print queryString
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
 
def candidateCountRangeHourlyDict(candidate, start,end):
    countList = []
    countDict = {}
    
    yearStart =  "2"+"0"+start[2]+start[3]
    #print year
    monthStart = start[4]+start[5]
    #print month
    dayStart = start[6]+start[7]
    #print day
    hourStart = start[8]+start[9]
    #print hour
    
    yearEnd =  "2"+"0"+end[2]+end[3]
    #print year
    monthEnd = end[4]+end[5]
    #print month
    dayEnd = end[6]+end[7]
    #print day
    hourEnd = end[8]+end[9]
    #print hour
    
    #for i in range(int(hourStart),24):
    #    if(i<10):
    #        countDict[yearStart+monthStart+dayStart+"0"+str(i)] = 0 
    #    else:
    #        countDict[yearStart+monthStart+dayStart+str(i)] = 0 
    
    if dayStart == dayEnd:
        
        queryString = ("select hour, count from counts where candidate = '"
        +str(candidate)+"' and year = 2016 and month = "+str(monthStart)+
        " and day = "+str(dayStart)+";")
        print queryString
        count = session.execute(queryString)
        hour = 0;
        for row in count:
            #countSum+= row.count;
            countList.append(row.count);
            if(row.hour<10):
                countDict[yearStart+monthStart+dayStart+"0"+str(row.hour)]=row.count
            else:
                countDict[yearStart+monthStart+dayStart+str(row.hour)] = row.count
    else:
        print str(dayStart) + " to " +str(dayEnd)
        
        queryString = ("select day, hour, count from counts where candidate = '"
        +str(candidate)+"' and year = 2016 and month = "+str(monthStart)+
        " and day >= "+str(dayStart)+" and day <= "+str(dayEnd)+";")
        print queryString
        count = session.execute(queryString)
        for row in count:
            #countSum+= row.count;
            countList.append(row.count);
            strHour = str(row.hour)
            strDay = str(row.day)
            if(row.hour<10):
                strHour = "0"+str(row.hour)
            if(row.day<10):
                strDay = "0"+str(row.day)
            
            countDict[yearStart+monthStart+strDay+strHour]=row.count
    return countDict;



#def candidateCountRangeDayDict(candidate, start,end):
    #countList = []
    #countDict = {}
    
    #yearStart =  "2"+"0"+start[2]+start[3]
    ##print year
    #monthStart = start[4]+start[5]
    ##print month
    #dayStart = start[6]+start[7]
    ##print day
    #hourStart = start[8]+start[9]
    ##print hour
    
    #yearEnd =  "2"+"0"+end[2]+end[3]
    ##print year
    #monthEnd = end[4]+end[5]
    ##print month
    #dayEnd = end[6]+end[7]
    ##print day
    #hourEnd = end[8]+end[9]
    ##print hour
    
    ##for i in range(int(hourStart),24):
    ##    if(i<10):
    ##        countDict[yearStart+monthStart+dayStart+"0"+str(i)] = 0 
    ##    else:
    ##        countDict[yearStart+monthStart+dayStart+str(i)] = 0 
    
    #if dayStart == dayEnd:
        
        #queryString = ("select hour, count from counts where candidate = '"
        #+str(candidate)+"' and year = 2016 and month = "+str(monthStart)+
        #" and day = "+str(dayStart)+";")
        #print queryString
        #count = session.execute(queryString)
        #hour = 0;
        #for row in count:
            ##countSum+= row.count;
            #countList.append(row.count);
            #if(row.hour<10):
                #countDict[yearStart+monthStart+dayStart+"0"+str(row.hour)]=row.count
            #else:
                #countDict[yearStart+monthStart+dayStart+str(row.hour)] = row.count
    #else:
        #print str(dayStart) + " to " +str(dayEnd)
        
        #queryString = ("select day, hour, count from counts where candidate = '"
        #+str(candidate)+"' and year = 2016 and month = "+str(monthStart)+
        #" and day >= "+str(dayStart)+" and day <= "+str(dayEnd)+";")
        #print queryString
        #count = session.execute(queryString)
        ##Complete this later.
        #for row in count:
            ##countSum+= row.count;
            #countList.append(row.count);
            #strHour = str(row.hour)
            #strDay = str(row.day)
            #if(row.hour<10):
                #strHour = "0"+=str(row.hour)
            #if(row.day<10):
                #strDay = "0"+str(row.day)
            
            #countDict[yearStart+monthStart+strDay]+=row.count
    #return countDict;
  

  
def candidateCountRangeDayFull(candidate, monthStart,dayStart,hourStart,monthEnd,dayEnd,hourEnd,):
    countList = []
    if dayStart == dayEnd:
        
        queryString = ("select count from counts where candidate = '"
        +str(candidate)+"' and year = 2016 and month = "+str(monthStart)+
        " and day = "+str(dayStart)+";")
        print queryString
        count = session.execute(queryString)
        daySum = 0
        for row in count:
            if(row.count != None):
                daySum += row.count;
                countList.append(daySum);
            #countSum+= row.count;
        
    else:
        
        #need to have a case for counting days up individually 
        print str(dayStart) + " to " +str(dayEnd)
        for day in range(dayStart,dayEnd+1):
            queryString = ("select count from counts where candidate = '"
            +str(candidate)+"' and year = 2016 and month = "+str(monthStart)+
            " and day = "+str(day)+";")
            print queryString
            count = session.execute(queryString)
            dayCounter =0
            daySum = 0
            for row in count:
                if(row.count != None):
                    daySum += row.count;
                    countList.append(daySum);
                #countSum+= row.count;
            print daySum
            print dayCounter
            
            countList.append(daySum);
            
    countListFullDay = []
    i = 0
    return countList;

def candidateCountRangeDayFull(candidate, monthStart,dayStart,hourStart,monthEnd,dayEnd,hourEnd,):
    countList = []
    if dayStart == dayEnd:
        
        queryString = ("select count from counts where candidate = '"
        +str(candidate)+"' and year = 2016 and month = "+str(monthStart)+
        " and day = "+str(dayStart)+";")
        print queryString
        count = session.execute(queryString)
        daySum = 0
        for row in count:
            if(row.count != None):
                daySum += row.count;
                countList.append(daySum);
            #countSum+= row.count;
        
    else:
        #need to have a case for counting days up individually
        print str(dayStart) + " to " +str(dayEnd)
        for day in range(dayStart,dayEnd+1):
            print 'Day: '+ str(day)
            for hour in range(hourStart, hourEnd+1):
                queryString = ("select count from counts where candidate = '"+str(candidate)+"' and year = 2016 and month = "+str(monthStart)+" and day = "+str(day)+" and hour = "+str(hour))
                print 'Hour: ' + str(hour)
                #in case the first day fails the try/except, define row ahead of time
                row = None
                try:
                    row = session.execute(queryString)[0]
                except:
                    countList.append(None)
                    continue
                if(row != None and row.count != None and row.count != 0):
                    countList.append(row.count);
                else:
                    countList.append(None)
            
    return countList;


def candidateCountHourly(candidate, month, start_day, end_day):
    print str(start_day)  + " to " +str(end_day)
    count_list = []
    for day in range(start_day,end_day+1):
        daySum = 0
        for hour in range(1, 24):
            queryString = ("select count from counts where candidate = '" +str(candidate)+"' and year = 2016 and month = "+str(month)+" and day = "+str(day)+" and hour = "+str(hour))
            print queryString
            row = session.execute(queryString)[0]
            if row.count != None:
                daySum += row.count;
                
        count_list.append(daySum);
        print daySum
        
    i = 0
    return count_list;

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
    
    
# format YYYYMMDDHH
totalCount = 0
#printStatement = candidateCountRangeDay("sanders",3,5,4,3,8,4)
#print printStatement
#print len(printStatement)


#Testing the dictionary
#print candidateCountRangeHourlyDict("sanders","2016030500","2016030600")
#print len(candidateCountRangeHourlyDict("sanders","2016030500","2016030800"))
tweets = candidateCountRangeDayFull('sanders', 03 , 01 , 00, 03 , 30, 23)
#tweets = candidateCountDaily('sanders', 03, 01, 10)
print tweets
#candidateCountRangeDayFull(candidate, monthStart,dayStart,hourStart,monthEnd,dayEnd,hourEnd,)
print len(tweets)
