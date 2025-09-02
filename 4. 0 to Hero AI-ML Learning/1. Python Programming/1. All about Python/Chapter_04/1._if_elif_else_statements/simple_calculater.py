num_1 = float(input("Enter the first number: "))
num_2 = float(input("Enter the second number: "))

operation = input("Please enter the operation you want to perform on the variables (+, -, *, /): ")

if operation == "+":
    print(f"The sum of variables is {num_1 + num_2}")
elif operation == "-":
    print(f"The subtraction of variables is {num_1 - num_2}")
elif operation == "*":
    print(f"The multiplication of variables is {num_1 * num_2}")
elif operation == "/":
    if num_2 != 0:
        print(f"The division of variables is {num_1 / num_2}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation! Please enter one of +, -, *, /.")
