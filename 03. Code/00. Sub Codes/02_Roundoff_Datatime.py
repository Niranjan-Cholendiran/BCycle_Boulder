import pandas as pd
import datetime

df=pd.read_csv('/content/Sample_Usable_Preprocessed_Data.csv')

# Round off the datatime to the previous ideal time interval (3 or 1 min)
time_interval_to_round= 3
df['datatime_mtd'] = pd.to_datetime(df['datatime_mtd'], format='%Y-%m-%d %H:%M:%S')
df['datatime_rnd'] = df['datatime_mtd'].apply(lambda x: x - pd.to_timedelta(x.minute % time_interval_to_round, unit='m') - pd.to_timedelta(x.second, unit='s')) # This rounds off the minute and makes the seconds zero

## However, rounding off values will create duplicates, so the below line will take only the first entry of every duplicate. For example, Minute 3, 4, and 5 will become 3- so this takes the first entry (3) as that is the closest representation
df.drop_duplicates(subset=['station_id', 'datatime_rnd'], keep='first', inplace=True)
    # print("Number of duplicates:", df.duplicated(subset=['station_id', 'datatime_rnd']).sum()) # To check duplicates
    # print("Number of duplicates per combination:\n\n", df.groupby(['station_id', 'datatime_rnd']).size().reset_index(name='count_of_duplicates').sort_values(by='count_of_duplicates', ascending=False)) # To check duplicates per combination
'''
    #Alternate way: Just make the seconds zero and multiply the numerator of minute divided by [req_time_interval] with [req_time_interval]

    req_time_interval= 3
    df[min_rounded] = int(df['min']/req_time_interval) * req_time_interval
'''

df.head()