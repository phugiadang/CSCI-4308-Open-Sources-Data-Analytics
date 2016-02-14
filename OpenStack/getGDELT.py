import sys
from subprocess import call

a = call("sudo sh -c \"date | cut -d ' ' -f 2-4\"", shell=True)
#a = a.replace("\n","")
#print a
