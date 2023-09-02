from pymongo import MongoClient
import time

client = MongoClient('localhost', 27017)
db = client['sahamyab']
series_collection = db['tweets']
start_time = time.time() 

pipeline = [ {"$match": {'type':'retwit'}}, 
             {"$out": "retwit_collection"}, ]

series_collection.aggregate(pipeline)

series_collection.remove({'type':'retwit'})

end_time = time.time()
delta_time = end_time - start_time
print('run time:', delta_time)

