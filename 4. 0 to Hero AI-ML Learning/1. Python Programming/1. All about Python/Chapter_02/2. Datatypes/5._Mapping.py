# Mapping datatype is one of the most important datatype for the storage of the data
# A dictionary in Python stores data in key-value pairs
# Syntax is like :  {key: value}
# Values can be of any datatype
# Dictionaries are mutable (can be changed)

# Defining a dictionary
record = {
    "Name": "Zeeshan",
    "Age": 20,
    "University": "Superior University Lahore"
}

# Printing the dictionary
print("Student Record Dictionary:")
print(record)

# Accessing individual elements using keys
print("Name:", record["Name"])
print("Age:", record["Age"])
print("University:", record["University"])

# Adding a new key-value pair
record["Program"] = "BS Information Technology"
print("After adding Program key:")
print(record)

# Updating an existing key
record["Age"] = 21
print("After updating Age:")
print(record)

# Getting all keys and values
print("\nAll Keys:", list(record.keys()))
print("All Values:", list(record.values()))


