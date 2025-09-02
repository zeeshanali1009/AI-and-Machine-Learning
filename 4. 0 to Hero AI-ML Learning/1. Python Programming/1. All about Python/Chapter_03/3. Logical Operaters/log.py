# Logical Operater are being used in the conditions there are three types of logical operaters
# 1. AND Operater   (All conditions must be TRUE to get the TRUE result )
# 2. OR Operater    (Any of the conditions must be TRUE to get the result TRUE)
# 3. NOT Operater   (Reverses the result)

name = "Zeeshan"
age = 20
University = "Superior University Lahore"

if (name == "Zeeshan" and age > 18):
    print(f"The student {name} is eligible to have the Identity Card!")

if(age > 18 or University == "Superior University Lahore"):
    print(f"The Student is currently doing the graduation!")

if (not(name =="Ubaid")):
    print(f"The name of the student is {name}")




