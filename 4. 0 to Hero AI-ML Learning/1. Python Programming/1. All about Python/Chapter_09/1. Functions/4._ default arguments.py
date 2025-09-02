# default arguments are being used at the function definition process which is then actually used in the place
# or the scenario if the arguments are not passed

def Sum_of_numbers(num_1 =12, num_2=12):
    number = num_1  + num_2
    return number


# first_number = int(input("Enter the first number: "))
# second_number = int(input("Enter the second number: "))

result = Sum_of_numbers()
print(f"The division of the two numbers is : {result}")