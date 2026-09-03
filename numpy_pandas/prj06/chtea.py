import numpy as np

# 열 = [주문ID, 주문금액, 수량, 할인금액]
orders = np.array([
    [1, 45000, 3, 5000],
    [2, 18000, 1, 0],
    [3, 72000, 4, 10000],
    [4, 55000, 2, 3000],
    [5, 27000, 3, 2000],
    [6, 81000, 5, 12000]
])

# 1. 총 매출(주문금액 합)
result1 = np.sum(orders[:,1])
print(result1)
# 2. 할인 후 실제 결제금액의 총합
result2 = (orders[:,1] - (orders[:,3]))
print(result2)
# 3. 주문금액이 5만원 이상인 주문ID
result3 = (orders[:,1] >= 50000)
menu_id = orders[:,0]
print(menu_id[result3])
# 4. 단가(주문금액 / 수량)가 가장 높은 주문ID
result4 = np.argmax(orders[:,1] / orders[:,2])
print(menu_id[result4])
# 5. 할인율(할인금액 / 주문금액)이 가장 높은 주문ID
result5 = np.argmax(orders[:,1] - orders[:,3])
print(menu_id[result5])
# 6. 실제 결제금액이 평균보다 큰 주문ID
result6 = (orders[:,1] > np.mean(orders[:,1]))
print(menu_id[result6])