import numpy as np

# 우주 탐사선 데이터 분석
missions = np.array([
    "화성탐사",
    "달탐사",
    "목성탐사",
    "금성탐사",
    "토성탐사"
])

# [속도, 연료효율, 탐사기간]
data = np.array([
    [90, 80, 300],
    [70, 95, 120],
    [150, 60, 500],
    [100, 75, 250],
    [130, 85, 450]
])

# 1. 탐사선별 총 점수 구하기
result1 = np.sum(data, axis=1)
print(result1)
# 2. 총 점수가 가장 높은 탐사선 이름
result2 = np.max(np.sum(data, axis=1))
print(result2)
# 3. 속도가 평균 이상인 탐사선 찾기
speed = data[:, 0]
result3 = np.mean(speed)
result4 = speed > result3
print(missions[result4])
# 4. 탐사기간이 300일 이상인 탐사선 개수
day = data[:, 2]
result5 = np.sum(day >= 300)
print(result5)
