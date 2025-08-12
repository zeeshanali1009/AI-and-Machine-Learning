# any particular item from
#  the dataframe can be targeted and can be updated easily using the loc keyword which is as
# follow

import pandas as pd

data = {
    "Name": ["Babar Azam", "Saim Ayub", "Muhammaad Haris", "Salman Agha", "Muhammad Rizwan", "Irfan Khan Niazi", 
             "Shadab Khan", "Shaheen Afridi", "Haris Rauf", "Naseem Shah", "Sufyan Muqeem"],
    "Age": [30, 21, 19, 30, 32, 28, 30, 24, 30, 21, 24],
    "Score": [56, 17, 45, 67, 12, 45, 12, 3, 4, 6, 0],
    "Wickets": [0, 3, 0, 5, 78, 12, 56, 78, 89, 12, 89]
}

df = pd.DataFrame(data)

df.loc[0, "Name"] = "Fakhar Zaman"

print(df)
