#지점별 매출 집계

import numpy as np
stores = np.array(["강남", "홍대", "잠실"])
# 4일 × 3지점 매출(만원)
sales = np.array([[120, 90, 100],
                  [130, 95, 110],
                  [100, 80,  90],
                  [140, 100, 120]])

# 1. 지점별 총매출 (열별 합계)
result01 = np.sum(sales, axis=0)
print(f"{result01}")
# 2. 일별 총매출 (행별 합계)
result02 = np.sum(sales, axis=1)
print(result02)
# 3. 전체 평균 매출
result03 = np.sum(sales, axis = 0) / len(result01)
print(f"{result03.round(1)}")
# 4. 매출이 가장 높은 지점 이름
result05 = np.argmax(result01)
print(f"{stores[result05]}")