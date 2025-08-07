# loops are the iterators that iterates the certain block of code continuously until or unless the condition is completed.
# like there are the following types of loops
#  for loop
# while loop
# do while loop 


# while loop practice
x = -1
while not (1 <= x <= 100):
    x = int(input("Enter the value between the range 1-100: "))
print(f"The number is valid with value: {x}")



# this same task can be performed using the for loop as well because in while loop we have no limit unless the condition is met 
# but in for loop we have the limit in the form of range function

for i in range(10):
    x = int(input("Enter the number between the range 1-100: "))
    if 1 <= x <= 100:
        print(f"The number is valid with value: {x}")
        break
    else:
        print("Invalid input. Try again.")
