#A compilation of the known bugs throughout the project
---
---
##HuffPost Polster API
---
##Tweet Streaming
###Bug: If we re-run a tweet stream too many times, we get a 420 error, which is a denial of service by Twitter due to too many requests.
###Solution: What was killing us was that we were running six different threads, each with its own tweet Stream, and all using the same Twitter credentials. We gave each thread unique Twitter credentials, and this fixed the issue of recieving 420 errors.
---
##Cassandra
###Bug: Fatal exception during initialization org.apache.cassandra.exceptions.ConfigurationException: Found system keyspace files, but they couldn't be loaded! 
###Solution: Execute the command ```sudo rm -rf /VOLUME/Cassandra/data/system'''
