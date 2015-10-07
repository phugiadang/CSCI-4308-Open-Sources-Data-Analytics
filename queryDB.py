from pymongo import MongoClient
import simplejson as json

client = MongoClient()
db = client['test-database']
#collection = db['test-collection']
cursor = db.tweets.find()

for document in cursor:
    print document['text']
    print document['created_at']
