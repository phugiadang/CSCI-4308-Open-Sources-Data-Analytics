
#Make sure cassandra status is "Up Normal (UN)" on machine 1
statusss=$(nodetool status | grep -c "Datacenter: Analytics")
if [ $statusss -eq 0 ]
then
        echo "Cassandra is down on Machine 1, better fix it!" | mail -s "Cassandra is down, restarting!" captainrex1995@gmail.com
        sudo rm /home/centos/dse-4.8.1/bin/java_*
        sudo ./home/centos/dse-4.8.1/bin/dse cassandra 
fi

echo $statusss


