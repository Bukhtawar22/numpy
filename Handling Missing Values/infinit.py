import numpy as np
#np.isinf() 10*100
#ye check krta hai k koi value kisi array m infinte toh nahi 

arr =np.array([1,2,np.inf , 4, -np.inf ,6])
print(np.isinf(arr))

