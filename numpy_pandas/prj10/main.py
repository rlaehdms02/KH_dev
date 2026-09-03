import pandas as pd

df = pd.read_csv('data/emp.csv')
#전 직원 평균 급여
#result = df["급여"].mean()

#부서별 평균 급여
#result = df.groupby("부서")["급여"].mean()

#부서별 인원 수
#result = df.groupby("부서").size()

#부서별 여러 통계 한번에 최소값 최대값 평균
#result = df.groupby("부서")["급여"].agg(["max","min","mean0"])

#컬럼으로 묶기(부서 + 직급)
#result = df.groupby(["부서","직급"]).max()

#컬럼마다 다른 집계 // 급여 평균, 나이 최대, 평가점수 최소
#result = df.groupby("부서").agg({"나이" : "max", "급여" : "mean", "평가점수" : "min"})

#map
# def f01(x):
#     if pd.isna(x): return None
#     if x >= 90:
#         return "A"
#     elif x >= 80:
#         return "B"
#     elif x >= 70:
#         return "C"
#     else:
#         return "D"
# df["평가점수등급"] = df["평가점수"].map(f01)

def calc_score(r):
    return r["근속연수"] * r["평가점수"]

df["종합점수"] = df.apply(lambda r : r["근속연수"] * r["평가점수"], axis= 1)
print(df)

