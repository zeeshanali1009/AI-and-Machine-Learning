# now we will be giving a sample that what we do in simple python logic when we do not use the Numpy library 
# Suppose we have to store the temperature of different cities so we will be doing it as:
temperature  = [12,23,45,56,67,23,2,46,34]
# now we are using the loop for the printing of this data 
total  = 0
for temp in temperature:
    total += temp

average  = total / len(temperature)
print(f"Average calculated through the simple python logic as {average}")

# now this same task can also be carried out in the more efficient and simple method as the process is as follow:
import numpy as np
Temperatures  = np.array([12, 34 ,56, 7 ,23 ,34, 12, 34, 12 ,34, 12, 12, 3, 4 ,4])
Average  = np.mean(Temperatures)
print(f"Average calculated through the Numpy library as {Average}")

