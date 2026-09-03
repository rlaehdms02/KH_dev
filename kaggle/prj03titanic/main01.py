import pandas as pd
import seaborn as sns
from sklearn.ensemble import RandomForestRegressor
import matplotlib.pyplot as plt
plt.rcParams["font.family"] = "Malgun Gothic"
plt.rcParams["axes.unicode_minus"] = False

# data
x = "penguins"
df = sns.load_dataset(x)

# 전처리
# species           종
# island            섬
# bill_length_mm    부리길이
# bill_depth_mm     부리깊이
# flipper_length_mm 지느러미 길이
# body_mass_g       체중
# sex               성별
#종 Gentoo, Chinstrap,Adelie
#섬 Torgersen, Biscoe, Dream
#성별 Female, Male, Nan

df = df.dropna().reset_index(drop=True)
pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)
df["sex_num"] = df["sex"].map({"Male": 1, "Female": 0, "Dream":2})
df["species"] = df["species"].map({"Gentoo": 0, "Chinstrap": 1, "Adelie":2})
df["island"] = df["island"].map({"Torgersen":0, "Biscoe":1,"Dream":2})

for dfs in [df]:
    dfs["bill_length_mm"] = dfs["bill_length_mm"].fillna(dfs["bill_length_mm"].median())
    dfs["bill_depth_mm"] = dfs["bill_depth_mm"].fillna(dfs["bill_depth_mm"].median())
    dfs["flipper_length_mm"] = dfs["flipper_length_mm"].fillna(dfs["flipper_length_mm"].median())
    dfs["body_mass_g"] = dfs["body_mass_g"].fillna(dfs["body_mass_g"].median())
    df["sex_num"] = df["sex_num"].fillna(df["sex_num"].median())
    df["species"] = df["species"].fillna(df["species"].median())
    df["island"] = df["island"].fillna(df["island"].median())

# 특성 고르기
features = ["bill_length_mm", "bill_depth_mm", "flipper_length_mm", "sex_num"]
x_train = df[features]
y_train = df["body_mass_g"]

# 학습
m = RandomForestRegressor(n_estimators=100, random_state=42, max_depth=10)
m.fit(x_train, y_train)

# 예측
test = df.copy()
result = m.predict(test[features])
test["pred_body_mass_g"] = result



#저장
test[["sex", "pred_body_mass_g"]].to_csv('data/result123.csv', index=False)