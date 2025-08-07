# Conditional statements are used to evaluate the different condition based on their validity.
# condition involves the if-elif and else parts
# like we have the following examples here 

# string_input  = input ("Enter your name!")
# if(len(string_input) > 12):
#     print("User name must not be greater then the 12 characters. Please try again!")
#     string_input  = input ("Enter your name!")
# elif (string_input.find(" ")):
#     print("User name must not contain the empty spaces. Please try again!")
#     string_input  = input ("Enter your name!")
# elif (string_input.isdigit()):
#     print("User name must not contain the digits. Please try again!")
#     string_input  = input ("Enter your name!")
# else:
#     print(f"Welcome dear {string_input}")


# we will be discussing another case here which is as 
list_1  = [1,2,3]
list_2  = [1,2,3]

if (list_1 == list_2):
    True
else:
    False

print(id(list_1))
print(id(list_2))

# there relevant ids would be different because they exist at the different memory locations 
if (id(list_1) == id(list_2)):
    True
else:
    False

list_1  = [1,2,3]
list_2  = list_1
print(id(list_1))
print(id(list_2))
# there relevant ids would be same now because they exist at the same memory locations 
if (id(list_1) == id(list_2)):
    True
else:
    False





