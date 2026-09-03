import numpy as np

data = np.array([10, 20, 30, 40, 50])

# 1. min-max 정규화 → 0~1 범위로
result1 = (data - np.min(data)) / (np.max(data) - np.min(data))
print(result1)
# 2. z-score 표준화 → 평균0, 표준편차1
result2 = (data - np.mean(data)) / np.std(data)
print(np.mean(result2))
print(np.std(result2))
# 3. (도전) 아래 2D를 '열별'로 min-max 정규화
features = np.array([[1, 100],
                     [2, 200],
                     [3, 300]])
min_val = np.min(features, axis=0)
max_val = np.max(features, axis=0)
result3 = (features - min_val) / (max_val - min_val)
print(result3)