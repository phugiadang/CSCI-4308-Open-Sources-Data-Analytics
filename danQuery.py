from sys import argv
from cassandra.cluster import Cluster
from subprocess import call
import operator
import calculateDate

addMinute = calculateDate.changeMinute
keyspace = 'candidates'
cluster = Cluster(
        contact_points=['128.138.202.110','128.138.202.117'],)
#connect to our Cassandra Keyspace
session = cluster.connect(keyspace)
session.default_timeout = 60

candidate = argv[1]
start_date = argv[2]
end_date = argv[3]
quantity = ''
sort_type = 0

if (len(argv) >= 5):
    quantity = argv[4]
if (len(argv) == 6):
    sort_type = argv[5]

if (sort_type == 'count'):
    sort_type = 1

else:
    sort_type = 0

list_of_candidates = ["trump", "sanders", "rubio", "clinton", "carson", "cruz", "kasich", "bush"]


#Check to see if the user wants count on an hour by hour basis
if (quantity == 'hourly'):
    new_start_date = start_date
    new_end_date = str(int(new_start_date) + 10000)

     
    if (candidate == 'all'):
        #The user wants counts from all candidates on an hour by hour basis
        list_of_counts = {}
        for name in list_of_candidates:
            list_of_dates = {}
	    while(int(new_start_date) != int(end_date)):
                result = session.execute('select count(*) from ' + name + ' where created_at >= ' + new_start_date + ' and created_at < ' + new_end_date + ' ALLOW FILTERING;')
                
                list_of_dates['from ' + new_start_date + ' to ' + new_end_date] = result[0][0]
                new_start_date = new_end_date
                new_end_date = str(int(new_start_date) + 10000)
                if ((new_end_date[8] == '2') and (new_end_date[9] == '4')):
                    new_end_date = str(int(new_end_date) + 760000)
    
            list_of_counts[name] = list_of_dates
            new_start_date = start_date
            new_end_date = str(int(start_date) + 10000)

        
        #junk = sorted(list_of_counts["bush"].items(), key=operator.itemgetter(0))
        #print junk

        
        
        for i in range (0, len(list_of_candidates)):
            junk = sorted(list_of_counts[list_of_candidates[i]].items(), key=operator.itemgetter(sort_type))

            print list_of_candidates[i] + ": " + str(junk) + "\n\n"
            
    else:
        #The user wants counts from a specific candidate on an hour by hour basis
        list_of_dates = {}
        new_start_date = start_date
        new_end_date = str(int(new_start_date) + 10000)

        while(int(new_start_date) != int(end_date)):
                result = session.execute('select count(*) from ' + candidate + ' where created_at >= ' + new_start_date + ' and created_at < ' + new_end_date + ' ALLOW FILTERING;')

                list_of_dates['from ' + new_start_date + ' to ' + new_end_date] = result[0][0]
                new_start_date = new_end_date
                new_end_date = str(int(new_start_date) + 10000)
                if ((new_end_date[8] == '2') and (new_end_date[9] == '4')):
                    new_end_date = str(int(new_end_date) + 760000)



  
        #final_step = session.execute('select count(*) from ' + candidate + ' where created_at >= ' + start_date + ' and created_at <= ' + end_date + ' ALLOW FILTERING;')

        #print candidate + str(sorted(list_of_dates.items(), key=operator.itemgetter(sort_type)))
        #print result_string[0]
        done_sorted = sorted(list_of_dates.items(), key=operator.itemgetter(sort_type))
        
       
        print "\"dataset\": [\n{\n\"seriesname: \"" + candidate + "\",\n\"data\": [\n"

        count111 = 0
        for x in done_sorted:
            #junk1 = str(x).replace("\n", "")
            #junk2 = str(x)[0]
            count111 += 1
            if (count111 != len(done_sorted)):
                print "{ \"" + str(x[0]) + "\": \"" + str(x[1]) + "\" },\n"
            else:
                print "{ \"" + str(x[0]) + "\": \"" + str(x[1]) + "\" }\n" 
        

        print "]\n"
        print "},\n"
        print "]"



else:
    if (candidate == 'all'):
        #The user wants the single tweet count of every candidate
        list_of_counts = []
        for name in list_of_candidates:
            result = session.execute('select count(*) from ' + name + ' where created_at >= ' + start_date + ' and created_at <= ' + end_date + ' ALLOW FILTERING;')
            list_of_counts.append(result[0][0])
  
        for i in range (0, len(list_of_candidates)):
            print list_of_candidates[i] + ": " + str(list_of_counts[i])
    
    else:
        #The user wants the single tweet count of a single candidate
        final_step = session.execute('select count(*) from ' + candidate + ' where created_at >= ' + start_date + ' and created_at <= ' + end_date + ' ALLOW FILTERING;')

        result_string = final_step[0]

        print result_string[0]
