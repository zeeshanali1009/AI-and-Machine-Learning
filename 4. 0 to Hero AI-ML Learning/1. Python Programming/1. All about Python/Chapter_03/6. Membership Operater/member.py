# Membership operaters atre used to compare the data/values of the variables
# in                returns true if the memory locations are same 
# not in           returns true if memory locations are not same 

this_list = [12,345,67,79,"Zeeshan"]


# is identity operater 
if (12 in this_list):
    print("The number 12 is present in the list")
else:
    print("The number 12 is not present in the list")

# is identity operater 
if (12 not in this_list):
    print("The number 12 is not present in the list")
else:
    print("The number 12 is present in the list")

# this can also be checked by more simpler method
print(12 in this_list)      # returns TRUE
print(12 not in this_list)      # returns FALSE
