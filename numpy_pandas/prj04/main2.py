# axis 액시스
import numpy as np

x = np.arange(1,13)
print(x)
x = x.reshape((3,-1))
result = np.sum(x, axis=0)
print(result)