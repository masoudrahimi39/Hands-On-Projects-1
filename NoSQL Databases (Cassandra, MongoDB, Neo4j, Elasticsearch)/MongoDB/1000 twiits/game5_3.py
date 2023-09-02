from pymongo import MongoClient
import time
import pymongo

client = MongoClient('localhost', 27017)
db = client['sahamyab']
series_collection = db['tweets']

### Adding index to field
series_collection.create_index(
        [("senderUsername", pymongo.DESCENDING)])
start_time = time.time() 
#### finding users with one tweet:
count_tweet_of_each_ID = {'$group' :
    {'_id' : "$senderUsername",'twitt_number': { '$sum': 1 }}}
match_gtr_4 = {'$match': { "twitt_number": { '$eq': 1 } }}
project = {'$project' : { "twitt_number":1, '_id': 0}}
                    
res_one_tweet = series_collection.aggregate(
     [count_tweet_of_each_ID, match_gtr_4, project])
#### finding users with 2&3 tweets:
count_tweet_of_each_ID = {'$group' :{
    '_id' : "$senderUsername",'twitt_number': { '$sum': 1 }}}
match_gtr_4 = {'$match': { "twitt_number": { '$gt': 1, '$lt': 4 } }}
project = {'$project' : { "twitt_number":1, '_id': 0}}
                    
res_2_3_tweets = series_collection.aggregate(
     [count_tweet_of_each_ID, match_gtr_4, project])
#### finding users with more than 3 tweets:
count_tweet_of_each_ID = {'$group' :{
          '_id' : "$senderUsername",
          'twitt_number': { '$sum': 1 }}}
match_gtr_4 = {'$match': { "twitt_number": { '$gte': 4 } }}
project = {'$project' : { "twitt_number":1, '_id': 0}}
                    
res_more_than_3 = series_collection.aggregate(
     [count_tweet_of_each_ID, match_gtr_4, project])
end_time = time.time()
delta_time = end_time - start_time
print('run time:', delta_time)
print(f'Number of users with one tweet: {len(list(res_one_tweet))}')
print(f'Number of users with two and three tweets: {len(list(res_2_3_tweets))}')
print(f'Number of users with more than three tweets: {len(list(res_more_than_3))}')
