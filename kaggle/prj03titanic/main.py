import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

import kagglehub

# Download latest version
path = kagglehub.competition_download('spaceship-titanic')

print("Path to competition files:", path)

#df 준비 : 파일 읽어오기
train = pd.read_csv('data/train.csv')
test = pd.read_csv('data/test.csv')

#df 전처리 : 결측치, 중복, 인코딩
for df in [train, test]:
    df.dropna(inplace=True)
    df["Sex"] = (df["Sex"] == "female").astype(int)

#df 에서 특징 고르기
x = train[["Pclass"]]
y = train["Survived"]

#학습
m = RandomForestClassifier(n_estimators=100, random_state=42, max_depth=1)
m.fit(x, y)

result = m.predict(test[["Pclass"]])
test["Survived"] = result


#예측