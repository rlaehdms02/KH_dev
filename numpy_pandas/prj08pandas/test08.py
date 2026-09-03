import pandas as pd

df = pd.read_csv("data/people.csv")
df = df.set_index("이름")
print(df.loc[["가영","나은","다희"],["나이","도시"]])