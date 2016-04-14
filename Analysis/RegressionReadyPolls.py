import operator
import sys
from AnalysisObjectFactory import AnalysisObjectFactory
#sys.path.insert(0, '../Polls')
from GetPollsFromDatabase import DatabasePolls


class RegressionReadyPolls:
    def __init__(self, polls, candidate, start, end):
        self.polls = polls
        self.candidate = candidate
        self.start = start
        self.end = end
        self.final_poll_numbers = []

    def getBestPollLength(self):
        #search for each poll with the candidate named. Record the number of choices
        #in that poll. Whatever the most common number of responses is is what we'll use
        choice_length = {'2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, '11': 0, '12': 0}
        for poll in self.polls:
            if self.candidate in poll[1]:
                if len(poll[1]) == 2:
                    choice_length['2'] += 1
                if len(poll[1]) == 3:
                    choice_length['3'] += 1
                if len(poll[1]) == 4:
                    choice_length['4'] += 1
                if len(poll[1]) == 5:
                    choice_length['5'] += 1
                if len(poll[1]) == 6:
                    choice_length['6'] += 1
                if len(poll[1]) == 7:
                    choice_length['7'] += 1
                if len(poll[1]) == 8:
                    choice_length['8'] += 1
                if len(poll[1]) == 9:
                    choice_length['9'] += 1
                if len(poll[1]) == 10:
                    choice_length['10'] += 1
                if len(poll[1]) == 11:
                    choice_length['11'] += 1
                if len(poll[1]) == 12:
                    choice_length['12'] += 1
    
        best_choice_length = max(choice_length.iteritems(), key=operator.itemgetter(1))[0]
        return best_choice_length

    def fillGapsWithAvg(self):
        interpolated_numbers = 0

        #since leading values can be None, iterate until we find the first number
        first_num = None
        for i in range (0, len(self.final_poll_numbers)):
            if self.final_poll_numbers[i] != None:
                first_num = self.final_poll_numbers[i]
                break
        #replace leading None's with this number
        for i in range (0, len(self.final_poll_numbers)):
            if self.final_poll_numbers[i] == None:
                self.final_poll_numbers[i] = first_num
                interpolated_numbers += 1
            else:
                break
        #Now deal with trailing None's. Give them the value of the last number in the list
        #check if the last value is None
        if self.final_poll_numbers[len(self.final_poll_numbers)-1] == None:
            last_num = None
            i = len(self.final_poll_numbers)-1
            while i >= 0 and last_num == None:
                if self.final_poll_numbers[i] != None:
                    last_num = self.final_poll_numbers[i]
                i = i - 1
            while i < len(self.final_poll_numbers):
                self.final_poll_numbers[i] = last_num
                interpolated_numbers += 1
                i += 1

        #now, replace None's in the middle of the list with the average of the numbers around them
        #General idea here: i iterates to the first num, i+j to the second, k passes over the None's
        #to replace them with the average
        first_num = None
        second_num = None
        first_found = False
        avg = None
        i = 0
        while i < len(self.final_poll_numbers)-1:
            if first_found == False and self.final_poll_numbers[i] == None:
                first_num = self.final_poll_numbers[i-1]
                first_found = True
                j = 0
                for j in range(0, len(self.final_poll_numbers)):
                    if self.final_poll_numbers[i+j] != None:
                        second_num = self.final_poll_numbers[i+j]
                        avg = (first_num + second_num) / 2
                        break
                k = i
                while k < i+j:
                    self.final_poll_numbers[k] = avg
                    interpolated_numbers += 1
                    k += 1
                    first_found = False
                i += j
            else:
                i += 1
        

    def incrementDate(self, date):
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
     
    def makeSimplePollNumbers(self):

        best_choice_length = self.getBestPollLength()
        #Only use polls with the best number of choices to make interpolation easier
        relevant_polls = []
	for poll in self.polls:
            if len(poll[1]) == int(best_choice_length):
                relevant_polls.append(poll)
                #we now have the polls of the correct length containing the correct candidate. Now pull out the poll numbers for the relevant candidate
	current_date = relevant_polls[0][0]
        to_be_averaged = []

        #if there are no polls on the first n days of the range, add n None's to poll_numbers
        #print int(self.start)
        if int(self.start) != current_date:
            for i in range (int(self.start), current_date):
                self.final_poll_numbers.append(None)

        for poll in relevant_polls:
            candidate_found = False
            i = 0
            #iterate through the list of candidates in the poll until we find the right one.
            #Then grab the corresponding poll value
            while i < int(best_choice_length)-1 and candidate_found == False:
                #this if statement will be true exactly once per poll, when the correct candidate is found
                if poll[1][i] == self.candidate:
                    candidate_found = True
                    if poll[0] == current_date:
                        #there's more than one poll a day, so we average each day's polls
                        to_be_averaged.append(poll[2][i])
                    else:
                        #if we're on to a poll on a new day, get the averages for the previous day
                        if (current_date != poll[0]):
                            #we found a poll on a new day, so average the old day and add it to poll_numbers
                            avg = 0
                            for num in to_be_averaged: avg += num
                            avg = avg/len(to_be_averaged)
                            self.final_poll_numbers.append(avg)
                            to_be_averaged = [poll[2][i]]
                        #we want to add 'None' into the days that have no poll numbers so we can later add averages there
                        if poll[0] != self.incrementDate(current_date):
                            for i in range (current_date, poll[0]-1):
                                self.final_poll_numbers.append(None)
                        current_date = poll[0]
                i += 1
    
        if len(to_be_averaged) != 0:
            avg = 0
            for num in to_be_averaged: avg += num
            avg = avg/len(to_be_averaged)
            self.final_poll_numbers.append(avg)
            to_be_averaged = []

        #Now, if there was no poll on the last day of the range then this will not insert enough None's.
        #e.g. in the range 20160301 20160305, the last poll was on the 3rd so the list will only be 3 long
        #We not have to add in the approproate number of trailing None's
    
        time_range = int(self.end) - int(self.start)
        if len(self.final_poll_numbers) <= time_range:
            for i in range(0, int(self.end) - current_date):
                self.final_poll_numbers.append(None)


    def getPollNumbers(self):
        return self.final_poll_numbers


