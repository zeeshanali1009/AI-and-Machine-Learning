# Adding estimated value into missing one
# Advantages
# it keeps the data consistent 
# Preserves the integrity
# Smooth trends
# Avoid data loss
# Disadvantages
# cannot be used with the categorical data

import pandas as pd

data = {
    "Name": ["Babar Azam", "Saim Ayub", "Muhammaad Haris", "Salman Agha", None, "Irfan Khan Niazi", 
             "Shadab Khan", "Shaheen Afridi", "Haris Rauf", "Naseem Shah", "Sufyan Muqeem"],
    "Age": [30, 21, 19, 30, 32,21, 30, 24, 30, 21, 24],
    "Score": [10,20,30,40,50,None,70,80,None,100,110],
    "Wickets": [0, 3, 0, 5, 78, 12, 56, 78, 89, 12, 89]
}
df = pd.DataFrame(data)
df.interpolate(method="linear", axis=0,inplace=True)
print(df)
