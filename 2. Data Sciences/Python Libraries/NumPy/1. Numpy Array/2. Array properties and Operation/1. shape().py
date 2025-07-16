# shape() method tells us about the shape of the array a it tells that how many rows and coloumns are there
# in the array gives the response in the form of (rows ,coloumns)

import numpy as np 

#  1d array
numpy_array  = np.array([12,23,45,67,23,56,23,56,23,56])
print(numpy_array.shape)

# 2d array
numpy_array = np.array([[12,23,45,56],[12,34,45,56]])
print(numpy_array.shape)