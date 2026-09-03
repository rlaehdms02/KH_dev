import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

data = fetch_california_housing()
X = data.data
y = data.target

df = pd.DataFrame(X, columns=data.feature_names)
df["Target"] = y
df.to_csv("california_housing.csv")
print(df.shape)
print(df.describe())
print(df.isna().sum())

fig, axes = plt.subplots(1,1, figsize=(10,6))
sns.histplot(data=df["Target"], ax=axes, bins=50)
plt.show()
#
# 0.5757877060324508
# 0.5332001304956565
# 0.7455813830127764
housing = ["MedInc","HouseAge", "AveRooms", "AveBedrms","Latitude", "Longitude"]
X = df[housing]
y = df["Target"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

m = LinearRegression()

m.fit(X_train_scaled, y_train)
y_pred = m.predict(X_test_scaled)
print(y_pred)
sr2 = r2_score(y_test, y_pred)
print(sr2)
mae = mean_absolute_error(y_test, y_pred)
print(mae)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
print(rmse)