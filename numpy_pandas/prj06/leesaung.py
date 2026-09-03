import numpy as np

icecream = np.array([
    [95, 90, 88],  # 민트초코
    [90, 85, 92],  # 바닐라
    [85, 80, 89],  # 딸기
    [88, 95, 84],  # 초당옥수수
    [70, 60, 75]  # 마라
])

menu = np.array([
    "민트초코",
    "바닐라",
    "딸기",
    "초당옥수수",
    "마라"
])

evaluation = np.array([
    "맛", "향", "식감",
])

# 문제 1: 각 아이스크림의 총점을 구하세요.(힌트 : axis=1, np.sum())
result1 = np.sum(icecream, axis = 1)
print(result1)
# 문제 2: 각 아이스크림의 평균 점수를 구하세요. (힌트 : axis=1, np.mean())
result2 = np.mean(icecream, axis = 1)
print(result2.round(1))
# 문제 3: 각 평가 항목(맛, 향, 식감)의 평균 점수를 구하세요. (힌트 : axis=0)
result3 = np.mean(icecream, axis = 0)
print(result3.round(1))
# 문제 4: 평균 점수가 85점 이상인 아이스크림 이름만 출력하세요. (힌트 : 불리언 인덱싱)
result4 = result2 >= 85
print(menu[result4])
# 문제 5: 다음을 구하세요.
## 가장 높은 점수 (np.max)
result5 = np.max(icecream, axis = 1)
print(result5)
## 가장 낮은 점수 (np.min)
result6 = np.min(icecream, axis = 1)
print(result6)
## 전체 점수의 표준편차 (np.std)
result7 = np.std(icecream, axis = 1)
print(result7.round(1))
## 전체 점수의 중앙값 (np.median)
result8 = np.median(icecream, axis = 1)
print(result8)
# 보너스 문제 (조금 어려움)-평균 점수가 가장 높은 아이스크림이 무엇인지 출력하세요.
## 힌트) avg = np.mean(icecream, axis=1)
top = np.argmax(np.mean(icecream, axis = 1))
print(menu[top])