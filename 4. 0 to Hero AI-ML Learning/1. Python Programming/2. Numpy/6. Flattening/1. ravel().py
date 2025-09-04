# Conversion of multi dimesional array into the 1 d array 
# ravel()       view only  and affects the array
# flatten()       it generated the copy of the actual array 

import numpy as np

array_2d = np.array([[1, 2, 3], [4, 5, 6]])

# Using flatten (returns a copy)
flat_copy = array_2d.flatten()

# Using ravel (returns a view)
flat_view = array_2d.ravel()

print("Original 2D array:")
print(array_2d)

print("\nFlattened using flatten():")
print(flat_copy)

print("\nFlattened using ravel():")
print(flat_view)


flat_copy[0] = 99
flat_view[1] = 88

print("\nModified flat_copy (flatten):", flat_copy)
print("Modified flat_view (ravel):", flat_view)
print("Original array after changes:")
print(array_2d)
