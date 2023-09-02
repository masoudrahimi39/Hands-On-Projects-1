from kafka import KafkaConsumer
from elasticsearch import Elasticsearch
import json 


def save_to_elasticsearch(consumer_G1_2_topic, elastic_index, data_size):
    
    # start elastic search
    elasticSearch = Elasticsearch([{'host':'localhost', 'port':9200}])
    
    ## initializing Kafka concumer; if auto_offset_reset='latest' producer should be run after concumer
    consumer_G1_2 = KafkaConsumer(auto_offset_reset='earliest', group_id='str2')
    consumer_G1_2.subscribe([consumer_G1_2_topic])
    lis = []
    i = 0 
    # iteration over each message which is received from kafka
    for msg in consumer_G1_2:
        try:
            # decoding msg to json format
            record = json.loads(msg.value)
            
            # changing key named "_meta" to "meta"
            record['meta'] = record.pop('_meta')
            lis.append(record)
            
            # sending data to elastic search 
            elasticSearch.index(index=elastic_index, doc_type='tweeter', body = record)
            print(i)
            i+=1
        except:
            data_size = data_size -1
            pass
        if i > data_size:
            break
        
    consumer_G1_2.close()
    
    
save_to_elasticsearch('processedTest15', 'test15', 5690)