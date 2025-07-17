# Splitting can be defines as the dividing of an array into the multiple sub-parts
import numpy as np

# 1D array
this_array = np.array([12, 23, 12, 23, 23, 3, 4, 90])
result = np.split(this_array, 2)  # Split into 2 equal parts
print(f"Split 1D array with np.split(): {result}")

# hsplit() only works on 2D arrays (splits columns), so we must reshape first
this_array_2d = this_array.reshape(2, 4)  # Now shape is (2, 4)
result_h = np.hsplit(this_array_2d, 2)
print(f"Horizontal split (hsplit) on 2D array: {result_h}")

# 2D array (correctly defined)
this_array_2d = np.array([[12, 23, 12], [34, 345, 45], [23, 24, 45]])

# Correct vertical split: splits rows (axis=0)
result_v = np.vsplit(this_array_2d, 3)  # 3 rows → 3 parts
print(f"Vertical split (vsplit) on 2D array: {result_v}")
