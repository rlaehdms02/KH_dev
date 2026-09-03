import pandas as pd

df = pd.read_csv("data/employees.csv")

# Q2-1 `이름`과 `연봉` 두 열만 뽑아 출력하세요.
# result = df[["이름","연봉"]]
# print(result)

# Q2-2 연봉이 5000 이상인 직원만 고르고, 몇 명인지 세세요.
# result = len(df[df["연봉"] >= 5000])
# print(result)

# Q2-3 부서코드가 `D01`이면서 나이가 30 미만인 직원을 고르세요.
# result = df[(df["부서코드"] == 'D01') & (df["나이"] < 30)]
# print(result)

# Q2-4 연봉 상위 5명의 이름·연봉을 구하세요.
# result = df.sort_values(by="연봉", ascending=False).head(5)[['이름','연봉']]
# print(result)

# Q2-5 `iloc`로 6~10번째 행(위치 기준)을 조회하세요.
# result = df.iloc[5:10]
# print(result)

# Q2-6 연봉이 비어있는(NaN) 행만 골라 사번·이름·부서코드를 보세요.
# result = df[df["연봉"].isnull()][['사번','이름',"부서코드"]]
# print(result)