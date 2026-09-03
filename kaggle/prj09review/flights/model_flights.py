import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split

plt.rcParams["font.family"] = "Malgun Gothic"
plt.rcParams["axes.unicode_minus"] = False

df = sns.load_dataset("flights")
df.to_csv("flights.csv")

#전처리
df["date"] = pd.to_datetime(
    df["year"].astype(str) +"-"+df["month"].astype(str),
    format="%Y-%b")
df_month_dummies = pd.get_dummies(df["month"], drop_first=True)

#result = pd.concat([df["passengers"], df_month_dummies], axis=1)
result['t'] = np.arange(len(df))

n_test = 12
X = result
y = df["passengers"]

X_train = X.iloc[:-n_test]
X_test = X.iloc[:-n_test]
y_train = y.iloc[-n_test:]
y_test = y.iloc[-n_test:]


m = LinearRegression()
m.fit(X_train,y_train)

y_pred = m.predict(X_test)
r2 = r2_score(y_test, y_pred)
print(r2)

#학습

#예측

#평가