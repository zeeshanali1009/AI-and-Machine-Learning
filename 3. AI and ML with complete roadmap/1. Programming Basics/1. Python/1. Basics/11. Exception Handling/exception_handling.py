# Exception handling is an important method to handle the multiple types of errors suppose:
# a = 12 
# b=3 
# print(a/b)
# b=0
# print(a/b)    # it will give us the zero division error
# so for handling these types of errors we use teh exception handling processes


try:
    print("File has been opened!")
    a= int(input("Enter the first number!"))
    b= int(input("Enter the second number!"))
    print(a/b)
except ZeroDivisionError as e:
    print(f"You cannot divide a number by 0,{e}")
except ValueError as e:
    print("You have entered incorrect value!")          # the statements in the except block will only be executed if there is the error in the try block
except Exception as e:
    print("Something went wrong!")

finally:
    print("File has been closed!")              # the statements in the finally statement will always be exeduted in every scenario