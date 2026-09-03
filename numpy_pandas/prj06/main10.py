import numpy as np
names = np.array(["김철수", "이영희", "박민수", "최지우", "정해인"])
depts = np.array(["개발", "영업", "개발", "디자인", "영업"])
# 5명 × 3분기 실적
sales = np.array([[100, 120, 130],
                  [90, 95, 100],
                  [110, 105, 120],
                  [80, 85, 90],
                  [130, 140, 135]])

# 1. 직원별 연간 총실적s
result1 = np.sum(sales, axis=1)
print(result1)
# 2. 실적 1등 직원 이름
result2 = np.argmax(result1)
print(names[result2])
# 3. 분기별 평균 실적
result3 = np.mean(sales, axis=0)
print(result3)
# 4. 연간 총실적 300 이상인 우수 직원 이름
result4 = np.where(result1 >= 300)
print(names[result4])
# 5. (도전) 매 분기 상승한(3분기>2분기>1분기) 직원 이름
q1 = sales[:,0]
q2 = sales[:,1]
q3 = sales[:,2]
mask = (q2>q1) & (q3>q2)
result5 = names[mask]
print(result5)