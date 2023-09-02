from pymongo import MongoClient
import time

client = MongoClient('localhost', 27017)
db = client['sahamyab']
series_collection = db['tweets']

start_time = time.time() 
series_collection.update_many(
              {'hashtags':{'$in': ['فولاد', 'شستا', 'شبندر'] }},
              {'$set':{'gov': True }})

end_time = time.time()
delta_time = end_time - start_time
print(delta_time)

