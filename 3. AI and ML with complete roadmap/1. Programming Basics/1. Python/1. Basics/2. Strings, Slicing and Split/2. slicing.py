# slicing is an important concept which is used to remove the specfic substring from the relaevant string using following :
# either it can be done using the indexing[] or using the slice() function 
# where the [start,stop, end] remains same for both of them like 

# here we will be discussing the direct slicing using the index values in the square brackets []
name  = "Zeeshan Ali"
print(f"First name is: {name[0:7]}")
print(f"Last name is: {name[8:11]}")
print(f"Funky name is: {name[0:11:3]}")
print(f"Name in the reversed form is : {name[::-1]}")

# now we will be discussing the same slicing concept using the slice function as it is as follow:

slicing_using_function  = slice(0,7)
print(name[slicing_using_function])

website  = "http://google.com"
website1  = "http://linedin.com"
slicing_using_function  = slice(7,-4)     # 0 represents the start for the slicing and -4 represents the end of the string like the
# end is done using the negative value 
print(website[slicing_using_function])
print(website1[slicing_using_function])
