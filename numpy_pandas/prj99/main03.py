import numpy as np
'''
reshape
flatten'''
x=np.arange(0,12,1)
x=x.reshape(-1,4)
x=x.flatten('K')
print(x)
print(x.shape)
print(x.ndim)
