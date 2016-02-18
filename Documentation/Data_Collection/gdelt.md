#Our Utilization of the GDELT Global Knowledge Graph(GKG) in gathering GDELT data
---
---
##We wrote a Python program that gathers all of the GDELT datas for every candidates from the GDELT Global Knowledge Graph. The GKG starts April 1, 2013 and consists of two parallel data streams, one encoding the entire knowledge graph with all of its fields, and the other encoding only the subset of the graph that records "counts" of a set of predefined categories. GDELT runs some machine learning techniques in their events data to create GKG. All files that are downloaded from GKG are in zip format. We created the function to unzip the files, collected only the informations that we need, and stored them to new tsv files that organized by the candidates' names and the dates. We wrote another program that parses each gdelt data, and then converted it into a universal form. Once the gdelt data is in the correct format, it is then stored in our gdelt table within our database.

