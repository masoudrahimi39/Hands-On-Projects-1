from pymongo import MongoClient
import time
#import pprint
client = MongoClient('localhost', 27017)
db = client['sahamyab']
series_collection = db['tweets']

start_time = time.time() 
unwind_hashtag_arr = { '$unwind': "$hashtags" }
group_by = {'$group' :{'_id' : "$hashtags",
                       'twitt_number': { '$sum': 1 }}}
sort_most = { '$sort' : { 'twitt_number' : -1 } }
sort_least = { '$sort' : { 'twitt_number' : 1 } }
lim = { '$limit': 1 }
                 
most_Repetitive = series_collection.aggregate(
     [unwind_hashtag_arr, group_by, sort_most, lim])

least_Repetitive = series_collection.aggregate(
     [unwind_hashtag_arr, group_by, sort_least, lim])
### end time
end_time = time.time()
delta_time = end_time - start_time
print('run time: ', delta_time)
print(f'most Repetitive hashtag: {list(most_Repetitive)}')
print(' -------------------------------------------------------- ')
print(f'least Repetitive hashtag: {list(least_Repetitive)}')
