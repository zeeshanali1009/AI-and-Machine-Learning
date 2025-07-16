# Numpy Array is special type of python list that have multiple features 

# Numpy Array is a special type of Python list that has multiple features 

import numpy as np

# 1D array 
array_1d = np.array([12, 23, 456, 67, 56, 45, 34, 46, 657, 34, 56, 34])
print(f"1 dimensional array is: \n{array_1d}\n")

# 2D array
array_2d = np.array([[12, 23, 456], [34, 23, 56], [45, 23, 12]])
print(f"2 dimensional array is: \n{array_2d}\n")

# Multi dimensional array for example we are using 4D array as the multi dimensional array
array_4d = np.array([
    [12, 23, 456, 67],
    [12, 45, 67, 23],
    [23, 56, 678, 789],
    [234, 56, 68, 78]
])
print(f"4 dimensional array is: \n{array_4d}")


