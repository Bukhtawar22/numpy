import numpy as np
''''
np.insert(array ,index,value, asix=None)
array - original array
index -
value -
asix -
asix = 0 is row -wise
asix =1 is col wise 



'''
arr =np.array([10,20,30,40,50,60])
print(arr)
new_arr=np.insert(arr,2,100,axis=0)
print(new_arr)