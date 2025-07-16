# Selecting a single element from the array is calles indexing
# Fancy Indexing
# selecting multiple item from the array at once is called fancy indexing 
# very useful in non-sequential data
# select in the form of list
# creates a copy and gives the output

# Left to right indexing (positive indexng)  Straight order
# right to left indexing (negative indexng)  Reverse order
import numpy as np
simple_array  = np.array([12,23,23,1,3,35,23,345,23,46,23,56,23])

# printing simple array
print(simple_array[2])

# slicing into the action
print(simple_array[0:5:2])

# it will start from 0 index and will finish at the end too 
print(simple_array[::2])

# it will print the array in the reverse order
print(simple_array[::-1])


