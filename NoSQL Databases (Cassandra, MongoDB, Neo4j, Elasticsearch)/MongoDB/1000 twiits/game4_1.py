from pymongo import MongoClient
import time
client = MongoClient('localhost', 27017)
db = client['sahamyab']
series_collection = db['tweets']
start_time = time.time() 
#### finding users with one tweet:
count_tweet_of_each_ID = {'$group' :{'_id' : "$senderUsername",
                                     'twitt_number': { '$sum': 1 }}}
match_1 = {'$match': { "twitt_number": { '$eq': 1} }}
project = {'$project' : { "twitt_number":1, '_id': 0}}
                    
res_one_tweet = series_collection.aggregate(
     [count_tweet_of_each_ID, match_1, project])
#### finding users with 2&3 tweets:
count_tweet_of_each_ID = {'$group' :{'_id' : "$senderUsername",
          'twitt_number': { '$sum': 1 }}}
match_2_3 = {'$match': { "twitt_number": { '$gte': 2, '$lte': 3 } }}
                    
res_2_3_tweets = series_collection.aggregate(
     [count_tweet_of_each_ID, match_2_3, project])
#### finding users with more than 3 tweets:
count_tweet_of_each_ID = {'$group' :{'_id' : "$senderUsername",
          'twitt_number': { '$sum': 1 }}}
match_gtr_4 = {'$match': { "twitt_number": { '$gt': 3} }}
                    
res_more_than_3 = series_collection.aggregate(
     [count_tweet_of_each_ID, match_gtr_4, project])
   
end_time = time.time()
delta_time = end_time - start_time
print('run time :', delta_time)
print(f'Number of one-tweet-user: {len(list(res_one_tweet))}')
print(f'Number of two and three-tweet-user: {len(list(res_2_3_tweets))}')
print(f'Number of more than three-tweets-user: {len(list(res_more_than_3))}')

### printing elements of res_more_than_3
#for i in res_more_than_3:
#    pprint.pprint(i) 