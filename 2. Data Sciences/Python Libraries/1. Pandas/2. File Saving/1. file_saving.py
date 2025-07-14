# If we have completed the process of data manipulation then the next step is the data analysis which can be carried
# using the saved files as we will be seeing the process of file saving now as here it is:
import pandas as pd
this_dictionary ={
    "Name" : ["Babar Azam","Saim Ayub", "Muhammaad Haris", "Salman Agha", "Muhammad Rizwan", "Irfan Khan Niazi", 
               "Shadab Khan","Shaheen Afridi", "Haris Rauf", "Naseem Shah", "Sufyan Muqeem"],
    "Score" : [56,17,45,67,12,45,12,3,4,6,0],
    "Wickets": [0,3,0,5,78,12,56,78,89,12,89]
}
# here the data is simply converted into the dataframe or the table form
df  = pd.DataFrame(this_dictionary)
print(df)
# now we will be trying to save it in the different forms so that we can use it later

df.to_csv("csv_file.csv", index=False)
df.to_csv("csv_file.json", index=False)
df.to_csv("csv_file.xls", index=False)

# the related files have been created successfu;y




