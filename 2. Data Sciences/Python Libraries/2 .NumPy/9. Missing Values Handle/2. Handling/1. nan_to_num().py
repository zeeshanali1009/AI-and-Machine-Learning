import numpy as np 

this_array  = np.array([12,23,np.nan,56,np.nan, 576,7])
print(np.nan_to_num(this_array, nan= 100))          # nan_to_num(array,replacing value)
