from pymongo import MongoClient
import time
import re

client = MongoClient('localhost', 27017)
db = client['sahamyab']
series_collection = db['tweets']

start_time = time.time() 
for document in series_collection.find({'content':{'$regex':'.*#.*'}}): 
    hashtags_sharp = re.findall('#\w+', document['content'])
    hashtags = [o.split('#')[1] for o in hashtags_sharp]  #removing shashtag sign
    new_dict = {"hashtags": hashtags }
    db.tweets.update(document, {"$set": new_dict })  

end_time = time.time()
delta_time = end_time - start_time
print(delta_time)
    
###################### Implementing in pymongo ####################   
#db.tweets.update_many(
#   {'content':{'$regex': '.*#.*'}},
#   [{'$set':{'‫‪hashtags‬‬': {'$regexFindAll': { 'input': '$content' , 'regex': '#.*'}}}
#   }])

  
