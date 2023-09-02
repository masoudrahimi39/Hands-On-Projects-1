from json import dumps
from kafka import KafkaProducer
import requests
import json
import time

# topic = 'test10'  

def produce(producer_G1_1_topic, total):
        
    # initializing a new Kafka producer
    producer_G1_1 = KafkaProducer(bootstrap_servers=['localhost:9092'],
                             value_serializer=lambda x: 
                             dumps(x).encode('utf-8'))
    
    
    
    ## sending data by API requested data to topic named "persianTweets" on kafka
                
    # reading tweet's ids which we have captured before in order to avoid getting redundant tweets
    #with open("seenIds_6000_tweets.txt", "r") as file2:
    #    seenIds = file2.readlines()
    #    seenIds = [line.rstrip() for line in seenIds]
        
    seenIds = list()
    fetched = len(seenIds)
    url = 'https://www.sahamyab.com/guest/twiter/list?v=0.1'  
    # total = 1000
    
    while fetched < total:
        # Getting last 10 tweets
        response = requests.get(url=url, headers={'User-Agent' : 'chrome/61'})
        data = json.loads(response.text)
        tweet_10 = data['items']
        
        for tweet in tweet_10:
            if tweet['id'] not in seenIds:  
                try:
                    producer_G1_1.send(producer_G1_1_topic, value=tweet)    # sendig data to kafka topic
                    seenIds.append(tweet['id'])
                    fetched += 1
                    print('tweet '+str(tweet['id'])+' fetched, total: '+str(fetched))    
                except Exception as e:
                    print(e)   
        # time.sleep(60 - time.time() % 60)
    
    producer_G1_1.flush()
    # Writing  seenIds to a file named "seenIds.txt"
    # with open("seenIds.txt", "w") as file:
    #     file.writelines('\n'.join(seenIds))
        
produce('test20', 1000)
