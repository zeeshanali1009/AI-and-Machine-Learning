# filteration of the data can be carried out by using the condition which can be single and multiple as well depending 
# upon the condition as the single condition involves the meeting of the single role to be completed
# here we will be discussing the multiple conditions as it involves:

import pandas as pd

data = {
    "Name": ["Babar Azam", "Saim Ayub", "Muhammaad Haris", "Salman Agha", "Muhammad Rizwan", "Irfan Khan Niazi", 
             "Shadab Khan", "Shaheen Afridi", "Haris Rauf", "Naseem Shah", "Sufyan Muqeem"],
    "Score": [56, 17, 45, 67, 12, 45, 12, 3, 4, 6, 0],
    "Wickets": [0, 3, 0, 5, 78, 12, 56, 78, 89, 12, 89]
}

df = pd.DataFrame(data)

# Multiple conditions (AND)
print("\nPlayers who scored > 50 and took more than 10 wickets:")
print(df[(df["Score"] > 50) & (df["Wickets"] > 10)])

# Multiple conditions (OR)
print("\nPlayers who scored > 50 or took more than 80 wickets:")
print(df[(df["Score"] > 50) | (df["Wickets"] > 80)])
