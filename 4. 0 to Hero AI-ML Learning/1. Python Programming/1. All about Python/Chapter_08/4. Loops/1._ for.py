# loops can also be used to manipulate into the dictionaries 
contacts = {"name" : "Zeeshan", "phone_no" : "03184269225", "address" :"Kot Radha Kishen"}


# by default it will be returning the keys from th dictionary
for i in contacts:
    print (i)
# for the keys 
for i in contacts.keys():
    print (i)
# for the values
for i in contacts.values():
    print (i)
# for the items in the dictionary
for i in contacts.items():
    print (i)