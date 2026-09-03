import numpy as np
category = np.array( ["한식", "양식", "중식", "일식"])
meal =np.array( ["점심", "저녁", "야식"])
food = np.array( [
    ["김치찌개", "제육볶음", "육개장"],
    ["피자", "햄버거", "파스타"],
    ["짜장면", "마라탕", "깐쇼새우"],
    ["초밥", "텐동", "라멘"]
])
price = np.array( [
    [6000, 8000, 10000],
    [12000, 5000, 9000],
    [7000, 8000, 13000],
    [10500, 11000, 8000]
])

# 모든 음식의 평균 가격
result1 = np.mean(price)
print(result1.round(1))
# 점심,저녁, 야식 별 총 가격(열)
result2 = np.sum(price, axis=0)
print(result2)
# 카테고리 별 평균 가격(행)
result3 = np.mean(price, axis=1)
print(result3.round(1))
# 가장 비싼 음식, 가장 저렴한 음식
rows, cols = np.where(price == np.max(price))
row, col = rows[0], cols[0]
print(food[row][col])
# 카테고리 별 음식 오름차순으로 정렬해서 출력
sort_idx = np.argsort(price, axis=1)

sorted_food = np.take_along_axis(food, sort_idx, axis=1)
sorted_price = np.take_along_axis(price, sort_idx, axis=1)

for c, f_list, p_list in zip(category, sorted_food, sorted_price):
    items = [f"{f}({p}원)" for f, p in zip(f_list, p_list)]
    print(f"{c}: {', '.join(items)}")
