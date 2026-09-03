import numpy as np
# 1=별로 2=보통 3=좋음
answers = np.array([1, 3, 2, 1, 1, 2, 3, 3, 3, 2])

# 1. 등장한 고유 응답값
unq , counts = np.unique(answers, return_counts=True)
print(unq)
# 2. 각 응답이 몇 번 나왔는지
print(counts)
# 3. 가장 많이 나온 응답
cont_max = unq[np.argmax(counts)]
print(cont_max)
# 4. (도전) 응답별 비율(%)
per = (counts / len(answers)) * 100
print(per)