import pandas as pd
# a function to convert month number to it's name
def month_name(num):  
    list1 = ['01','02','03','04','05','06','07','08','09','10','11','12']
    list2 = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 
             'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    for i in range(len(list1)):
        if num == list1[i]:
            month = list2[i]
            break
    return month

# part 3: adding year column to csv file
data = pd.read_csv('fma_dataset.csv')
timestamp_lis = data['date_released'].tolist()
year_list = []
for element in timestamp_lis:
    if str(element).split('-')[0] != 'nan':
        year_list.append(str(element).split('-')[0])
    else:
        year_list.append('null')
data['year'] = year_list

# part 4: adding month column to csv file 
month_list = []
for element in timestamp_lis:
    if str(element).split('-')[0] != 'nan':
        month_list.append(month_name(str(element).split('-')[1]))
    else:
        month_list.append('null')
data['month'] = month_list
data['temp'] = [1]*len(data)

data.to_csv('fma_dataset_edited.csv', index=False)





