import requests
import json
from pymongo import MongoClient
import time

client = MongoClient('localhost', 27017)
db = client['sahamyab']
series_collection = db['tweets']

start_time = time.time() 
while series_collection.count() < 1000:
    # Getting last 10 twiits
    response = requests.get('https://www.sahamyab.com/guest/twiter/list?v=0.1', headers={'User-Agent' : 'chrome/61'})
    data = json.loads(response.text)
    twiit_10 = data['items']
    # insert data into mongodb
        ### cheching if twitt is not in collection
    for element in twiit_10 :
        if series_collection.find_one(element) == None:
            result = series_collection.insert_one(element)
        
    time.sleep(60 - time.time() % 60)
    
end_time = time.time()
delta_time = end_time - start_time

#print(series_collection.count())
    

