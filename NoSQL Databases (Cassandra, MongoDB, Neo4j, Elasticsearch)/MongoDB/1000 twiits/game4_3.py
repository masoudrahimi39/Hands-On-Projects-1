from pymongo import MongoClient
import time

client = MongoClient('localhost', 27017)
db = client['sahamyab']
series_collection = db['tweets']

start_time = time.time() 
series_collection.update_many(
              {'parentId':True},
              {'$unset':{'type': '' }})
                              
end_time = time.time()
delta_time = end_time - start_time
print('run time:', delta_time)

