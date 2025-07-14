# If multiple columns are selected then they will be displayed in the form of dataframe
import pandas as pd

this_dictionary = {
    "Name": ["Babar Azam", "Saim Ayub", "Muhammaad Haris", "Salman Agha", "Muhammad Rizwan", "Irfan Khan Niazi", 
             "Shadab Khan", "Shaheen Afridi", "Haris Rauf", "Naseem Shah", "Sufyan Muqeem"],
    "Score": [56, 17, 45, 67, 12, 45, 12, 3, 4, 6, 0],
    "Wickets": [0, 3, 0, 5, 78, 12, 56, 78, 89, 12, 89]
}

df = pd.DataFrame(this_dictionary)

# Multiple columns
print("\nMultiple Columns (Name and Wickets):")
print(df[["Name", "Wickets"]])
