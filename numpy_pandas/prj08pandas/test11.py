import pandas as pd

df = pd.read_csv("data/people.csv")


df["나이"] =  df["나이"].fillna(30)
df["나이"] =  df["나이"].astype(int)

print(df.info())