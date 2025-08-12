# append() method adds element into the array in the end
# original array will remain unchaged while a new sample will be created
import numpy as np
this_array = np.array([12,3,4,57,78,890,90,546,34,57])
np.append(this_array,[34,23,45,23,45,45,2])
print(this_array)