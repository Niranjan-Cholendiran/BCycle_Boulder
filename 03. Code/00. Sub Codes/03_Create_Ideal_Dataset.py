import pandas as pd
from itertools import product

# Decide the start and end datetime
start_datetime = '2023-10-31 00:00:00' # str(df['date_rnd'].min()) + " 00:00:00"
end_datetime = '2023-11-06 23:57:00' # str(df['date_rnd'].max()) + " 23:57:00"

# Create a datetime range with a 3-minute gap interval
datetime_range = pd.date_range(start=start_datetime, end=end_datetime, freq='3T')

# List of 54 unique station IDs
station_ids = ['bcycle_boulder_1855', 'bcycle_boulder_1858', 'bcycle_boulder_1859', 'bcycle_boulder_1860', 'bcycle_boulder_1861', 'bcycle_boulder_1866', 'bcycle_boulder_1867', 'bcycle_boulder_1869', 'bcycle_boulder_1870', 'bcycle_boulder_1871', 'bcycle_boulder_1872', 'bcycle_boulder_1873', 'bcycle_boulder_1943', 'bcycle_boulder_2021', 'bcycle_boulder_2022', 'bcycle_boulder_2132', 'bcycle_boulder_2144', 'bcycle_boulder_2161', 'bcycle_boulder_2182', 'bcycle_boulder_2198', 'bcycle_boulder_2756', 'bcycle_boulder_2757', 'bcycle_boulder_2759', 'bcycle_boulder_2760', 'bcycle_boulder_2761', 'bcycle_boulder_2762', 'bcycle_boulder_2763', 'bcycle_boulder_2764', 'bcycle_boulder_2765', 'bcycle_boulder_2766', 'bcycle_boulder_2767', 'bcycle_boulder_2768', 'bcycle_boulder_2769', 'bcycle_boulder_2770', 'bcycle_boulder_2771', 'bcycle_boulder_2875', 'bcycle_boulder_3318', 'bcycle_boulder_3379', 'bcycle_boulder_3589', 'bcycle_boulder_3675', 'bcycle_boulder_3676', 'bcycle_boulder_3876', 'bcycle_boulder_3894', 'bcycle_boulder_4091', 'bcycle_boulder_4142', 'bcycle_boulder_4656', 'bcycle_boulder_4657', 'bcycle_boulder_7305', 'bcycle_boulder_7314', 'bcycle_boulder_7327', 'bcycle_boulder_7345', 'bcycle_boulder_7346', 'bcycle_boulder_7387', 'bcycle_boulder_7393']
# station_ids = df['station_id'].unique()

# Creating combinations
combinations = list(product(datetime_range, station_ids))

# Creating the ideal dataframe using the combinations
df_ideal = pd.DataFrame(combinations, columns=['Datatime_ideal', 'station_id_ideal'])

print("Is the size of ideal datasets [number of datetime] * [54 stations]:", df_ideal.shape[0] == len(df_ideal['Datatime_ideal'].unique()) * len(df_ideal['station_id_ideal'].unique()) )
