import numpy as np
#Bool 인덱싱
m = np.linspace(1,5,5).astype(int)
mask = [False, True, True, True , False]
result = m > 3
print(result)
print(m.ndim)
print(m.size)
print(m.dtype)
print(m[(m > 1) & (m  < 5)])
