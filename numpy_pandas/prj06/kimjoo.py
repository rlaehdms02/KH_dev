import numpy as np

member = np.array(["김감자", "이호박", "박키위", "최사과", "양양파"])
# 배열 왼쪽부터 "김감자", "이호박", "박키위", "최사과", "양양파" 1은 출석 0은 결석
atten_reco = np.array([
    [1, 1, 1, 1, 1],  # 월요일
    [0, 0, 1, 1, 1],  # 화요일
    [1, 0, 1, 0, 1],  # 수요일
    [0, 0, 1, 0, 1],  # 목요일
    [1, 0, 1, 1, 1],  # 금요일
    [1, 0, 1, 0, 0],  # 토요일
    [1, 1, 1, 1, 0]  # 일요일
])

# 1. 인물별 출석 횟수를 출력
result1 = np.sum(atten_reco, axis=1)
print(result1)
# 2. 평일과 주말에 각각 출석률이 가장 낮은 사람(memeber)을 출력
day = atten_reco[:5,:]
day2 = atten_reco[5:,:]
result2 = np.sum(day, axis=0)
result3 = np.sum(day2, axis=0)
result4 = np.argmin(result2)
result5 = np.argmin(result3)
print(member[result4])
print(member[result5])
# 3. 가장 많이 출석한 사람과 낮은 사람의 출석률(%)을 출력
result6 = np.sum(atten_reco, axis=0)
result7 = np.argmax(result6)
result8 = np.argmin(result6)
print(f"{member[result7]}, {result6[result7]/7*100:.0f}")
print(f"{member[result8]}, {result6[result8]/7*100:.0f}")


# 4. 평균 출석률보다 낮은 사람 목록하고 출석률이 가장 높은 사람 이름을 출력