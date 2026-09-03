import numpy as np

my_loc = np.array([0, 0])
target = np.array([3, 4])
cafes = np.array([
    [1, 1],
    [5, 5],
    [-1, 2]
])

# 1. 내 위치와 목적지 사이의 유클리드 거리 (norm 함수 사용)
result = np.linalg.norm(cafes - target)
print(result)
# 2. 유클리드 거리 공식을 직접 작성하여 구하기 (np.sqrt 등 사용)

# 3. 내 위치에서 각 카페들까지의 모든 거리 구하기

# 4. 가장 가까운 카페의 인덱스 번호 찾기