import pandas as pd
import numpy as np

a = np.array([10,20,30])
print(a[0])
b=  pd.Series([10,20,30], index=["수학", "영어", "국어"])
print(b["수학"])