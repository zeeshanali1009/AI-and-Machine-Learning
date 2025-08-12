import pandas as pd

League01 = {
    "Name": ["Babar Azam", "Saim Ayub", "Muhammaad Haris", "Salman Agha", None, "Irfan Khan Niazi", 
             "Shadab Khan", "Shaheen Afridi", "Haris Rauf", "Naseem Shah", "Sufyan Muqeem"],
    "Age": [30, 21, 19, 30, 32, 44, 30, 24, 30, 21, 24],
    "Score": [56, 17, 45, 67, 12, 45, 12, 3, 4, 0, 0],
    "Wickets": [0, 3, 0, 5, 78, 12, 56, 78, 89, 12, 89]
}

League02 = {
    "Name": ["Babar Azam", "Saim Ayub", "Muhammaad Haris", "Salman Agha", None, "Irfan Khan Niazi", 
             "Shadab Khan", "Shaheen Afridi", "Haris Rauf", "Naseem Shah", "Sufyan Muqeem"],
    "Age": [30, 21, 19, 30, 32, 44, 30, 24, 30, 21, 24],
    "Score": [56, 34, 34, 57, 24, 67, 34, 57, 34, 23, 56],
    "Wickets": [12, 34, 56, 67, 79, 45, 78, 55, 34, 68, 78]
}


df1 = pd.DataFrame(League01)
df2 = pd.DataFrame(League02)

# Merge on 'Name'
df_merged = pd.merge(df1, df2, on="Name", how="inner")

print(df_merged)
