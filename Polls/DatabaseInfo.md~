INSERTS INTO CASSANDRA SO FAR

```
2016-president 2014-01-01 2016-01-25
```

TESTING

```
SELECT * FROM junk.polls;
SELECT pollster FROM junk.polls WHERE startDate = '2014-01-10';

This will cause an error:

SELECT name FROM junk.polls WHERE name = 'Obama Job Approval'

...because the primary key is (startDate, endDate, name) and a primary key can't be restricted if a preceeding part of the primary key isn't. It might be worth throwing away the table and using a different primary key, or figure out how to use Solr to fix this.
```