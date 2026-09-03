import pandas as pd
from pandas.core.dtypes import astype

df = pd.read_csv('data/emp.csv')

result = df.pivot_table(index="부서", columns="직급", values="급여", aggfunc="mean")
result = result.fillna(0).astype(int)
result = result.agg()
print(result)