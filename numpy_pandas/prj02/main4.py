import numpy as np

x= np.linspace(1, 24,24)
x = x.reshape(2, 3,2,2)
print(x)
print(x.shape)