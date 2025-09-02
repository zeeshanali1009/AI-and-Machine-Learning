contacts = {"name": "Zeeshan", "phone_no": "03184269225", "address": "Kot Radha Kishen"}
# storing the keys into the container
keys = list(contacts.keys())

i = 0
# while loop to go on into the dictionary
while i < len(keys):
    key = keys[i]                       # storing the current key data into the key container/variable
    print(f"{key}: {contacts[key]}")
    i += 1
