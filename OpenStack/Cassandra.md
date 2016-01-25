#For info about connecting to Cassandra within python, visit https://pypi.python.org/pypi/cql/1.4.0
---
#1. Info about our Database:
---
##We have a table for each candidate. The primary key name for each table is tweet_id, and the value name for each table is tweet (this is the tweet's text field).

---
#2. Example interaction with our databases:
---
##To look at all of the tweet ids of all of the tweets for Trump, you would use the command:
---
###SELECT tweet_id from trump;
---
##IF I just want to look at the text fields from tweets about Trump, you would use the command:
---
###SELECT tweet from trump;
---
#3. Useful Cassandra Commands:
---
##1. Use a keyspace
###   USE name_of_keyspace;
---
##2. Print out rows in a table
###   SELECT * from name_of_table;
---
##3. Count number of rows in table
###   SELECT COUNT(*) from name_of_table;

##4. Create table Bernie3
CREATE TABLE bernie3 (
  created_at text PRIMARY KEY,
  tweet_id bigint,
  coordinates list<float>,
  retweet_count int,
  favorite_count int,
  hashtags list<text>,
  lang text,
  quoted_status_id bigint
);
