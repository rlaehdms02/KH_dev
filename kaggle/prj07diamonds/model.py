import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

df = sns.load_dataset('diamonds')

df = df[(df["x"] > 0) & (df["y"] > 0) & (df["z"] > 0)].reset_index(drop=True)

cut_order = ['Fair', 'Good', 'Very Good', 'Premium', 'Ideal']
color_order = ['J', 'I', 'H', 'G', 'F', 'E', 'D']
clar_order = ['I1', 'SI2', 'SI1', 'VS2', 'VS1', 'VVS2', 'VVS1', 'IF']

df["cut_o"] = df["cut"].map({v: i for i, v in enumerate(cut_order)})
df["color_o"] = df["color"].map({v: i for i, v in enumerate(color_order)})
df["clar_o"] = df["clarity"].map({v: i for i, v in enumerate(clar_order)})

features = ["carat", "cut_o", "color_o", "clar_o"]
X = df[features]
y = df["price"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

m = RandomForestRegressor(random_state=42, n_estimators=100)
m.fit(X_train, y_train)

y_pred = m.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2s = r2_score(y_test, y_pred)

print(f"MAE: {mae:.4f}")
print(f"RMSE: {rmse:.4f}")
print(f"R2 Score: {r2s:.4f}")
# sr = pd.Series(m.coef_, index=features)
# print(sr)