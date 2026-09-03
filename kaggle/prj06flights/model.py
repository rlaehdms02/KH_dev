#flights
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

plt.rcParams["font.family"] = "Malgun Gothic"
plt.rcParams["axes.unicode_minus"] = False

#데이터
df = sns.load_dataset("flights")
x = df["year"].astype(str) + "-" + df["month"].astype(str)
df["date"] = pd.to_datetime(x, format="%Y-%b")
df = df.sort_values('date').reset_index(drop=True)

#t (time) 추세
df["t"] = np.array(len(df))

#m (month) 계절
month_dummies = pd.get_dummies(df["month"], drop_first=True)

#학습
X = pd.concat([df["t"], month_dummies], axis=1)
y = df["passengers"]

test_cnt = 12

X_train, X_test = X.iloc[0:-test_cnt], X.iloc[-test_cnt:]
y_train, y_test = y.iloc[0:-test_cnt], y.iloc[-test_cnt:]

##수치형 학습
m = LinearRegression()
m.fit(X_train, y_train)

#수치형 예측
y_pred = m.predict(X_test)

#오차확인
mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

print("MAE: ", mae)
print("MSE: ", rmse)
print("R2: ", r2)

x = np.mean(np.abs((y_test - y_pred) / y_test) * 100)
print("x: ", x)