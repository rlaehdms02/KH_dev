import numpy as np

rng = np.random.default_rng(seed=42)
# 1. 주사위(1~6)를 100번 굴린 배열 만들기
result01 = rng.integers(low=1, high=7, size=100)
print(result01)
# 2. 각 눈(1~6)이 몇 번씩 나왔는지 세기
counts = np.bincount(result01)[1:]
for face, count in enumerate(counts, start=1):
    print(f"눈 {face}: {count}회")
# 3. 나온 값들의 평균
result03 = np.sum(result01) / len(result01)
print(result03)
# 4. (도전) 6이 나온 횟수
result04 = np.sum(np.where(result01 == 6, 1 , 0))
print(result04)