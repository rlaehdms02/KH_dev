import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import sklearn.metrics as skm
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split

plt.rcParams["font.family"] = "Malgun Gothic"
plt.rcParams["axes.unicode_minus"] = False

df = sns.load_dataset("diamonds")

#전처리
df = df[(df["x"] > 0) & (df["y"] > 0) & (df["z"] > 0)]

#인코딩

X = df[['carat']]
y = df['price']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size = 0.2, random_state = 42
)

m = LinearRegression()

print(X_train.shape)
print(y_train.shape)
print(X_test.shape)
print(y_test.shape)

m.fit(X_train, y_train)

y_pred = m.predict(X_test)
print()

sr2 = r2_score(y_test, y_pred)
print(sr2)