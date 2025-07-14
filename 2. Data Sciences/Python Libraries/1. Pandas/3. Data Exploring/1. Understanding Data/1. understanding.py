# One of the most important step is the data understanding as there are the following steps involved in it:
# number of rows and coloumns 
# finding the missing data 
# removing the duplications
# planing the next steps for the solution of the problem
import pandas as pd
this_dictionary ={
    "Name" : ["Babar Azam","Saim Ayub", "Muhammaad Haris", "Salman Agha", "Muhammad Rizwan", "Irfan Khan Niazi", 
               "Shadab Khan","Shaheen Afridi", "Haris Rauf", "Naseem Shah", "Sufyan Muqeem"],
    "Score" : [56,17,45,67,12,45,12,3,4,6,0],
    "Wickets": [0,3,0,5,78,12,56,78,89,12,89]
}

df  = pd.DataFrame(this_dictionary)
print(df.head(7))                   # by default it will show the first 5 values if n is not given 
print(df.tail(7))                   # by default it will show the first 5 values if n is not given 
 