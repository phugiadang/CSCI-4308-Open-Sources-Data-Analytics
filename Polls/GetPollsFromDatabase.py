from cassandra.cluster import Cluster
import sys

cluster = Cluster(['128.138.202.110', '128.138.202.117'])
session = cluster.connect('polls')

cql = "SELECT * FROM polls.presidentbydate"
rows = session.execute(cql)

class DatabasePolls:
    def __init__(self, start, end, candidates):
        self.start = int(start)
        self.end = int(end)
        self.candidates = candidates
        self.raw_polls = None
        self.cleaned_polls = None

    def queryDatabase(self):
        #dates are going to be in the format YYYYMMDD
        polls = []
        #loop through all the dates in the range, query each
        for i in range(self.start, self.end+1):
            
            #make the dates wrap correctly
            if i%100 == 32:
                i += 68
            if i%10000 == 1300:
                i += 8700
            #polls.append(session.execute('SELECT * FROM polls.presidentbydate WHERE end_date=' + str(i)))
            polls_on_date = session.execute('SELECT * FROM polls.presidentbydate WHERE end_date=' + str(i))
            for poll in polls_on_date:
                new = {'pollster': poll.pollster, 'start_date': poll.start_date, 'end_date': poll.end_date, 'name': poll.name, 'observations': poll.observations, 'responses': eval(poll.responses)}
                polls.append(new)
        self.raw_polls = polls
        return
        
    def cleanPolls(self):
        relevant_responses = []
        #grab the polls with the relevant candidates
        for poll in self.raw_polls:
            #iterate through the candidates in the current poll
            return_poll = False
            for candidate in poll['responses']:
                #if this poll contains a candidate we care about...
                if candidate['choice'] in self.candidates:
                    #flag this poll as one to return
                    return_poll = True
                    break
            if return_poll == True:
                #break down the poll to eventually return
                new_entry = [poll['end_date'], [], []]
                for candidate in poll['responses']:
                    new_entry[1].append(candidate['choice'])
                    new_entry[2].append(candidate['value'])
                relevant_responses.append(new_entry)
        self.cleaned_polls = relevant_responses
      
    def getCleanedPolls(self):
        return self.cleaned_polls
    
    def printCleanedPolls(self):
        for poll in self.cleaned_polls:
            print poll
        print self.start
        print self.end

def main():
    
    if len(sys.argv) < 3:
        print '\nUsage: python GetPollsFromDatabase.py <start date> <end date> <candidates>'
        print 'where the dates are formatted as YYYYMMDD and the candidates are a list of'
        print 'any length of candidate names separated by spaces'
        print 'Example:'
        print 'python GetPollsFromDatabase.py 20160301 20160310 Trump Sanders\n'
        return
    
    candidates = []
    for i in range(3, len(sys.argv)):
        candidates.append(sys.argv[i])
    
    dp = DatabasePolls(sys.argv[1], sys.argv[2], candidates)
    dp.queryDatabase()
    dp.cleanPolls()
    dp.printCleanedPolls()

main()
#Structure of what this returns:

#[
#[20160101, [clinton, sanders, undecided], [30, 40, 30]], 
#[20160101, [trump, rubio, cruz], [40, 20, 40]], 
#[...]
#]
