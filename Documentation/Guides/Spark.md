#A Guide for Setting up a Spark Cluster on Multiple Machines
---
---
##1. ```sudo yum install wget```


##2. ```wget -O /home/centos/spark.tar‘http://d3kbcqa49mib13.cloudfront.net/spark-1.5.1-bin-hadoop2.6.tgz’```


##3. ```tar -zfx spark.tar```


##4. ```cd spark-1.5.1-bin-hadoop2.6/```


##5. ```yum search openjdk-devel```


##6. ```sudo yum install java-1.7.0-openjdk-devel.x86_64```


##7. ```sudo /usr/sbin/alternatives --config java```


##8. ```sudo /usr/sbin/alternatives --config javac```


##9. ```sudo vim /etc/profile```


##10. Now, add the following lines at the end


###a) ```export JAVA_HOME=/usr/lib/jvm/java-1.7.0-openjdk-1.7.0.19.x86_64```


###b) ```OPTIONAL( export JAVA_HOME=/usr/lib/jvm/java-1.7.0-openjdk-1.7.0.85-2.6.1.2.el7_1.x86_64/jre  )```


###c) ```export JRE_HOME=$JAVA_HOME/jre```


###d) ```export PATH=$PATH:$JAVA_HOME/bin```


###e) ```export CLASSPATH=.:$JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar```


##11. Now, save and exit


##12. ```source /etc/profile```


##13. ```java -version```


##14. ```wget -O /home/centos/scala.tgz "http://downloads.typesafe.com/scala/2.10.6/scala-2.10.6.tgz?_ga=1.170409123.2032133767.1444195421"```


##15. ```tar zfx scala.tgz```


##16. ```sudo mv scala-2.10.6 /usr/lib```


##17. ```sudo vim /etc/profile```


##18. Now, add the following lines at the end


###a) ```export SCALA_HOME=/usr/lib/scala-2.10.6```


###b) ```export PATH=$PATH:$SCALA_HOME/bin```


##19. Now, Save and exit


##20. ```source /etc/profile```


