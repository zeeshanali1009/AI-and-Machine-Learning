# common is like finding the common item from the tuple

tuple_1 = (1,2,3,4,5)
tuple_2 = (5,56,7,8,9)

set_1 = set(tuple_1)
set_2 = set(tuple_2)
common = set_1.intersection(set_2)
print(f"The common item is {common}")