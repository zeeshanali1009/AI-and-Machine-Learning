# update method is also being used to update the lists using the indexing
this_list = [1,2,3,4,5,6,7,8,9,"Zeeshan",True]
print(f"List before the updation: {this_list}")

this_list[0] = "Muhammad"
print(f"List after the updation: {this_list}")

# we can also update the given range by the slicing method 
this_list[0:4] = "Zeeshan", "Ali Raza", "Sufyan Muqeem", "Luke Wood"
print(this_list)
