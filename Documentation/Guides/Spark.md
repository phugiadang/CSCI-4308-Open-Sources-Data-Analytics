#A Guide for Setting up a Spark Cluster on Multiple Machines
---
---
1. ```sudo yum install wget```


2.wget -O /home/centos/spark.tar‘http://d3kbcqa49mib13.cloudfront.net/spark-1.5.1-bin-hadoop2.6.tgz’ 


3.tar -zfx spark.tar


4.cd spark-1.5.1-bin-hadoop2.6/


5.yum search openjdk-devel


6.sudo yum install java-1.7.0-openjdk-devel.x86_64


7.sudo /usr/sbin/alternatives --config java


8.sudo /usr/sbin/alternatives --config javac


9.sudo vim /etc/profile


10.# add the following lines at the end


11.export JAVA_HOME=/usr/lib/jvm/java-1.7.0-openjdk-1.7.0.19.x86_64


12.OPTIONAL( export JAVA_HOME=/usr/lib/jvm/java-1.7.0-openjdk-1.7.0.85-2.6.1.2.el7_1.x86_64/jre  )


13.export JRE_HOME=$JAVA_HOME/jre


14.export PATH=$PATH:$JAVA_HOME/bin


15.export CLASSPATH=.:$JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar


16.# save and exit vim


17.$ source /etc/profile


18.$ java -version


19.wget -O /home/centos/scala.tgz "http://downloads.typesafe.com/scala/2.10.6/scala-2.10.6.tgz?_ga=1.170409123.2032133767.1444195421"


20.tar zfx scala.tgz


21.$ sudo mv scala-2.10.6 /usr/lib


22.$ sudo vim /etc/profile


23.# add the following lines at the end


24.export SCALA_HOME=/usr/lib/scala-2.10.6


25.export PATH=$PATH:$SCALA_HOME/bin


26.# save and exit vim


27.# make the bash profile take effect immediately


28.source /etc/profile


29.# test


30.$ scala -version


31.html=$(wget google.com -q -O -)


32.echo $html


33../sbin/start-slave.sh spark://open-source-data-analytics-1:7077

34../sbin/start-master.sh

