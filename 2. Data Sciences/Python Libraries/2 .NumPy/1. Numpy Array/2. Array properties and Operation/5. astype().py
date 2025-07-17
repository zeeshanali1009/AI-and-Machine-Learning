# astype is used for the conversion from one datatype to another datatype

import numpy as np 

# 1D array
numpy_array = np.array([12, 23, 45, 67, 23, 56, 23, 56, 23, 56])
converted_array = numpy_array.astype(float)
print("1D array dtype after conversion:", converted_array.dtype)

# 2D array
numpy_array = np.array([[12, 23, 45, 56], [12, 34, 45, 56]])
converted_array = numpy_array.astype(float)
print("2D array dtype after conversion:", converted_array.dtype)

# Multi-dimensional array 
numpy_array = np.array([
    [12, 90, 45, 56],
    [12, 34, 45, 56],
    [45, 34, 23, 45],
    [23, 34, 34, 23],
    [23, 24, 45, 45]
])
converted_array = numpy_array.astype(float)
print("Multi-dimensional array dtype after conversion:", converted_array.dtype)
