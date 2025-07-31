#np.isnan(array)
import numpy as np


arr =np.array([1,2,np.nan , 4, np.nan ,6])
print(np.isnan(arr))  # [1. 2. nan 4. nan 6.]

# can not directly compare np.nan == np.nan
