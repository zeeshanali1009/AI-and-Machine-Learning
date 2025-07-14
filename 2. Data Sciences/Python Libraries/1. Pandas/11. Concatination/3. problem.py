# there are the two relationships like customers and their transaction history we have to merge
#  both of them on the basis of ids and save the record of new customers using
#  the concatination

import pandas as pd

# Existing customers
customers = {
    "CustomerID": [101, 102, 103, 104],
    "Name": ["Ali", "Zara", "Ahmed", "Sana"],
    "Email": ["ali@example.com", "zara@example.com", "ahmed@example.com", "sana@example.com"]
}

# Transaction history
transactions = {
    "TransactionID": [201, 202, 203, 204],
    "CustomerID": [101, 102, 101, 103],
    "Amount": [500, 1500, 200, 700]
}

df_customers = pd.DataFrame(customers)
df_transactions = pd.DataFrame(transactions)

df_merged = pd.merge(df_customers, df_transactions, on="CustomerID", how="inner")
print("Merged Data:")
print(df_merged)

# New customers
new_customers = {
    "CustomerID": [105, 106],
    "Name": ["Hassan", "Iqra"],
    "Email": ["hassan@example.com", "iqra@example.com"]
}

df_new_customers = pd.DataFrame(new_customers)


df_all_customers = pd.concat([df_customers, df_new_customers], ignore_index=True)
print("\nAll Customers (after adding new):")
print(df_all_customers)


df_all_customers.to_csv("all_customers.csv", index=False)
df_merged.to_csv("merged_transactions.csv", index=False)
