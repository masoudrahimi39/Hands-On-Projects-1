import pandas as pd
import requests
import json
response = requests.get('https://www.sahamyab.com/guest/twiter/list?v=0.1', headers={'User-Agent' : 'chrome/61'})
data = json.loads(response.text)

twiit_10 = data['items']
#for element in twiit_10:
#    df = pd.DataFrame(element.items()) # each twiit in a dataframe
#    df.to_csv(element['id'] + '.csv')