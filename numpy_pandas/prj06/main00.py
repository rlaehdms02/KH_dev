import numpy as np

names = ["가희","나희","다희","라희","마희"]
scores = np.array([[85, 90, 100],   # 가희
                   [70, 60, 50],    # 나희
                   [95, 88, 92],    # 다희
                   [40, 55, 65],    # 라희
                   [100, 100, 80]]) # 마희
#학생별 총점
result01 = np.sum(scores, axis=1)
print(result01)
#과목별 평균
result02 = np.sum(scores, axis=0)
print(result02)
result03 = np.argmax(np.sum(scores, axis=1))
print(names[result03])
result04 = scores[scores < 60]
print(result04)