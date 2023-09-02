from pymongo import MongoClient
import time
import pprint

client = MongoClient('localhost', 27017)
db = client['sahamyab']
series_collection = db['tweets']

start_time = time.time() 
#### finding 10-most relevant tweets:
# filter by day number
filter_time = { '$match': {'sendTimePersian':{ '$regex': '.*/19 .*'}}}
### unwind array elements
unwind_hashtag_arr = { '$unwind': "$hashtags" }  
count_tweets = {'$group' :
    {'_id' : "$hashtags",'twitt_number': { '$sum': 1 }}}
### sorting by tweets number
sort = { '$sort' : { 'twitt_number' : -1 } }
### limiting the most ten hashtags
lim = { '$limit': 10 }
                 
ten_most_relevant = series_collection.aggregate(
     [filter_time, unwind_hashtag_arr, count_tweets, sort, lim])

end_time = time.time()
delta_time = end_time - start_time
print('run time:', delta_time)
for i in ten_most_relevant:
    pprint.pprint(i)    