#Tests

**_Test #1_**  
**File(s):** PollGrabber.py  
**Purpose:** Ensure poll data is in Cassandra  
**Details** _(setup, step-by-step explanation so test can be recreated)_:   
1. Manually create Cassandra table on OpenStack  
2. Run PollGrabber.py: `python PollGrabber.py <any topic> <any start date> <any end date>`  
3. Log back into cqlsh, run `SELECT * FROM junk.polls`  
4. See all that wonderful data  
**Pass/Fail?:** PASS  
______________________________________________________________________________
**_Test #2_**  
**File(s):** PollGrabber.py  
**Purpose:** Demonstrate uerying limitations in Cassandra  
**Details** _(setup, step-by-step explanation so test can be recreated)_:   
1. Populate Cassandra database with poll info (in this case in junk.polls)  
2. Log into cqlsh, run `SELECT pollster FROM junk.polls WHERE startDate = '2014-01-10';`  
3. One poll will be returned  
4. run `SELECT name FROM junk.polls WHERE name = 'Obama Job Approval'`  
5. This will throw an error. See DatabaseInfo.md for details  
**Pass/Fail?:** PASS  
______________________________________________________________________________
**_Test #3_**  
**File(s):** PollGrabber.py
**Purpose:** Ensure polls are now being ordered by end_date
**Details** _(setup, step-by-step explanation so test can be recreated)_:   
1. used print statement in a for loop to print all end_date values of self.all_polls
2. observed in terminal that end_date values were in increasing rder (older polls first)
**Pass/Fail?:** PASS  
______________________________________________________________________________
**_Test #4_**  
**File(s):** PollGrabber.py  
**Purpose:** Ensure polls are now being ordered by end_date  
**Details** _(setup, step-by-step explanation so test can be recreated)_:   
1. used print statement in a for loop to print all end_date values of self.all_polls  
2. observed in terminal that end_date values were in increasing rder (older polls first)  
**Pass/Fail?:** PASS  
______________________________________________________________________________
**_Test #5_**  
**File(s):** query.py  
**Purpose:** test if dates are being interpreted correctly  
**Details** _(setup, step-by-step explanation so test can be recreated)_:  
1. ran file with 20160101 and 20160102 as the start/end date arguments  
2. observed that counts were 0, realized incorrect date format was used as input  
**Pass/Fail?:** FAIL  
______________________________________________________________________________
**_Test #6_**  
**File(s):** tweetsBetweenPolls.py  
**Purpose:** functionality test - ran program when it seemed to be finished  
**Details** _(setup, step-by-step explanation so test can be recreated)_:  
1. the two newest polls had the same end date
2. ran the program, error was thrown because the two dates it checked for tweets between were the same date
**Pass/Fail?:** FAIL  
______________________________________________________________________________
**_Test #7_**  
**File(s):** tweetsBetweenPolls.py  
**Purpose:** check if error in previous test was corrected  
**Details** _(setup, step-by-step explanation so test can be recreated)_:  
1. re-wrote program so that if the two newest polls have the same date, an older poll will be used as the starting date  
2. ran the program normally  
**Pass/Fail?:** PASS
______________________________________________________________________________
**_Test #8_**  
**File(s):** PollGrabber.py; cassandra database, polls.president table  
**Purpose:** confirming that PollGrabber inserted polls that ended ON the supplied end date  
**Details** _(setup, step-by-step explanation so test can be recreated)_:  
1. ran "SELECT * FROM polls.president WHERE end_date=20160220"  
2. query failed. Tried "SELECT * FROM polls.president WHERE pollster=CNN AND end_date=20160220" in case restricting on the primary key would allow wuery to run
2. query failed
**Pass/Fail?:** FAIL  
This requires further testing on how to query on the polls' end dates.
______________________________________________________________________________
**_Test #9_**  
**File(s):** 
**Purpose:** 
**Details** _(setup, step-by-step explanation so test can be recreated)_:  
1. 
2. 
**Pass/Fail?:** 