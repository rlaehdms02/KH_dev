import pandas as pd

df = pd.read_csv("data/people.csv")
df.to_csv("data/result.csv", index=False, encoding="utf-8-sig")

print(df)