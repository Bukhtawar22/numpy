import numpy as np
#np.nan_to_num(array ,nan=value) default 0
#missing value handel

arr =np.array([1,2,np.nan , 4, np.nan ,6])
clean_arr = np.nan_to_num(arr , nan=100)
print(clean_arr) 
