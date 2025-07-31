import numpy as np
''''
np.insert(array ,index,value, asix=None)
array - original array
index -
value -
asix -
asix = 0 is row -wise
asix =1 is col wise 

append =  add on end of array
insert = add at specific index

'''

arr =np.array([10,20,30,40,50,60])
print(arr)
new_arr=np.insert(arr, 2, 100, axis=0)
print(new_arr)

arr_2d = np.array([[1,2],[4,5]])
print(arr_2d)
#axis = None , 0 ,1
new_arr_2d = np.insert(arr_2d , 2 , [8,6] , axis=1)
print(new_arr_2d)