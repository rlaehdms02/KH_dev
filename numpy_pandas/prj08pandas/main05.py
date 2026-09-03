import pandas as pd

df = pd.read_csv("data/people.csv")
print(df.describe())
print(df.info())