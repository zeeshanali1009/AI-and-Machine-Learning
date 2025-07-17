# Broadcasting can only be carried out by the following conditions
# Matching dimensions 
# Expanding Simple elements
# Incomapatible Shape 

import numpy as np
this_array = np.array([12,34,23,34,23,23,23,23,23])
result = this_array * 2 
print(result)
#  1d with 2d 
vector = np.array([12,34])
matrix = np.array([[12,34],[45,67,],[56,34]])
result  = matrix * vector

# Incomatibility
print(result)
vector = np.array([12,34,234,23,23,23,23])
matrix = np.array([[12,34],[45,67,],[56,34]])
result  = matrix * vector
print(result)



