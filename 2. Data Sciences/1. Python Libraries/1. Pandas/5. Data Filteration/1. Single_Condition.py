# filteration of the data can be carried out by using the condition which can be single and multiple as well depending 
# upon the condition as the single condition involves the meeting of the single role to be completed
import pandas as pd

data = {
    "Name": ["Babar Azam", "Saim Ayub", "Muhammaad Haris", "Salman Agha", "Muhammad Rizwan", "Irfan Khan Niazi", 
             "Shadab Khan", "Shaheen Afridi", "Haris Rauf", "Naseem Shah", "Sufyan Muqeem"],
    "Score": [56, 17, 45, 67, 12, 45, 12, 3, 4, 6, 0],
    "Wickets": [0, 3, 0, 5, 78, 12, 56, 78, 89, 12, 89]
}

df = pd.DataFrame(data)

# Single condition
print("Players who scored more than 50:")
print(df[df["Score"] > 50])

