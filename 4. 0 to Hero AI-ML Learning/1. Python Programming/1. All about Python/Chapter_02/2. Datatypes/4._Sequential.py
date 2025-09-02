# Sequential datatype is one of the most important datatype as the sequence may be in the form of
# Strings, lists, tuples , sets 

    # string is the datatype which represents that there will be the sequence of the data 
    # enclosed in the inverted commas
    # Immutable One
this_string = "This is the first string"
 
    # list is the datatype which represents the data will be arranged in a sequence enclosed in 
    # large brackets the data enclosed in the large brackets may be of different datatypes
    # (can be of string,integer, float , bool etc)
    # Mutable One

this_list = [12,45,56.56,"Zeeshan"]

    # tuple is the datatype which represents the data will be arranged in a sequence enclosed in 
    # paranthesis, the data enclosed in the paranthesis may be of different datatypes
    # (can be of string,integer, float , bool etc)
    # ImMutable One
this_tuple = (456,789,234,78.890, "Ali", 'Muhammad')

    # Set is the datatype which represents the data will be arranged in a sequence enclosed in 
    # curly braces, the data enclosed in the curly braces may be of different datatypes
    # (can be of string,integer, float , bool etc)
    # Mutable One
    # Sets prints only the unique numbers.
this_set = {1,2,3,4,5,6,7,8,7,6,5,4,3,2,1}
    # Sets also provides the unique feature of "Frozenset" which makes the sets like frozen
    # Immutable 
    # makes the set like a sealed packed box which can be just seen cannot be open
    # Any sequence datatype can be made frozenset



print(f"This is the String {this_string}")
print(f"This is the list {this_list}")
print(f"This is the tuple {this_tuple}")
print(f"This is the Set {this_set}")

new_list = frozenset(this_list)
print("""Any datatype can be made frozen set as the list is the mutable but when we will be making 
      it frozenset it will be sealed """)
print(new_list)