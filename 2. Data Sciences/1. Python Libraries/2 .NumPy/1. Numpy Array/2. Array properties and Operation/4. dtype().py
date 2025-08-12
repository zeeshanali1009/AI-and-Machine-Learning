# dtype tells the nature of the data or the datatype used specially for the data validation

import numpy as np 

#  1d array
numpy_array  = np.array([12,23,45,67,23,56,23,56,23,56])
print(numpy_array.dtype)

# 2d array
numpy_array = np.array([[12,23,45,56],[12,34,45,56]])
print(numpy_array.dtype)

# multi dimensional array
numpy_array = np.array([[12,90,45,56],[12,34,45,56],[45,34,23,45],[23,34,34,23],[23,24,45,45]])
print(numpy_array.dtype)