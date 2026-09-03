import numpy as np

names = np.array(["김민수", "이서준", "박지훈", "최유진", "한도윤"])

sales = np.array([
    [120, 110, 130],
    [80, 90, 100],
    [140, 130, 120],
    [90, 95, 110],
    [100, 105, 115]
])

# 1. 모든 분기 매출이 전체 분기 평균보다 높은 직원 이름 출력
#    (mean, all, where)
result1 = np.mean(sales, axis=1) < np.mean(sales)
print(names[result1])

# 2. 총매출 상위 3명 중 평균매출이 가장 높은 직원 이름 출력
#    (sum, argsort, mean, argmax)
result2 = np.argmax(np.sum(sales, axis=1))
print(names[result2])

# 3. 분기별 매출 1위를 한 번도 하지 못한 직원 이름 출력
#    (argmax, isin, where)
result3 = np.argmax(sales, axis=0)
all_indices = np.arange(len(names))
never_winner = np.isin(all_indices, result3)
never_winner_idx = np.where(never_winner)[0]  # [1, 3, 4]
result3 = names[never_winner_idx]
print(result3)

# 4. 1분기 대비 3분기 매출 증가폭이 가장 큰 직원 이름 출력
#    (인덱싱, argmax)
q1 = sales[:, 0]
q3 = sales[:, 2]
result4 = np.argmax(q3 - q1)
print(names[result4])

# 5. 평균매출은 전체 평균 이상이지만,
#    어느 한 분기라도 해당 분기 평균보다 낮은 직원 이름 출력
#    (mean, any, logical_and 또는 &, where)

cond1 = np.mean(sales, axis=1) >= np.mean(sales)
quarter_mean = np.mean(sales, axis=0)
cond2 = (sales < quarter_mean).any(axis=1)
target_idx = np.where(np.logical_and(cond1, cond2))[0]
result5 = names[target_idx]
print(result5)