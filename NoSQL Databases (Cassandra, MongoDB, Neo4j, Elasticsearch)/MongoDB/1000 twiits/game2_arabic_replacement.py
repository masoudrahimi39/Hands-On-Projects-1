from pymongo import MongoClient
import re
import time

    
client = MongoClient('localhost', 27017)
db = client['sahamyab']
series_collection = db['tweets']

start_time = time.time()
for document in series_collection.find({'content':{'$regex':'.*ك.*|.*ي.*'}}):
    new_dict = document.copy()
    new_dict['content'] = re.sub('ي', 'ی', new_dict['content'])
    new_dict['content'] = re.sub('ك', 'ک', new_dict['content'])
    db.tweets.update(document, new_dict)  

end_time = time.time()
delta_time = end_time - start_time 
print(delta_time)