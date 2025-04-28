import pandas as pd

df = pd.read_csv(r"C:\Users\Zeeshan Ali\Desktop\AI-and-Machine-Learning\Pandas\annual-enterprise-survey-2023-financial-year-provisional-size-bands.csv")
# gives the first few rows and coloumns from the data 
# print(df.head())
# gives the last few rows and coloumns from the data 
# print(df.tail())
# analyze the rows and coloumn respectively 
# print(df.shape())
# analyzes which type of data exists in the file
# print(df.dtypes())



# now we will be discovering something more about the other numeric features which can be applied on the 
# structured data

# Average (mean,median,mode) these are the three methods which can be applied to find the average as
# there are the clear differences in each method
# mean is not mostly favorabble as it fluctauates the result when there is the dispersion in the data
# median is the most favorable as the data is in the sorted pattern and it easy to find the central tendency
# mode is again not mostly favorabe as there can be no mode and can be more then one as well

# Dispersion  (Inter Quartile Range)
# Q1  is covering the data under 25%  (first quartile)
# Q2  is covering the data under 50% also known as the median 
# Q3  is covering the data under 75% (third quartile )
# Q4  is covering the data under 75 - 100% (fourth quartile)
# IQR = Q3 - Q1 

# ther are the multiples functions present in the pandas library as can be used to find all the relevant 
# functioning

# this function gives the all the necesaary outputs relevant to the numeric data like all the quartiles 
# mean , standard deviaion , highest , minimum etc  
# it can be applied on the overall dataset and on the specific attribute or instance as well

# on the complete dataset
print(df.describe)

# on the specific attribute
print(df['value'].describe())

# this function prints the value present at that given location
print(df.iloc[22])

# this function prints the value relative to the given string 
# print(df.loc["Total expenditure."])

# it will be sorting the year attribute by ther by default pattern "accsending order" which can be 
# changed as well
df.sort_values(by="year").head()

# in the descending order
df.sort_values(by="year", ascending=False).head()


# it wil be printing the attribute "industry_code_ANZSIC"
df["industry_code_ANZSIC"].head()

# the condition applying on the year attribute to print the data of only year 2011
df[df["year"] == "2011"]


# it will be printing the data after the year 2011
after_2011 = df["year"] > 2011
df[after_2011]


# it will be printing the data within the range 
filter_data = df["year"].between (2011,2020)
df[filter_data]


