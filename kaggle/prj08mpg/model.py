import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split

df = sns.load_dataset("mpg")
df["horsepower"] = df["horsepower"].fillna(df["horsepower"].mode()[0])
num_cols = ["cylinders", "displacement", "horsepower", "weight", "model_year"]
result = pd.get_dummies(df["origin"], drop_first=True)
X = pd.concat([df[num_cols], result], axis=1)
y = df["mpg"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
m = LinearRegression()
m.fit(X_train, y_train)
y_pred = m.predict(X_test)
print("예측값:", y_pred[:5])
mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_absolute_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)
print("MAE:", mae)
print("RMSE:", rmse)
print("R2:", r2)
temp = pd.Series(m.coef_, index = X.columns)
print(temp)


select * from (select name from user where id = 'test') as t where name = '강도'