# copy method is used to copy the list items present in the one list to the other 
this_list = [90,34,6734,78,23,67,89,2378,234,68]
another_list = this_list.copy()
print(another_list)

this_list[0] = "Zeeshan"
print(this_list,another_list)