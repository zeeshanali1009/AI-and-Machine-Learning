# here we will be having the discussion on the sets operations as the operations woud be like
# union, union update , intersection, intersection update

# union of the sets
set_1 = {12, 23, 3, 4, 56, 6, 78}
set_2 = {34, 46, 57, 68, 79, 89}
set_4 = {34, 456, 57, 5, 34, 46, 57}
print(set_1.union(set_2, set_4))

# Actually the difference is that for the symbol | or & or - or ^ operands must be the same like we cannot use the tupple  while using 
# the symbols | or & or - or ^  like set_3  = (12,23,4) | or & or - or ^  {12,2,35,46} because there is no conversion point like in the above method there is 
# the conversion point 

# this can also be done using the symbol | 
set_3  = set_1 | set_2 | set_4
print(set_3)

# union update stores the union of the particular sets into the target set like 
set_1.update(set_2, set_4)      # update done in-place, no reassignment
print(set_1)


# intersection of the sets
set_1 = {12, 23, 3, 4, 56, 6, 78}
set_2 = {12, 23, 45, 34, 46, 57, 68, 79, 89}
set_4 = {12, 234, 35, 4, 5, 67, 67}
print(set_1.intersection(set_2, set_4))

# Actually the difference is that for the symbol | or & or - or ^ operands must be the same like we cannot use the tupple  while using 
# the symbols | or & or - or ^  like set_3  = (12,23,4) | or & or - or ^  {12,2,35,46} because there is no conversion point like in the above method there is 
# the conversion point  

# this can also be done using the symbol &
set_3  = set_1 & set_2 & set_4
print(set_3)

# intersection update stores the intersection of the particular sets into the target set like 
set_1.intersection_update(set_2, set_4)
print(set_1)


# Diffference of the sets
set_1 = {12, 23, 3, 4, 56, 6, 78}
set_2 = {12, 23, 45, 34, 46, 57, 68, 79, 89}
set_4 = {12, 234, 35, 4, 5, 67, 67}
print(set_1.difference(set_2, set_4))

# Actually the difference is that for the symbol | or & or - or ^ operands must be the same like we cannot use the tupple  while using 
# the symbols | or & or - or ^  like set_3  = (12,23,4) | or & or - or ^  {12,2,35,46} because there is no conversion point like in the above method there is 
# the conversion point 

# this can also be done using the symbol -
set_3  = set_1 - set_2 - set_4
print(set_3)

# difference update stores the intersection of the particular sets into the target set like 
set_1.difference_update(set_2, set_4)
print(set_1)


# Symmetric diffference of the sets
set_1 = {12, 23, 3, 4, 56, 6, 78}
set_2 = {12, 23, 45, 34, 46, 57, 68, 79, 89}
set_4 = {12, 234, 35, 4, 5, 67, 67}

print(set_1.symmetric_difference(set_2))   # this is applicable for only two sets, sets more then two are dealt with the symbol ^

# Actually the difference is that for the symbol | or & or - or ^ operands must be the same like we cannot use the tupple  while using 
# the symbols | or & or - or ^  like set_3  = (12,23,4) | or & or - or ^  {12,2,35,46} because there is no conversion point like in the above method there is 
# the conversion point 

# this can also be done using the symbol ^
set_3  = set_1 ^ set_2 ^ set_4
print(set_3)

# symmetric difference update stores the intersection of the particular sets into the target set like 
set_1.symmetric_difference_update(set_2)   # only one set allowed at a time
set_1.symmetric_difference_update(set_4)   # again one at a time
print(set_1)


# disjoint,subset,superset checking

set_1 = {"Zeeshan", "Ali", "Muhammad", "Raza"}
set_2  = {"Babar", "Saqib","Shoaib"}
set_3 = {"Ali", "Muhammad"}
print(set_1.isdisjoint(set_2))
print(set_1.issubset(set_2))
print(set_1.issuperset(set_2))
