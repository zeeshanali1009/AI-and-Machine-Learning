# strngs in python are used to store the values like names or any thing inside the inverted commas 
# here we have an example like 
# declaration part 
string_data  = "Zeeshan"
# here we will be using some functoins along with the strings which are as:
print(len(string_data))
print(string_data.find("e"))       # finds the index of the given subpart
print(string_data.rfind("e"))          # finds the highest existing inedx number of the subpart from the string
print(string_data.capitalize())
print(string_data.lower())
print(string_data.upper())
print(string_data.isalpha())
print(string_data.isdigit())
print(string_data.count("e"))  # will count the existing counts of the e
print(string_data.replace("Z", "z"))  # will replace the Z with the z

# now we have an exercise for our practice as it is as :
# validate the user inputs using the following conditions 
# 1. input must be not greater then 12 characters
# 2. user name must not contain the spaces 
# 3. user name must not contains the digits

# solution:
string_input  = input ("Enter your name!")
if(len(string_input) > 12):
    print("User name must not be greater then the 12 characters. Please try again!")
    string_input  = input ("Enter your name!")
elif (string_input.find(" ")):
    print("User name must not contain the empty spaces. Please try again!")
    string_input  = input ("Enter your name!")
elif (string_input.isdigit()):
    print("User name must not contain the digits. Please try again!")
    string_input  = input ("Enter your name!")
else:
    print(f"Welcome dear {string_input}")

    
    


