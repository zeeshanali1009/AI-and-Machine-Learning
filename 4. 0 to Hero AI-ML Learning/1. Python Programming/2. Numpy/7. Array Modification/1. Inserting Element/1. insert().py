# Insert() method is used to insert the elements at a specific position 
# it will return a new array after the modification
import numpy as np
this_array = np.array([])
# insert(array, index, value, axis) 
# ->none means data will be inserted into the flattened/row array
# ->0 means data will be inserted into the row array or 1d array  (by default)
# ->1 means data will be inserted into the columns array 2d array
np.insert(this_array, 0, [12,12,12,],axis=None)

