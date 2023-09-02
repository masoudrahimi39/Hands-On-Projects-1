from pymongo import MongoClient
import time
import pprint

client = MongoClient('localhost', 27017)
db = client['sahamyab']
series_collection = db['tweets']
start_time = time.time() 
# filter by day number. here I filtered by 14.
filter_time = { '$match': {'sendTimePersian':{ '$regex': '.*/19 .*'}}}
# group by senderUsername and counting each one tweets
count_tweet_of_each_ID = {'$group' :{
          '_id' : "$senderUsername",
          'twitt_number': { '$sum': 1 }}}
### sorting by tweets number
sort = { '$sort' : { 'twitt_number' : -1 } }
### limiting the most ten hashtags
lim = { '$limit': 1 }
project = {'$project' : { "twitt_number":1, 'sendTimePersian':1 }}
                    
res_one_tweet = series_collection.aggregate(
     [filter_time, count_tweet_of_each_ID, sort, lim])

end_time = time.time()
delta_time = end_time - start_time
print('run time:', delta_time)
for i in res_one_tweet:
    pprint.pprint(i)    
