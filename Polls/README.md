#Huffington Post Pollster API in Python

###Documentation, Source Code and Examples:

http://elections.huffingtonpost.com/pollster/api

https://github.com/huffpostdata/python-pollster

###Installing:

```
sudo easy_install pollster
```

###Example Programs:

```
python PollByDate.py <start_date> <end_date>
Date format: YYYY-MM-DD

python PollByTopic.py <topic>
Use "python PollByTopic.py -showall" to see all topics

python PollByPollster.py <pollster>
```

###To See Structure:

```
python PollStructure.py
```

###Explanation of Structure:

`pollster.charts()` returns a long list of 'charts' which are categories of polls.

eg: `<Chart: 2012 Iowa GOP Primary>, <Chart: 2012 New Hampshire GOP Primary>, <Chart: 2012 South Carolina GOP Primary>, ...`

`pollster.charts(topic = <topic>)` will narrow down the list of returned charts to only includes items relevant to the topic. A list of valid topics is included in the usage message of the `PollByTopic.py` file.

eg: setting topic to 'obama-job-approval' returns
`<Chart: Obama Job Approval>, <Chart: Obama Job Approval - Economy>, <Chart: Obama Job Approval - Health>, ...`

`pollster.charts()[0].estimates` returns a series of dictionaries containing all the relevnt values of a certain poll, eg candidate names and the percent of the vote they have. Note that this is an average of all the poll numbers of this type over a period of time.

eg: `{u'first_name': u'Mitt', u'last_name': u'Romney', u'value': 22.5, u'choice': u'Romney', u'incumbent': False, u'party': u'Rep', u'lead_confidence': None}, ...`

`pollster.charts()[0].estimates_by_date` returns all of the individual polls that `pollster.charts()[0].estimates` averages, along with the date of the poll.

eg: `{u'date': u'2011-12-30', u'estimates': [{u'value': 13.6, u'choice': u'Gingrich'}, {u'value': 3.6, u'choice': u'Huntsman'}, ...`