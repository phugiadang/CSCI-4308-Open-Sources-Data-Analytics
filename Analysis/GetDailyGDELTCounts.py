from cassandra.cluster import Cluster
import sys

cluster = Cluster(contact_points=['128.138.202.110','128.138.202.117'])
session = cluster.connect('candidates')

def incrementDate(date):
    final_date = None
    date_str = str(date)

    def inc31Days():
        if date_str[6] + date_str[7] == '31':     
            final = date + 70
        else: final = date + 1
        return final

    def inc30Days():
        if date_str[6] + date_str[7] == '30':
            final = date + 71
        else: final = date + 1
        return final

    def incFeb():
        if int(date_str[2] + date_str[3])%4 == 0:
            return inc30Days()
        else:
            if date_str[6] + date_str[7] == '29':
                final = date + 72
            else: final = date + 1
        return final

    def incDec():
        if date_str[6] + date_str[7] == '31':
            final = date + 8870
        else: final = date + 1
        return final

    if date_str[4] + date_str[5] in ['01', '03', '05', '07', '08', '10']:
        final_date = inc31Days()
    elif date_str[4] + date_str[5] in ['04', '06', '09', '11']:
        final_date = inc30Days()
    elif date_str[4] + date_str[5] == '02':
        final_date = incFeb()
    elif date_str[4] + date_str[5] == '12':
        final_date = incDec()
    return final_date

def getGDELTCounts(candidate, start, end):
    countList = []
    #create list of every date to query the database for
    dates = []
    date = int(start)
    while date <= int(end):
        dates.append(str(date))
        date = incrementDate(date)

    #query the counts for each day
    for date in dates:

        queryString = ("select count from " + (candidate + 'gdelt') +  " where date = " + date)
        #in case the first day fails the try/except, define row ahead of time
        row = None
        try:
            row = session.execute(queryString)[0]
        except:
            countList.append(None)
            continue
        if(row != None and row.count != None):
            countList.append(row.count);
        else:
            countList.append(None)
            
    return countList, dates;


#def main():
#    if len(sys.argv) != 4:
#        print 'Usage: GetDailyGDELTCounts.py <candidate, lower case> <start date> <end date>'
#        print 'where date format is YYYYMMDD'
#    else:
#        print getGDELTCounts(sys.argv[1], sys.argv[2], sys.argv[3])
#main()
