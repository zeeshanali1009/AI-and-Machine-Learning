# identity operaters atre used to compare the memory location of the variables
# is                returns true if the memory locations are same 
# is not            returns true if memory locations are not same 

first_list = [12,345,67,79,"Zeeshan"]
second_list = first_list
third_list= [12,345,67,79,"Zeeshan"]

# is identity operater 
if (first_list is second_list):
    print("The memory locations are same for these lists")
else:
    print("The memory location is not same")

# is not identity operater 
if (first_list is not second_list):
    print("The memory locations are same for these lists")
else:
    print("The memory location is not same")

# this can also be checked by more simpler method
print(first_list is second_list)      # returns TRUE
print(first_list is third_list)      # returns FALSE
