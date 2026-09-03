import numpy as np

# 카페 5개 지점의 3개월(6,7,8월) 음료 판매량
branches = np.array(["강남점", "홍대점", "신촌점", "잠실점", "건대점"])
sales = np.array([[320, 350, 410],
                  [280, 260, 300],
                  [150, 200, 180],
                  [400, 420, 460],
                  [220, 210, 195]])

# 1. 지점별 3개월 총 판매량
result1 = np.sum(sales, axis=1)
print(result1)
# 2. 판매량이 가장 많은 지점 이름
result2 = np.argmax(result1)
print(branches[result2])
# 3. 월별(6/7/8월) 평균 판매량
result3 = np.mean(sales, axis=0)
print(result3)
# 4. 총 판매량이 900개 이상인 지점 이름
result4 = np.sum(sales, axis=1) > 900
print(branches[result4])
# 5. 매달 판매량이 계속 증가한 지점 이름
increasing = (sales[:,0 ] < sales[:,1]) & (sales[:,1] < sales[:,2])
result5 = branches[increasing]
print(result5)