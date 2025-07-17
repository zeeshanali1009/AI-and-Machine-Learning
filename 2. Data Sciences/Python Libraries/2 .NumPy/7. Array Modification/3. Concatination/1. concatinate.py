# concatination of the arrays is carried out through the simple syntax
import numpy as np
this_array_1 = np.array([12,34,56,68,9,89])
this_array_2= np.array([12,34,56,68,9,89])
# axis  = 0  vertical stacking
# axis = 1   horizontal stacking 
vertical_stacking  = np.concatenate((this_array_1,this_array_2), axis = 0)
print(f"Vertical concatination or stacking is {vertical_stacking}")


this_array_1 = np.array([[12,34,56,68,9,89],[12,23,34,45,45,12],[12,34,45,56,23,34]])
this_array_2 = np.array([[12,34,56,68,9,89],[12,23,34,45,45,12],[12,34,45,56,23,34]])

horizontal_stacking = np.concatenate((this_array_1,this_array_2), axis = 1)
print(f"Horizontal concatination or stacking is {horizontal_stacking}")


