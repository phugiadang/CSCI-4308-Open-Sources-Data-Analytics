#How to change the date on a machine running centos, if you are an American
---
---
#1. Run the command ```cd /usr/share/zoneinfo/America```
#2. Run ```ls``` to see the timezones of all the major cities
#3. Once you find a city in your timezone, run this command (I am using Yelloknife as an example) ```sudo cp Yellowknife /etc/localtime```
#4. Now run ```date``` and your machine's time should now be in the correct time zone
