# Reading the CSV file using pandas
import pandas as pd


# df = pd.read_csv(r"C:\Users\Zeeshan Ali\Desktop\AI-and-Machine-Learning\2. Data Sciences\Python Libraries\Pandas\1. File Reading\csv_file.csv", encoding="Latin1")
# # Displaying the DataFrame
# print(df)


df = pd.read_excel(r"C:\Users\Zeeshan Ali\Desktop\AI-and-Machine-Learning\2. Data Sciences\Python Libraries\Pandas\1. File Reading\excel_file.xls")

print(df)

# for reading the files placed in the cloud storage we can use the additional library naming as the "gcsfs"



