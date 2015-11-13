#!/bin/bash

#set this to machine number
m=1

good=0

a=$(ping -w 5 google.com | grep "bytes from" | wc | cut -d ' ' -f 7)

if [ $a -eq 0 ]
   then
	echo "YAY"
	echo "Machine ${m} has no internet, better restart!" | mail -s "Machine ${m} has no internet!" captainrex1995@gmail.com
    	good=good-1

fi


