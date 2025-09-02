try:
    a = int(input("Enter the number!"))
    b = int(input("Enter the number!"))
    result = a/b

except ZeroDivisionError:
    print("A number cannot be divided with the 0!")

except ValueError:
    print("Both the values must be same to carry out the division process!")

