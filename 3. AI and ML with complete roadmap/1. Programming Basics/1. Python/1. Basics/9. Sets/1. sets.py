# sets can also store similar or different types of data into them like it has the following properties
# immutable
# not indexed

set_1 = {12, 23, 34, 45, "Zeeshan", "Ali", True}
# slicing cannot be done in the sets also indexing cannot be done because the sets are not indexed.

# empty set declaration
set_2 = {}    # will return a dictionary in the type(set_2)
print(type(set_2))
set_2 = set()   # this time it will works as a set
print(type(set_2))

# built in functionalities

set_1.add(67)               # adds a new element to the set (only if it doesn't already exist)
print(set_1)

set_1.remove(23)            # removes 23 from the set; raises error if not present
print(set_1)

set_1.discard(67)           # removes 67 if present; doesn't raise error if not
print(set_1)

set_1.pop()                 # removes a random element from the set
print(set_1)

set_1.clear()               # removes all elements from the set; makes it empty
print(set_1)

# we can add the tuple into the set but cannot add the list because the tuple is immutable while the list is mutable
set_5 = {23, 34, 35, 5, 656, 53, 434, 35, (12.35, 454, 5, 46)}
print(set_5)
