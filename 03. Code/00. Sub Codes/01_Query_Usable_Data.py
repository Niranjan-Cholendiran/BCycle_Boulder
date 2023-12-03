import psycopg2
import pandas as pd

# Connect to the postgrey server using your IP address, username and password
Hostname= "localhost"
HostIP: "192.168.1.155" #Santhosh's IP
Dbname= "DockWatchDB"
Username= "postgres" #Santhosh
Password= "Niranjan_99" #Santhosh_99
Port= 5432
Schema= "mastertables"

conn = psycopg2.connect(
    host= Hostname,
    dbname= Dbname,
    user= Username,
    password= Password,
    port= Port
)

query= "SELECT 	* FROM  Preprocessed.\"Bcycle_Status_TD_Preprocessed\" WHERE DATE BETWEEN '2023-10-31' AND '2023-11-06';"
df = pd.read_sql_query(query, conn)

# All selected Tuesday to Saturday data  are accurate and complete
# Selected Sunday (2023-11-05) data is available only till 17:26:10, remaining are just the duplicates of the last availabe status
# Selected Monday (2023-11-06) data is accureate only after 17:40:44, hence the ones before it just the replicate of Tuesday's (2023-10-31)

# Always close the connection at the end
conn.close()

print(df.head(10))

#df.to_csv("C:\Users\admin\OneDrive - UCB-O365\01. Study\03. CUB Courses\01. Undergoing Courses\03. CSCI 5502- Data Mining\04. Project\01. Data\02. Preprocessed Data\Sample_Usable_Preprocessed_Data.csv",index=False)
df.to_csv('Sample_Usable_Preprocessed_Data.csv',index=False)


