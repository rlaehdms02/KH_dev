import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split

plt.rcParams["font.family"] = "Malgun Gothic"
plt.rcParams["axes.unicode_minus"] = False

df = sns.load_dataset("tips")

#전처리
df["tip_pct"] = df["tip"] / df["total_bill"]*100
df["sex"] = df["sex"].map({"Female" : 0, "Male":1})
df["time"] = df["time"].map({"Dinner":0, "Lunch":1})
features = ["total_bill", "size", "tip_pct"]

X = df[features]
y = df["tip"]

X_train, X_test, y_train, y_test = train_test_split(
    X,y,test_size=0.2,random_state=42)

m = LinearRegression()
m.fit(X_train,y_train)
y_pred = m.predict(X_test)
print(y_pred)
x = r2_score(y_test,y_pred)
print(x)