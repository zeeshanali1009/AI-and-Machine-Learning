# positional arguments means that the arguments are being placed in the same pattern as the parameters are 
# being placed 

def Division_numbers(num_1, num_2):
    number = num_1  /num_2
    return number


first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))

result = Division_numbers(first_number,second_number)
print(f"The division of the two numbers is : {result}")