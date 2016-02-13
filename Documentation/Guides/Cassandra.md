#Setting up a Cassandra Cluster across multiple machines
---
---
#Step 1. Create a Datastax Enterprise Account
#Step 2. Run the command:
```
curl --user <your_datastax_email_here>:<your_datastax_password_here> -L http://downloads.datastax.com/enterprise/dse.tar.gz | tar xz
```
#Step 3. Repeat Step 2 on every machine you want to include in your cluster
#Step 4. Edit the Cassandra.yaml file on each cluster, which is located at:
```
dse-x.x.x/resources/cassandra/conf/cassandra.yaml
```
#Here are the things that you want to edit in cassandra.yaml:
##1. cluster_name
##2. initial_token
###There is a python file that generates tokens for each machine, based off of the number of machines that are in your cluster. Use google to find the specific algorithim. You will have one machine set its initial_token to 0.
##3. Under the section seed_provider, in the section marked seeds, add the ip address of each machine you have in your cluster. An example of this would be:
```
- seeds: "128.138.202.110, 128.138.202.117"
```
###Make sure that the ip of the machine you are on comes first in this list.
##4. listen_address
###Simply set this to the machine's ip. Example:
```
listen_address: 128.138.202.117
```
##5. endpoint_snitch
###The snitch Cassandra where to store replicas. There are several snitches, so it is best to know exactly how you want your cluster to be setup, so you can choose the snitch that best suites your needs.
