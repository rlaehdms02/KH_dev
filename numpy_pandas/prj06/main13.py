import numpy as np
price = np.array([100, 105, 103, 110, 108, 115])

# 1. 전일 대비 변동액 (diff)
result1 = np.diff(price)
print(result1)
# 2. 가장 많이 오른 날의 변동액
result2 = np.max(np.diff(price))
print(result2)
# 3. 오른 날의 수 (변동 > 0)
result3 = np.sum(np.diff(price) > 0)
print(result3)
# 4. (도전) 전일 대비 변동률(%) — 소수 첫째자리
result4 = (np.diff(price)) / price[:-1] * 100
print(result4.round(1))
