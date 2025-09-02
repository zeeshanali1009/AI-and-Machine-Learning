# membership used to check whether the certain character exists or not exists
# 1 ----  in       return true if exists
# 2-----  not in    returns false if exists or negates the result

this_list = [1,3,4,5,"Zeeshan", "Raza",True]
user_input = int(input("Enter the chracter you want to check: "))

if (user_input in this_list):
    print("Found!")
else:
    print("Not found!")


if (user_input not in this_list):
    print("Not Found!")
else:
    print("Found!")
    