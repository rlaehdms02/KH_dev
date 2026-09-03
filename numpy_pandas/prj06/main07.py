import numpy as np

products = np.array(["사과", "바나나", "포도", "딸기", "수박"])
price = np.array([3000, 1500, 8000, 6000, 12000])
stock = np.array([50, 120, 20, 35, 8])

# 1. 5000원 이상인 상품 이름
result1 = price >= 5000
print(products[result1])
# 2. 재고 30개 미만인 상품 이름
result2 = stock < 30
print(stock[result2])
# 3. 5000원 이상 상품들의 평균 가격
result3 = np.mean(price[np.where(price >= 5000)])
print(result3.round(1))
# 4. (도전) 5000원 이상 '그리고' 재고 30개 미만인 상품
result4 = np.where((price >= 5000) & (stock < 30) )
print(products[result4])