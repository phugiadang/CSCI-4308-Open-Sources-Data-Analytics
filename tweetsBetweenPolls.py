#if there's a new poll in the database, grab the counts of tweets about each candidate 
#that were posted since the last poll
#Specifically, checks if there is a poll in the DB with an ID that is one larger than the one
#recorded in lastPoll.txt and then uses query.py to get the tweets between the polls

from cassandra.cluster import Cluster
import os

cluster = Cluster(['128.138.202.110', '128.138.202.117'])
session = cluster.connect('polls')

def tweetsSinceLastPoll():
    if newPoll():
        #get the end date of the last poll and the new poll
        f = open(os.path.join(os.path.expanduser('~'), 'CSCI-4308-Open-Sources-Data-Analytics/lastPoll.txt'), 'r+')
#        f = open('lastPoll.txt', 'r+')
        poll_ID = int(f.readline())
        f.close()
        poll_1 = session.execute('SELECT end_date FROM president WHERE id = ' + str(poll_ID-1) + ' ALLOW FILTERING')[0]
        poll_2 = session.execute('SELECT end_date FROM president WHERE id = ' + str(poll_ID) + ' ALLOW FILTERING')[0]
        #if the two newest polls are on the same day, use an older poll for poll_1
        i = 1
        while (poll_1.end_date == poll_2.end_date):
            i = i+1
            poll_1 = session.execute('SELECT end_date FROM president WHERE id = ' + str(poll_ID-i) + ' ALLOW FILTERING')[0]
        #the dates need to be appended with 000000 to match the way twitter dates are stored
        poll_1_end = poll_1.end_date*1000000
        poll_2_end = poll_2.end_date*1000000
        print(poll_1_end)
        print(poll_2_end)
        #get counts of tweets between these dates (beginning of first day, end of second)
        filePath = os.path.join(os.path.expanduser('~'), 'CSCI-4308-Open-Sources-Data-Analytics/query.py')
        command = 'sudo python ' + filePath + ' all ' + str(poll_1_end) + ' ' + str(poll_2_end)
        os.system(command)
        
        #Now post the results from the new poll
    else:
        print 'No new poll since this program was last run'
        

#returns true if a new poll has been added to the database since last time this was run
def newPoll():
    #the ID of the last poll will be writted to lastPoll.txt. Check if another one has been added
    f = open(os.path.join(os.path.expanduser('~'), 'CSCI-4308-Open-Sources-Data-Analytics/lastPoll.txt'), 'r+')
    #f = open('lastPoll.txt', 'r+')
    last_poll_ID = int(f.readline())
    #check for another poll by checking for the next ID
    row = session.execute('SELECT id FROM president WHERE id = ' + str(last_poll_ID+1) + ' ALLOW FILTERING')
    try:
        if row[0][0] == (last_poll_ID+1):
            f.seek(0)
            f.write(str(row[0][0]))
            f.close
            return True
    except:
        return False
        
def main():
    tweetsSinceLastPoll()

if __name__ == "__main__":
    main()
