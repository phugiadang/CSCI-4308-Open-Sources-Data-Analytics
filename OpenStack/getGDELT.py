import sys
from subprocess import call

a = call("sudo sh -c \"date | cut -d ' ' -f 2-6 > date.txt\"", shell=True)


date_dictionary = {"Jan" : "01", "Feb" : "02", "Mar" : "03", "Apr" : "04", "May" : "05", "Jun" : "06", "Jul" : "07", "Aug" : "08", "Sep" : "09", "Oct" : "10", "Nov" : "11", "Dec" : "12"}

#Feb 14 15:09:30

full_date = ''

def updateData(current_word, current_word_number):
    global full_date
    full_date += current_word
    return '', current_word_number+1


with open("date.txt", "r+") as date_file:
    for line in date_file:
        current_word = ''
        current_word_number = 0
        for character in line:
            if (character != ' '):
                current_word += character

            else:
                if (current_word_number == 0):
                    current_word = date_dictionary[current_word]

	        res = updateData(current_word, current_word_number)
                current_word = res[0]
                current_word_number = res[1]

  	full_date = current_word+full_date
        

full_date = full_date.replace("MST", "").replace(":", "").replace("\n","")
print full_date
