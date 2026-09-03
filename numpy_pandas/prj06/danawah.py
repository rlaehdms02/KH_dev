import numpy as np
from numpy.ma.core import argmax

# 상품명
items = np.array(["노트북", "마우스", "키보드", "모니터", "헤드셋", "웹캠"])

# 카테고리
categories = np.array(["전자기기", "소모품", "소모품", "전자기기", "소모품", "소모품"])

# 단가
prices = np.array([1200000, 30000, 80000, 350000, 60000, 50000])

# 6개 상품의 1월~4월 월별 판매량 (행: 상품, 열: 1~4월)
sales = np.array([[50, 60, 55, 70],  # 노트북
                  [200, 230, 210, 250],  # 마우스
                  [150, 180, 160, 190],  # 키보드
                  [80, 90, 85, 95],  # 모니터
                  [120, 110, 130, 140],  # 헤드셋
                  [90, 95, 100, 105]])  # 웹캠

# 1. 상품별 4달간 총 판매량
result01 = np.sum(sales, axis=1)
print(result01)
# 2. 소모품 카테고리에 속하는 상품들의 이름만 추출
result02 = categories == "소모품"
print(items[result02])
# 3. 월별 전체 상품의 평균 판매량
result03 = np.sum(sales, axis = 0) / len(result01)
print(result03.round(1))
# 4. 4달간의 총 매출액(판매량 × 단가)이 가장 높은 상품
result04 = np.max(np.sum(sales, axis = 1) * prices)
print(result04)

