import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.model_selection import train_test_split

plt.rcParams["font.family"] = "Malgun Gothic"
plt.rcParams["axes.unicode_minus"] = False

#데이터
df = pd.read_csv("train.csv")
print(df)

#전처리(결측치, 중복제거, 인코딩, 파생변수)
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])
df["Fare"] = df["Fare"].fillna(df["Fare"].median())

df["Sex"] = df["Sex"].map({"male": 0, "female": 1})
df["Embarked"] = df["Embarked"].map({"S": 0, "C": 1, "Q": 2})

df["FamilySize"] = df["Parch"] + df["SibSp"] + 1

#모델 (학습, 예측, 평가)

features = ["Age","Embarked","FamilySize","Sex","Fare", "Pclass"]
X = df[features]
y = df["Survived"]


X_train, X_test, y_train, y_test = train_test_split(
    X,y, test_size = 0.2, random_state = 42, stratify = y
)

m = LogisticRegression(max_iter=10000)
m.fit(X_train, y_train)

y_pred = m.predict(X_test)

result = classification_report(y_test, y_pred, target_names=["사망","생존"])
print("Result",result)

acc_score = accuracy_score(y_test, y_pred)
print("acc_score",acc_score)
sr = pd.Series(m.coef_[0], index=features).sort_values(ascending=False)
print(sr)
# cm = confusion_matrix(y_test, y_pred)
# plt.figure(figsize = (8,6))
# sns.heatmap(cm, annot=True, cmap="Blues", xticklabels=["사망 예측"], yticklabels=["생존 예측"])
# plt.show()
# print(cm)