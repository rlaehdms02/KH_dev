import numpy as np

raw = np.array([95, 120, -10, 80, 105, 60])

# 1. 0~100 범위로 잘라내기 (0미만→0, 100초과→100)
result2 = np.clip(raw,0, 100)
print(result2)
# 2. 보정 후 평균
result1 = np.mean(result2)
print(result1)
# 3. (도전) 보정된 값이 원래와 다른 항목 수
result3 = np.sum(raw != result2)
print(result3)
