import pandas as pd
from sklearn.datasets import load_iris
from sklearn.impute import SimpleImputer
import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler, OrdinalEncoder

#
# df = pd.DataFrame({
#    "age" : [20,30,np.nan,40,50],
#     "score" : [100,np.nan,80,70,np.nan]
# })
# #결측치 처리
# # imputer = SimpleImputer(strategy="median").set_output(transform="pandas")
# # result = imputer.fit_transform(df)
# #print(result)
#
# #스케일링
# X = np.array([[1.0, 100.0],
#               [2.0, 300.0],
#               [3.0, 500.0],
#               [4.0, 700.0]])
# scaler = StandardScaler()
# X_scaled = scaler.fit_transform(X)
# print(X_scaled)

#범주형 인코딩 (순위X)
# df = pd.DataFrame({"color": ["red", "green", "blue", "green"]})
# result = pd.get_dummies(df, columns=["color"], drop_first=True)
# print(result)

#범주형 인코딩 (순위O)
# df = pd.DataFrame({"size": ["소", "대", "중", "소"],
#                    "grade" : ["Bronze", "Gold", "Silver", "Bronze"]})
# enc = OrdinalEncoder(categories=[
#     ["소","중", "대"],
#     ["Bronze", "Gold", "Silver"]
# ])
# df[["size", "grade"]] = enc.fit_transform(df[["size", "grade"]])
# print(df)

#퍼생컬럼 ,중복제거, 시계할
X,y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
#전처리
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
#모델
m = KNeighborsClassifier(n_neighbors=3)
#파이프 라인(전처리 + 모델)
pipe = make_pipeline(scaler,m)

#학습, 예측, 평가
pipe.fit(X_train, y_train)
y_pred = pipe.predict(X_test)
print(y_pred)
accuracy_score = accuracy_score(y_test, y_pred)
print(accuracy_score)
