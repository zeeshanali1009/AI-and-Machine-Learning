# mean value can be added into the missing value by using the fillna() method as it makes the data more consistent 

import pandas as pd

data = {
    "Name": ["Babar Azam", "Saim Ayub", "Muhammaad Haris", "Salman Agha", None, "Irfan Khan Niazi", 
             "Shadab Khan", "Shaheen Afridi", "Haris Rauf", "Naseem Shah", "Sufyan Muqeem"],
    "Age": [30, 21, 19, 30, 32, None, 30, 24, 30, 21, 24],
    "Score": [56, 17, 45, 67, 12, 45, 12, 3, 4, None, 0],
    "Wickets": [0, 3, 0, 5, 78, 12, 56, 78, 89, 12, 89]
}
df = pd.DataFrame(data)
df["Age"].fillna(df["Age"].mean(), inplace=True)
print(df)