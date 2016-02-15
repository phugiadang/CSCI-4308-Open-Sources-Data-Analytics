from sys import argv
from cassandra.cluster import Cluster
from subprocess import call
import operator

keyspace = 'candidates'
cluster = Cluster(
        contact_points=['128.138.202.110','128.138.202.117'],)
#connect to our Cassandra Keyspace
session = cluster.connect(keyspace)

candidate = argv[1]
start_date = argv[2]
end_date = argv[3]
quantity = ''

if (len(argv) == 5):
    quantity = argv[4]

list_of_candidates = ["trump", "sanders", "rubio", "clinton", "carson", "cruz", "kasich", "bush"]

if (quantity == 'hourly'):
    new_start_date = start_date
    new_end_date = str(int(new_start_date) + 10000)
    if (candidate == 'all'):
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
            junk = sorted(list_of_counts[list_of_candidates[i]].items(), key=operator.itemgetter(0))

            print list_of_candidates[i] + ": " + str(junk) + "\n\n"

    else:
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

        print candidate + str(sorted(list_of_dates.items(), key=operator.itemgetter(0)))
        #print result_string[0]





else:
    if (candidate == 'all'):
        list_of_counts = []
        for name in list_of_candidates:
            result = session.execute('select count(*) from ' + name + ' where created_at >= ' + start_date + ' and created_at <= ' + end_date + ' ALLOW FILTERING;')
            list_of_counts.append(result[0][0])
  
        for i in range (0, len(list_of_candidates)):
            print list_of_candidates[i] + ": " + str(list_of_counts[i])
    
    else:
        final_step = session.execute('select count(*) from ' + candidate + ' where created_at >= ' + start_date + ' and created_at <= ' + end_date + ' ALLOW FILTERING;')

        result_string = final_step[0]

        print result_string[0]
