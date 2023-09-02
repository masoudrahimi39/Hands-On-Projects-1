from pymongo import MongoClient
import time
import pprint


###########change your time in line of << res=... >>


client = MongoClient('localhost', 27017)
db = client['sahamyab']
series_collection = db['tweets']
start_time = time.time() 

res = series_collection.find(
    {'sendTimePersian':{'$regex':'.* 13:.*'} }, 
    {'senderName':1, 'senderProfileImage':1, '_id':0})

end_time = time.time()
delta_time = end_time - start_time
print(delta_time)

twitt_time_intvrl = []
for i in res:
    twitt_time_intvrl.append([i['senderName'],
                            i['senderProfileImage']])
    pprint.pprint(i)