# combining the multiple arrays into a single one array 
import numpy as np
Firstarray = np.array([12,23,12,23,23,3,4])
Secondarray = np.array([12,23,12,23,23,3,4])
verticalstack = np.vstack(((Firstarray,Secondarray)))
print(f"After the vertical stacking {verticalstack}")


Firstarray = np.array([12,23,12,23,23,3,4])
Secondarray = np.array([12,23,12,23,23,3,4])
horizontalstack = np.hstack(((Firstarray,Secondarray)))
print(f"After the horizontal stacking {horizontalstack}")