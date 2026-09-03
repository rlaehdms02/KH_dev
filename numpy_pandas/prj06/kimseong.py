import numpy as np

temps = np.array([12, 15, 18, 14, 20, 22, 17])  # 월~일 기온(℃)

# --------------------------------------------------
# [문제] 아래 조건에 맞는 코드를 작성해보세요.
# --------------------------------------------------

# 1. 일주일간의 평균 기온 구하기 (np.mean)
result1 = np.mean(temps)
print(result1.round(1))
# 2. 가장 더운 날과 가장 추운 날의 기온을 튜플 형태로 한 번에 출력하기 (np.max, np.min)
temps_max = np.max(temps)
temps_min = np.min(temps)
print(temps_max, temps_min)
# 3. 기온의 표준편차를 구하고 소수점 둘째 자리까지 출력하기 (np.std)
result2 = np.std(temps)
print(result2.round(2))
# 4. 기온의 중앙값(Median) 구하기 (np.median)
result3 = np.median(temps)
print(result3)
# 5. (도전) 일주일 중 '평균 기온보다 더 따뜻했던 날'은 총 며칠이었는지 구하기 (np.sum 활용)
result4 = np.sum(temps > result1)
print(result4)