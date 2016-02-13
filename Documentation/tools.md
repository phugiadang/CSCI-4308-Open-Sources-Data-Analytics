#Here are the tools that we used for this project, along with some reasoning behind them.
---
---
#1. Hardware
##a) Open Stack Machines
###The University of Colorado gave us access to their Open Stack cluster for this project. We have two instances running on it, that we use for data retrieval, data storage, and analysis. Since each machine only starts out with 16GB of storage, we decided to expand their capacity by adding a 500GB volume to each instance. We did this in order to have ample space in storing large volumes of data.
---
#2. Data
##a) Twitter
###Twitter is a great resource, becuase you can use it to draw conclusions about the trends of who is talked about, and what people around the world think of them.
##b) GDELT
###For this project, we wanted to know how often a presidential candidate is mentioned in the media, and various news sources. GDELT was perfect for this, as it gives us a giant comma seperated file that shows when a candidate is mentioned in an article. From this, we can then derive the count, or how many articles mentioned a specific candidate.
##c) Huffington Post Pollster API
###The goal of this project was to find a change in number of mentions about a candidate, and then try to see if there is a correlation to a change in poll numbers about that candidate. We chose the Huff Post Polster API, because it was the only API we could find that retrieves polls from most major sources, which is clearly essential in coming to a valid conclusion.
---
#3. Data Storage
##a) Cassandra
###We were initially going to use MongoDB to store our data, until we met with Professor Ken Anderson, who has worked with analyis of data on distributed systems in the past. He explained to us that MongoDB works well if you have a database on only one machine, but if you have it setup on multiple machines, you will lose on the order of half your data. To combat this, he reccomended that we use Cassandra, since it was built on the notion of having a database setup on multiple machines. It works great, because it replicates the data across both of our instances. This way, we will not lose half of our data. Another  benefit is that if one of our instances dies for some reason, we should still have our data on the other instance.
