import pandas as pd

df = pd.read_csv("data/employees.csv")
orders = pd.read_csv("data/orders.csv")

#Q1-1 앞 5줄 출력
#print(df.head(5))

#Q1-2 행,열 크기 구하기
#print(df.shape)

#Q1-3 각 열의 자료형과 결측치 여부를 한번에 요약
#print(df.info())

#Q1-4 나이 연봉 두 숫자의 열의 통계 요약
#print(df[["나이","연봉"]].describe().astype(int))

#Q1-5 부서코드별 인원 수를 세세요
#print(df.groupby("부서코드").size())

#Q1-6 orders.csv의 카테고리별 개수를 세고, 표기가 이상한 값을 찾으세요
#print(orders.value_counts())