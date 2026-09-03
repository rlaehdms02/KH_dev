import pandas as pd
from sklearn.ensemble import RandomForestClassifier

#data
train = pd.read_csv('data/train.csv')
test = pd.read_csv('data/test.csv')

#잔처리
HomePlanet_mapping = {"Mars": 1, "Earth": 2, "Europa": 3}
Destination_mapping = {"TRAPPIST-1e": 1, "PSO J318.5-22": 2, "55 Cancri e": 3}

for df in [train, test]:
    df["Age"] = df["Age"].fillna(df.groupby("Cabin")["Age"].transform("median"))
    df["Age"] = df["Age"].fillna(df["Age"].median())
    df["VIP"] = (df["VIP"].fillna(False)).astype(int)
    df["CryoSleep"] = (df["CryoSleep"].fillna(False)).astype(int)
    df["HomePlanet"] = df["HomePlanet"].map(HomePlanet_mapping).fillna(0)
    df["Destination"] = df["Destination"].map(Destination_mapping).fillna(0)
#특성 고르기
#"Cabin",
features = ["VIP", "Age", "CryoSleep", "HomePlanet", "Destination"]
x = train[features]
y = train["Transported"]

#학습
m = RandomForestClassifier(n_estimators=100, random_state=42, max_depth=10)
m.fit(x, y)

#예측
result = m.predict(test[features])
test["Transported"] = result.astype(bool)
#model
#test["Survived"] = (test["Sex"] == "female").astype(int)

#결과물 저장
test[["PassengerId", "Transported"]].to_csv('data/result123.csv', index=False)

