import numpy as np
"""
.concatenate((array1,array2),axis =0)
"""
arr1 =np.array([10,20,30])
arr2=np.array([1,2,3])
new_arr=np.concatenate((arr1 ,arr2))
print(new_arr)