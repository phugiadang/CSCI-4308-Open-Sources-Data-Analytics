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
**File(s):**   
**Purpose:**   
**Details** _(setup, step-by-step explanation so test can be recreated)_:   
1.   
2.   
3.  
**Pass/Fail?:**   