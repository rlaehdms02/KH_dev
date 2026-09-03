import pandas as pd

df = pd.read_csv("data/people.csv")

#결축지 처리
# df.dropna()
df["나이"] =df["나이"].fillna(df["나이"].mean())
df["도시"] = df["도시"].fillna("미상")
df["연봉"] = df["연봉"].fillna(df["연봉"].mean())

#중복 제거
df.drop_duplicates()

#결축지 확인
print(df.isna().sum())

print(df.head())