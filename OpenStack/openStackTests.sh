#!/bin/bash

#set this to machine number
m=1
nm=1
listOfUsers="captainrex1995@gmail.com,brco0199@colorado.edu,dano8957@colorado.edu,dano8957@gmail.com,dabi9710@colorado.edu,erli3237@colorado.edu,phda1798@colorado.edu"
good=0

a=$(ping -w 5 google.com | grep "bytes from" | wc | cut -d ' ' -f 7)

if [ $a -eq 0 ]
   then
	echo "YAY"
	echo "Machine ${m} has no internet, better restart!" | mail -s "Machine ${m} has no internet!" ${listOfUsers}
#captainrex1995@gmail.com
    	good=good-1

fi


html=$(wget localhost:8080 -q -O -)
b=$(echo $html | grep "Status:</strong> ALIVE" | wc | cut -d ' ' -f 7)
if [ $b -ne $nm ]
   then
	echo $b
	echo $nm
	echo "Not all Spark workers are alive, better check it out!" | mail -s "Missing Spark Worker(s)!" ${listOfUsers}
	good=good-1
fi

#check on tweet streaming
c=$(ps aux | grep trump.py | wc | cut -d ' ' -f 7)
if [ $c -eq 1 ]
then
	echo "bad!!!"
	echo "Tweet streaming is stopped, better restart it!" | mail -s "Tweet Streaming Stopped!" ${listOfUsers}
	good=good-1
fi

#If all tests pass!
if [ $good -eq 0 ]
   then
	echo "All OpenStack operations are normal, everything looks good!" | mail -s "OpenStack Machine 1 Status: OK!" ${listOfUsers}
fi

