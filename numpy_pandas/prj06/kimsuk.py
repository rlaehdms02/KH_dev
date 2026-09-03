import numpy as np

apps = np.array(["유튜브", "인스타그램", "카카오톡", "네이버", "틱톡"])

# 5개 앱 × 3개 지표 [일평균 이용시간(분), 만족도(5점 만점), 배터리 소모율(%)]
data = np.array([
    [120, 4.5, 30],
    [85, 4.2, 20],
    [90, 4.8, 15],
    [60, 4.0, 10],
    [110, 3.8, 25]
])
# 1. 일평균 이용시간(1열)의 총합(분)
sum_data = data[:,0]
result1 = np.sum(sum_data, axis = 0)
print(result1)
# 2. 만족도(2열)가 가장 높은 앱의 이름
good_app = data[:,1]
result2 = np.argmax(good_app, axis = 0)
print(apps[result2])
# 3. 배터리 소모율(3열)이 20% 이상인 앱들의 이름
battery =  data[:,2]
result3 = battery >= 20
print(apps[result3])
# 4. 일평균 이용시간이 90분 이상인 앱의 개수
day_data = data[:, 0]
result4 = np.sum(day_data >= 90)
print(result4)
# 5. 이용시간과 만족도를 곱한 가중치가 가장 큰 앱의 이름
result5 = np.argmax((sum_data) * good_app )
print(apps[result5])