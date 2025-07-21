import numpy as np
'''
converting float into int
'''

arr= np.array([1.2,5.6,88.2,44.5])
print(arr.dtype) 
int_arr=arr.astype(int)

print(int_arr)  # Output: [1 5 88 44]
print(int_arr.dtype)  # Output: [1.2 5.6 88.2
# rows adn