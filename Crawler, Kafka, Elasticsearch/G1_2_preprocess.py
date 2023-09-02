from kafka import KafkaConsumer, KafkaProducer, TopicPartition
import json
import uuid
import re
from urlextract import URLExtract   # a lib. in order to extract urls
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer


# defining a function to find hashtags of a string and put those in a list
def hashtags_ext(text):   
    hashtags_sharp = re.findall('#\w+', text)
    hashtags = [o.split('#')[1] for o in hashtags_sharp]  #removing shashtag sign
    return hashtags


def preprocess(consumer_G1_1_topic, producer_G1_2_topic, data_size):
    
    # reading stopWords from file
    with open("persian_stop_words-Copy.txt", "r",  encoding="utf8") as file:
        stop_words = file.readlines()
        stop_words = [line.rstrip() for line in stop_words]
    # adding white space to the stop_words
    stop_words.append(' ')
    stop_words.append('')
    
    # a list containing some key words in order to extract keyWords from each tweet
    some_keyWords = ['اقتصاد', 'بورس', 'انتخابات','دلار'
                     ,'تحریم','دولت', 'طلا' ,'حسن روحانی','کرونا'             
                     ,'کوید۱۹','تورم','دانشگاه','کوید','covid'             
                     ]
    
    # in order to find links 
    extractor = URLExtract()
    
    ## initializing Kafka concumer; if auto_offset_reset='latest' producer should be run after concumer
    consumer_G1_1 = KafkaConsumer(auto_offset_reset='earliest')
    consumer_G1_1.subscribe([consumer_G1_1_topic])
    
    # obtaining the last offset value
    #topic = 'test1'
    #tp = TopicPartition(topic, 0)
    #consumer.seek_to_beginning(tp)
    #lastOffset = consumer.position(tp)
    
    
    # processed tweets and its details will be appended to below list.
    records = [] 
    # a blank list in order to put all tweets content in it
    all_contents = [] 
    a = 0 
    # aa = 5740
    # iteration over each message which is received from kafka
    for msg in consumer_G1_1:
        
        # decoding msg to json format
        record = json.loads(msg.value)
        
        # do process if the tweet has the content field in it
        if 'content' in record:
            try:
                
                ### adding UUID for each tweet
                record['id'] =  str(uuid.uuid4())
        
                # finding the words that are in the list of some_keyWords and appned them in key_words
                key_words = []
                for element in some_keyWords:
                    if len(re.findall(element, record['content'])) != 0:
                        key_words.append(''.join(re.findall(element, record['content'])))
                            
                ### adding some information as meta_data to each tweet;
                record['_meta'] = {
                        'UUID' : record['id'],
                        'topic': msg.topic,
                        'partition': msg.partition,
                        'offset': msg.offset,
                        'timestamp': msg.timestamp,
                        'hashtags' : hashtags_ext(record['content']),    # adding list of hashtags
                        'key_words' : key_words
                }
                
                ### adding list of links to each tweet
                record['links'] = extractor.find_urls(record['content'])
                
                # appending each tweet's text to below list
                all_contents.append(record['content'])
                
                # appending each tweet and its deatils to below list
                records.append(record)
            except:
                data_size = data_size - 1 
                
        a+=1
        print(a)
        if a == data_size:
            break
    #     checkig if the consumer obtain the last offset value 
    #    if msg.offset == lastOffset - 1:
    #        break
    consumer_G1_1.close()
    
    
    # running producer in order to send preprocessed data to kafka topic
    producer_G1_2 = KafkaProducer(bootstrap_servers=['localhost:9092'],
                             value_serializer=lambda x: 
                             json.dumps(x).encode('utf-8'))
        
    ### finding tf-idf for words in each tweet
    tfidf_vectorizer = TfidfVectorizer(stop_words=stop_words, use_idf=True)
    tfidf_vectorizer_vectors = tfidf_vectorizer.fit_transform(all_contents)
    
    
    # iteration over all tweets in order to find keywords
    for i in range(len(all_contents)) : 
        first_vector_tfidfvectorizer = tfidf_vectorizer_vectors[i]
        df = pd.DataFrame(first_vector_tfidfvectorizer.T.todense(), index=tfidf_vectorizer.get_feature_names(), columns=["tfidf"])
        
        # removing words that index are completly digit; i.i. 320 will be removed 
        df = df.loc[(df.index.to_series().str.isdecimal()== False )]
        df = df.sort_values(by=["tfidf"],ascending=False).head(2)
        
        # adding these key_words to the tweet info
        for element in list(df.index):
            if element not in records[i]['_meta']['key_words']:
                records[i]['_meta']['key_words'].append(element)
        
        # sending data to kafka topic named "test_processed1"
        producer_G1_2.send(producer_G1_2_topic, value=records[i])
    
        
    producer_G1_2.flush()


preprocess('test20', 'processedTest21',10000 )