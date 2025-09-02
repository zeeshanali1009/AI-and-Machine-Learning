# This program takes the starting and ending points from the user and also the skipping part and prints the
# result

start = int(input("Enter the starting point: "))
end = int(input("Enter the ending point: "))

skip = int(input("Enter the skip point: "))


for i in range(start, end):
    if (i==skip):
        continue
    else:
        print (i)