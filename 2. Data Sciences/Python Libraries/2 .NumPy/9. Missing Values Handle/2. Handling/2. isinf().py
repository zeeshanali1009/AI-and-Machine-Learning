import numpy as np 

this_array  = np.array([12,23,np.inf,np.nan, 56,np.inf, 576,np.nan, 7])
cleaned = np.nan_to_num(this_array, posinf=1000, neginf=2000)
print(cleaned)
