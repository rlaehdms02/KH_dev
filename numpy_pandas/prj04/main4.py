import numpy as np

m = np.arange(12)
#m = m.reshape(3,4)



print(m)
print(m.shape)
m2 = m[ :, np.newaxis]
print(m2)
print(m2.shape)