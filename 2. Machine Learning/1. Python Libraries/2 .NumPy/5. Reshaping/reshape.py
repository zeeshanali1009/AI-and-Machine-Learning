# Reshape changes the dimensions of the array without modifying data
# it does not create a copy rather than it returns a single view
# it will affect the array



import numpy as np

simple_array = np.array([12, 23, 23, 1, 3, 35, 23, 345, 23, 46])

reshaped_array = simple_array.reshape(5, 2)

print("Original 1D array:")
print(simple_array)

print("\nReshaped 2D array (5 rows, 2 columns):")
print(reshaped_array)
