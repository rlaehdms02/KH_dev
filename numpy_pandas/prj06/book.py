import numpy as np

books = np.array(["파이썬 입문", "데이터 분석", "머신러닝", "알고리즘", "웹개발"])
rental = np.array([12, 25, 8, 30, 15])  # 누적 대출 횟수
stock = np.array([3, 0, 5, 1, 7])  # 현재 재고

# 1. 대출 횟수를 내림차순 정렬
result1 = np.sort(rental)
print(result1)
# 2. 대출 많은 순으로 책 제목 나열
result2 = np.argsort(rental)[::-1]
print(books[result2])
# 3. 재고가 0권인 책 이름
result3 = np.where(stock == 0)
print(books[result3])
# 4. 대출 횟수 상위 3권의 평균 대출 횟수
result4 = np.argsort(rental)[-1:1:-1]
print(books[result4])
# 5. 재고 5권 미만이면서 대출 횟수 20회 이상인 '인기 소진' 책 이름
result5 = np.where((stock < 5)  & (rental >= 20))
print(books[result5])