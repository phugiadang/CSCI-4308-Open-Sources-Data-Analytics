#!/bin/bash

#set this to machine number
m=1
nm=1
list_of_users="captainrex1995@gmail.com,brco0199@colorado.edu,dano8957@colorado.edu,dano8957@gmail.com,dabi9710@colorado.edu,erli3237@colorado.edu,phda1798@colorado.edu"
good=0

a=$(ping -w 5 128.138.202.117 | grep "bytes from" | wc | cut -d ' ' -f 7)

if [ $a -eq 0 ]
   then
	echo "Machine 2 is down! Fix it fast!" | mail -s "Machine 2 is down, fix it fast!" ${list_of_users}
#captainrex1995@gmail.com
    	good=$(($good-1))

fi


#html=$(wget localhost:8080 -q -O -)
#b=$(echo $html | grep "Status:</strong> ALIVE" | wc | cut -d ' ' -f 7)
#if [ $b -ne $nm ]
#   then
#	echo $b
#	echo $nm
#	echo "Not all Spark workers are alive, better check it out!" | mail -s "Missing Spark Worker(s)!" ${listOfUsers}
#	good=$(($good-1))
#fi

#check on tweet streaming
c=$(ps aux | grep 'python threadCass.py' | wc | cut -d ' ' -f 7)
if [ $c -eq 1 ]
then
	echo "bad!!!"
	echo "Tweet streaming is stopped, better restart it!" | mail -s "Tweet Streaming Stopped!" ${list_of_users}
	good=$(($good-1))
fi

#Make sure cassandra status is "Up Normal"
statusss=$(nodetool status | grep "UN " | wc | cut -d ' ' -f 7)
if [ $statusss -ne 2 ]
then
	echo "Cassandra is down, better fix it!" | mail -s "Cassandra is down!" ${list_of_users}
	good=$(($good-1))
fi

#If all tests pass!
if [ $good -eq 0 ]
   then
	#echo "Please reply to senior project group text if you get this" | mail 7206297749@vtext.com
	echo "All OpenStack operations are normal, everything looks good!" | mail -s "OpenStack Machine 1 Status: OK!" ${list_of_users}
fi

