import pymongo
from pymongo import MongoClient
import time
import pprint

client = MongoClient('localhost', 27017)
db = client['sahamyab']
series_collection = db['tweets']

### Adding index to field
series_collection.create_index([("mediaContentType", pymongo.DESCENDING), ("parentId", pymongo.DESCENDING)])

start_time = time.time() 
res = series_collection.find({
    '$and':[
              {'mediaContentType':'image/jpeg'}, {'parentId':{ '$exists': True } } 
           ]}, {"senderName": 1, '_id':0})

end_time = time.time()
delta_time = end_time - start_time
print('run time:', delta_time)

lis = []
for i in res:
    lis.append(i['senderName'])
    pprint.pprint(i)

