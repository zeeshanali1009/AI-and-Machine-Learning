# spltting in the python is used to split the strings into variety of ways like
simple_text  = "This is the textual data."
print(simple_text.split("i"))    # while the i will become exclusive 
print(simple_text.split())
simple_text  = " This is the textual data "
# now we have the function like maxsplit which is also very much usefull it specifies the split function
# that how many splits will it make during the function execution
address = "560000, Lahore, Pakistan"
print(address.split(maxsplit=1))        # it will split only the postal addrss while the remianing addrress will remain same.

