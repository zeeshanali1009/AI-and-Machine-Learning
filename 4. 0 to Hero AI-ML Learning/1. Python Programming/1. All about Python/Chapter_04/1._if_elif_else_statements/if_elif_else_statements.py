# if elif and else are the statements which decides the flow of the program 


age = int(input("Enter your age: "))

# if (age >= 18):
#     print("You are eligible to cast the vote!")
# else:
#     print("You are not eligible to cast the vote!")


# this same process can also be posible with many other ways like we can use the elif statements as well for 
# other coditions as well 
if (age >= 18):
    print("You are eligible to cast the vote!")
elif (age < 0):
    print("Invalid age!")
else:
    print("You are not eligible to cast the vote!")



