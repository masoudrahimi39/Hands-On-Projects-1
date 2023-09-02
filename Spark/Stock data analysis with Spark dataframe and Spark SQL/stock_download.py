from datetime import date, timedelta
import pandas as pd
import requests
import os
import jdatetime

# start date
start_date = date(2021, 3, 30)   

# end date
end_date = date(2021, 6, 1)   
delta_time = end_date - start_date       
date_list = []
for i in range(delta_time.days + 1 ):
    day = start_date + timedelta(days=i)
    gregorian_date =  jdatetime.date.fromgregorian(day=day.day ,month=day.month,year=day.year)
    url = 'http://members.tsetmc.com/tsev2/excel/MarketWatchPlus.aspx?d='
    url1 = url + str(gregorian_date)
    r = requests.get(url1, allow_redirects=True)
    open(str(gregorian_date)+'.xlsx', 'wb').write(r.content) 
    
#####reading the excel files
    file_size = os.path.getsize(str(gregorian_date)+'.xlsx')
    
    # checking if the file size is not less than 1 KB. 
    #less than 1KB means it is empth file and that day was holidaay.
    if file_size > 10240 :
        df = pd.read_excel(str(gregorian_date)+'.xlsx')
        
        #dropping the first line which is cointained "نماد بازار"
        df = df.drop([0])
        
        #putting the columnn names of dataFrame based on the first row of prior dataFrame 
        df.columns = df.iloc[0]
        
        # dropping the first row. first row was the column names.
        df = df.drop([1])
        
        # save the dataFrame to a csv file.
        df.to_csv(str(gregorian_date)+'.csv')
    
    # removing the .xlsx file if its size is less than 1 KB.
    else:
        os.remove(str(gregorian_date)+'.xlsx')








