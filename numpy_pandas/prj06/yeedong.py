import numpy as np

data = np.array([73, 290, 256, 170, 232, 115, 70, 242, 187, 138, 78, 111,
                 215, 281, 181, 288, 220, 220, 256, 172, 257, 47, 158, 213,
                 212, 204, 118, 68, 134, 157, 212, 152, 146, 185, 249, 173,
                 125, 189, 80, 197, 70, 212, 121, 70, 63, 127, 286, 292, 272, 51])

temps = np.random.choice(data, size=10, replace=False)  # 10개 랜덤 추출

print(temps)
# 1. 평균 크기
result1 = np.mean(temps)
print(result1)
# 2. 가장 큰 물고기와 작은 물고기
fish_max = np.max(temps)
fish_min = np.min(temps)
print(fish_max, fish_min)
# 3. 크기의 표준편차
result2 = np.std(temps)
print(result2.round(1))
# 4. 중앙값
result3 = np.median(temps)
print(result3)
# 5. 평균보다 큰 물고기는 몇 마리?
result4 = np.sum(temps > result1)
print(result4)