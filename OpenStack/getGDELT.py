import sys
from subprocess import call

a = call("sudo sh -c \"date | cut -d ' ' -f 1-5\"", shell=True)
#a = a.replace("\n","")
#print a
