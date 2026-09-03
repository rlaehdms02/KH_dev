import numpy as np

# 1분 동안 측정한 세트별 줄넘기 횟수 (회)
rope_jumps = np.array([120, 450, 110, 130, 850, 140, 125, 95])

# 1. 평균 줄넘기 횟수와 중앙값
result1 = np.mean(rope_jumps)
result2 = np.median(rope_jumps)
print(result1, result2)
# 2. 가장 많이 뛴 횟수(최댓값)와 가장 적게 뛴 횟수(최솟값)
max_jump = np.max(rope_jumps)
min_jump = np.min(rope_jumps)
print(max_jump, min_jump)
# 3. 줄넘기 횟수의 표준편차
result3 = np.std(rope_jumps)
print(result3.round(1))
# 4. 목표 기준치인 200회를 초과한 세트 수
result4 = np.sum(rope_jumps >= 200)
print(result4)