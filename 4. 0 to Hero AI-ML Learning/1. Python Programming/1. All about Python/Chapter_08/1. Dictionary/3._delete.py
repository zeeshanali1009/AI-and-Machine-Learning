# by using the delete keyword we can delete any key from the dictionary 

contacts = {"name" : "Zeeshan", "phone_no" : "03184269225", "address" :"Kot Radha Kishen"}
print(f"The dictionary before the process of deletion: {contacts}")
del contacts["address"]
print(f"The dictionary after the process of deletion: {contacts}")