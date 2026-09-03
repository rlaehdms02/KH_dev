import pandas as pd

df = pd.read_csv("data/people.csv")

df["월급"] = df["연봉"] / 12

result = df.groupby("도시")["연봉"].agg(["max"])
result = df.groupby("도시").agg(
        연봉최대= ("연봉","max"),
        나이평균 = ("나이", "mean")
)
print(result)