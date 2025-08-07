# tuple also have the ability to store the data of similar or different types
# but it has the following properties like 
# immutable one 
# indexed

tuple_1  = (12,23,34,45,46,56,"Zeeshan", True, 12.12)
print(tuple_1)

tuple_2 = (12)
print(type(tuple_2)) # will recognize it as the int because there is no cooma there

tuple_2 = (12,)
print(type(tuple_2)) # will recognize it as the tuple now because there is cooma there

# tuple_1[5]= "Ali"           # here it is the property of the tuple that it 
# print(tuple_1)              # immutable

# tuples also allows the slicing as it is follow
print(tuple_1[0:10:2])

# nesting in tuples
tuple_4 = (23,45,57,67,78)
tuple_5 = (352335,345,"ali", "hamza")
tuple_6 = (tuple_4, tuple_5)
print(len(tuple_6))
print(tuple_6)

# concatination of tuples
tuple_6  = tuple_5 + tuple_4
print(tuple_6)
print(len(tuple_6))

# built in functions now
print(min(tuple_4))
print(max(tuple_4))
print(tuple_6.count(23))   # will count the existence of item in tuple 
print(tuple_6.index(23))   # will find the index number of the 23 from the tuple

# we can also pass the list into the tuple like
list_1  = [23,4,3,34,34,545,56]
tuple_7 = (12,2,35,45,list_1, "Zeeshan", "Ali")
print(tuple_7)
