import numpy as np

fruits = np.array(["사과", "바나나", "포도", "딸기", "수박"])

# 5개 과일 × 3개 지표 [월간 판매량(개), 당도(10점 만점), 보유 품종 수]
data = np.array([
    [5000, 9.2, 12],
    [4800, 8.8, 10],
    [5200, 9.0, 15],
    [3100, 7.9, 8],
    [4100, 8.5, 9]
])

# 1. 월간 판매량(1열)의 총합
result1 = data[:, 0]
salary = np.sum(result1)
print(salary)
# 2. 당도(2열)가 가장 높은 과일의 이름
sugar = data[:, 1]
result2 = np.argsort(sugar)
sugar_max = np.argmax(sugar)
print(fruits[sugar_max])
# 3. 보유 품종 수(3열)가 10개 이상인 과일들의 이름
beer = data[:, 2]
beer_tenup = np.where(beer >= 10)
print(fruits[beer_tenup])
# 4. 월간 판매량이 4000개 이상인 과일의 수
m_sale = data[:, 0]
m_sale_top = np.sum(m_sale >= 4000)
print(m_sale_top)
# 5. 월간 판매량과 당도를 곱한 값이 가장 큰 과일의 이름
top = np.argmax(result1 * sugar)
print(fruits[top])