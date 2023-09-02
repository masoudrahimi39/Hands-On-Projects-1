from pymongo import MongoClient
import time
import pprint

client = MongoClient('localhost', 27017)
db = client['sahamyab']
series_collection = db['tweets']

start_time = time.time() 
unwind_hashtag_arr = { '$unwind': "$hashtags" }

group_by = {'$group' :{'_id' : "$hashtags",
          'twitt_number': { '$sum': 1 }}}

sort = { '$sort' : { 'twitt_number' : -1 } }
                  
res_one_tweet = series_collection.aggregate(
            [unwind_hashtag_arr, group_by, sort])

### end time
end_time = time.time()
delta_time = end_time - start_time
print('Run time', delta_time)
## printing elements of res_more_than_3
for i in res_one_tweet:
    pprint.pprint(i)    

