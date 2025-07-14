# Insert method is the precise method which gives the freedom for the addition of the coloumn at the specific 
# index number 

import pandas as pd

data = {
    "Name": ["Babar Azam", "Saim Ayub", "Muhammaad Haris", "Salman Agha", "Muhammad Rizwan", "Irfan Khan Niazi", 
             "Shadab Khan", "Shaheen Afridi", "Haris Rauf", "Naseem Shah", "Sufyan Muqeem"],
    "Age" : [30,21,19,30,32,28,30,24,30,21,24],
    "Score": [56, 17, 45, 67, 12, 45, 12, 3, 4, 6, 0],
    "Wickets": [0, 3, 0, 5, 78, 12, 56, 78, 89, 12, 89]
}

df = pd.DataFrame(data)
df.insert(0,"Position", [1,2,3,4,5,6,7,8,9,10,11])       # insert(location/Index, Column name, data)
print(df.to_string(index=False))