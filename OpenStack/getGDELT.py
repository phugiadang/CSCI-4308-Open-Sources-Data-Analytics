import sys
from subprocess import call

a = call("sudo sh -c \"date | cut -d ' ' -f 2-4 > date.txt\"", shell=True)


date_dictionary = {"Jan" : "01", "Feb" : "02", "Mar" : "03", "Apr" : "04", "May" : "05", "Jun" : "06", "Jul" : "07", "Aug" : "08", "Sep" : "09", "Oct" : "10", "Nov" : "11", "Dec" : "12"}

with open("date.txt", "r+") as date_file:
    for line in date_file:
        

