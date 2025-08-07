# operaters are used to perform the specific operations on the data which are as follow:
#1. Arithmetic operaters 
#2. Assignment Opertaters
#3. Unary Operaters
#4. Relational Operaters
#5. Logical Operaters 

# here we will discuss them using the examples 
# arithmetic operaters 
a = 12
b = 13
print(f"Addition of a and b is: {a+b}")
print(f"Subtraction of a and b is: {a-b}")
print(f"Division of a and b is: {a/b}")
print(f"Modulous of a and b is: {a%b}")
print(f"Multiplication of a and b is: {a*b}")

# assignment operaters
a = 23
b = 0
a = a + 2
a += 2

# unary operaters
a = 12
a = -a

# relational operaters
a = 12
b = 89
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)
print(a == b)
print(a != b)

# logical operaters 
a = 76
b = 78
c = 56
print(a > b and a > c)
print(a > b or a > c)
print(not (a > b or a > c))
