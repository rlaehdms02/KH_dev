import numpy as np
import numpy as np

a = [
    [1,2],
    [3,4]
]
b = [
    [5,6],
    [7,8]
]
a = np.array(a)
b = np.array(b)
x = np.array([100,65,50,60,80,85,30])
# result = np.min(x)
# result = np.max(x)
# result = np.sum(x)
# result = np.mean(x)
# result = np.median(x)
#result = np.std(x)

#집계 ,axis

#정렬
#result = np.sort(x)
#result = np.argsort(x)
#result = np.argmax(x)

#result = np.where(x >= 60, "합격", "불합격")
# g = np.random.default_rng(42)
# result = g.normal(0,10,size=3)
# result = a @ b
# result = np.linalg.inv(a)
# print(a @ result)


np.save("data.npy", x)
result = np.load("data.npy")
print(result)