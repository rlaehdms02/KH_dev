import numpy as np

scores = np.array([100,50,70,30])
x =(scores > 50) & (scores < 80)
print(x)
print(scores[x])



