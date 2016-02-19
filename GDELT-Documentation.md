#GDELT -> Cassandra Documentation

#Approach 1: Daniel

#Making a Keyspace

<h3>First, we must make a keyspace. To make the keyspace for GKG we do as follows:</h3>

<h5>
CREATE KEYSPACE gkg
WITH REPLICATION = { 'class' : 'SimpleStrategy', 'replication_factor' : 3 };
</h5>

<h3>This creates a keyspace "GKG" that repicates itself 3 times over servers so that information is secured if one copy is destroyed.</h3>

#Making a Table

<h3>How the GKG Counts Table was Made (Pseudocode):</h3>

<h5>
CREATE TABLE gkg.gkgcounts 
( column_definition, column_definition, ...)
WITH property AND property ...
</h5>

<h3>Now that we have a keyspace and table, we must take the GKG .CSV file and import it into our empty table.
To do this, we move our GKG .CSV file into the /bin of our cassandra client.
1. Start a Cassandra client: sudo ./cassandra [IP of OpenStack server]
2. Open a new terminal and .cqlsh [IP of OpenStack Server]
3. In our terminal running CQLSH, we write something like this:
</h3>

<h5>COPY gkg.gkgcounts from 'YYYYMMDD.counts.csv' (or whatever you named it in the directory of the OpenStack) with HEADER = TRUE;</h5>

# UNFORTUNATELY, once this line is run the columns are never read in, which means that there is an issue in between importing the file
# and getting the data to move into our CQL Database and the OpenStack server.

#Links:

https://www.youtube.com/watch?v=dhzNJnSeiN4
https://docs.datastax.com/en/cql/3.0/cql/cql_reference/create_table_r.html
