# now we will be giving a sample that what we do in simple python logic when we do not use the Numpy library 
# Suppose we have to store the temperature of different cities so we will be doing it as:
temperature  = [12,23,45,56,67,23,2,46,34]
# now we are using the loop for the printing of this data 
total  = 0
for temp in temperature:
    total += temp

average  = total / len(temperature)
print("Average temperature is = ", average)

# now this same task can also be carried out in the more efficient and simple method as the process is as follow:

