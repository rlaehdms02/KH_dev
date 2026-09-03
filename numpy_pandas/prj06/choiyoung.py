import numpy as np

branches = np.array(["강남점", "홍대점", "잠실점", "신촌점"])
menus = np.array(["아메리카노", "라떼", "콜드브루", "티", "에이드"])

# 4개 지점 x 5개 메뉴, 한 달 판매량
sales = np.array([
    [320, 210, 150, 80, 140],  # 강남점
    [280, 190, 260, 100, 175],  # 홍대점
    [410, 230, 180, 60, 120],  # 잠실점
    [150, 260, 200, 130, 300],  # 신촌점
])

# 1. 지점별 한 달 총 판매량.
result1 = np.sum(sales, axis=1)
print(result1)
# 2. 판매량 1위 지점 이름.
result2 = np.argmax(result1)
print(branches[result2])
# 3. 메뉴별 평균 판매량. (5개 메뉴 각각이 지점 평균 몇 잔씩 팔렸는지)
result3 = np.mean(sales, axis=0)
print(result3)
# 4. 200잔 이상 팔린 메뉴만 골라내기. (지점 메뉴 포함)
row_idx, col_idx = np.where(sales >= 200)
result4 = [f"{b} {m} ({s}잔)" for b, m, s in zip(branches[row_idx], menus[col_idx], sales[row_idx, col_idx])]
print(result4)
# 5. 각 지점에서 가장 많이 팔린 메뉴 이름. (지점 포함)
row= np.argmax(sales, axis=1)
result5 = [f"{b} {m}" for b, m in zip(branches, menus[row])]
print(result5)
