import pandas as pd
from numpy.ma.extras import column_stack

df = pd.read_csv("data/people.csv")

df.drop(columns=["나이"])

df["월급"] = df["연봉"] / 12
df["도시"] = df["도시"].replace("서울", "한양")
df["연봉"] = df["연봉"].replace(df["연봉"].mean() < "연봉","평균이상")
df = df.rename(columns={"월금":"급여","도시":"지역"})


print(df)