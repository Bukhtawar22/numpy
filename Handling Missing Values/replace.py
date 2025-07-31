import numpy as np
#kisi array mein infinte values hai pata lg gya 
#isinf sy ab os ko replce kese kare


arr =np.array([1,2,np.inf , 4, -np.inf ,6])
print(np.isinf(arr))

clean_arr = np.nan_to_num(arr , posinf=1000, neginf=-1000)
#posint ->positive infinte
#neginf->negtive infinet
print(clean_arr)