# delete() method is used to delete the particular element from the specific position
import numpy as np
this_array = np.array([12,23,45,678,9,8,45234,56,678,89,678])
modified = np.delete(this_array, 0, axis = None)        # delete(array,index,axis=none/0/1)    none --> flattened      0--> means rows     1--> means columns
print(f"Array before the deletion {this_array}")
print(f"Array after the deletion {modified}")