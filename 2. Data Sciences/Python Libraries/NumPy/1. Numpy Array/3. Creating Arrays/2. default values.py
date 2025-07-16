# numoy array can be created with the default values as it may be into the different forms
# default values with zeroes using the zeros() method
import numpy as np
simple_array  = np.zeros(2)
print(f"Array with the default values fixed by the user as zeros {simple_array}")
print(simple_array)

# this same work of zeros can also be replaced by the ones as
simple_array  = np.zeros(2)
print(f"Array with the default values fixed by the user as ones {simple_array}")
print(simple_array)

simple_array  = np.full((2,3),7)
print(f"Array with the default values fixed by the user as {simple_array}")
