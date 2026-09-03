import numpy as np

names = np.array(["철수", "유리", "강남", "지연", "현수", "은지", "민지"])
exam = np.array([
    [65, 91, 60, 55, 40, 75, 30],
    [40, 70, 73, 65, 90, 55, 100]
])

# 1. 과목별 최고 점수 학생, 과목별 최저 점수 학생
subjects1 = np.argmax(exam, axis=1)
subjects2 = np.argmin(exam, axis=1)
print(names[subjects1])
print(names[subjects2])
# 2. 과목중 하나라도 40점이면 과락 학생
result1 = (exam <= 40).any(axis=0)
result2 = np.where(result1, "과락", "합격")
print(names[result1])
# 3. 평균이 60이상이면서 과목중 하나라도 40미만이 아닌 학생
result3 = ((exam > 40).all(axis=0)) & ((np.mean(exam, axis=0)) >= 60)
print(names[result3])
# 4. 총 합격자 수
result4 = np.sum(result3)
print(result4)