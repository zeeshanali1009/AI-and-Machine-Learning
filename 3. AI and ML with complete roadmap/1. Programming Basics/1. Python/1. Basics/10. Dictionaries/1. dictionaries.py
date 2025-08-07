# dictionaries stores the data in the form of pairs(keys, values)
# we will be covering it with full details as :
students_record  = {
    "std1": "Zeeshan",
    "std2": "Juniad",
    "std3": "Haseeb",
    "std4": "Awais",
    "std5": "Mubashir"
}
# for printing the specific calues with the help of keys 
print(students_record["std2"])
print(students_record["std3"])
print(students_record["std3"])

# for updating it would be like 
students_record["std5"] ="Babar"
print(students_record["std5"])

# printing the dictionary 
for std in students_record:
    print(std)          # it will be printing the keys only 

# printing the dictionary 
for std in students_record:
    print(std, students_record[std])          # it will be printing the complete dictionary

# printing can also be done this way

for key, value in students_record.items():
    print(key,value)

# we can also check whether the particular thing exists in the dictionary or not like

if ("Zeeshan" in students_record):
    True
else:
    False

# we can check the lenght of the dictionary as well like
print((len(students_record)))

# removing the particular item would be like
students_record.pop("std4")
print(students_record)

# it would remove the item automatially
students_record.popitem()
print(students_record)

# it would delete the student record of student 2 completely from the memory as well
del students_record["std2"]
print(students_record)

# now if we want to copy the one dictionary from the other dictionary it would be done this way
another_dictionary  = students_record.copy()

# nested dictionaries
country_data  = {
    "South Asian": {"count1": "Pakistan", "count2": "India"},
    "America": {"count1": "New York", "count2": "California"},
}
print(country_data["South Asian"]["count1"])

# creating a squared number array
squared_number  = {x:x**2 for x in range(10)}
print(squared_number)


# default values concept 
keys  = ["count1", "count2", "count3"]
print(keys)
default_value = "Country"
new_dictionary  = dict.fromkeys(keys, default_value)
print(new_dictionary)
# nesting once again and lets see the result again
new_dictionary  = dict.fromkeys(keys, keys)
print(new_dictionary)















