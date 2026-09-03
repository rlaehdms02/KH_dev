# 일주일 기온 통계

import numpy as np

temps = np.array([12, 15, 18, 14, 20, 22, 17])  # 월~일 기온(℃)

# 1. 평균 기온
result01 = np.sum(temps) / len(temps)
print(f"{result01:.1f}")
# 2. 가장 더운 날과 추운 날의 기온
result02 = np.min(temps)
result03 = np.max(temps)
print(result02, result03)
# 3. 기온의 표준편차
result04 = np.sum(temps) / len(temps)
print(f"{result04:.1f}")
# 4. 중앙값
result05 = np.median(temps)
print(f"{result05}")
# 5. 평균보다 더운 날은 몇번 있었나?
result06 = temps[temps > result01 ]
print(f"{len(result06)}")