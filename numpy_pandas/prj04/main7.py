import numpy as np

a = np.arange(6)
m = np.array([
    [1,2,3],
    [4,5, 6],
    [3,5,1]
    ])
a = a.reshape(2,3)
m = np.min(m,axis=0)
print(m)
print(a)