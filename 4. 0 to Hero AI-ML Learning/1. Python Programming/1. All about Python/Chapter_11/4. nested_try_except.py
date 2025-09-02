try:
    a= int(input("Enter the number!"))
    b= int(input("Enter the number!"))
    try:
        result = a/b 
        print(f"Result is {result}")
    except ZeroDivisionError:
        print("The number cannot be divided with the 0!")
except ValueError:
    print("Values must be same for the division!")