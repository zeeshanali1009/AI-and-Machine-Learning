import pandas as pd

df = pd.read_csv(r"C:\Users\Zeeshan Ali\Desktop\AI-and-Machine-Learning\Pandas\annual-enterprise-survey-2023-financial-year-provisional-size-bands.csv")
# gives the first few rows and coloumns from the data 
print(df.head())
# gives the last few rows and coloumns from the data 
print(df.tail())
# analyze the rows and coloumn respectively 
print(df.shape())
# analyzes which type of data exists in the file
print(df.dtypes())


