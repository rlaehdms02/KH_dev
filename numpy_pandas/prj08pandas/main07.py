import pandas as pd

df = pd.read_csv("data/people.csv")
result = df.set_index("이름")
print(result.iloc[0])