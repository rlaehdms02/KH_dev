import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

df = sns.load_dataset("penguins")
df = df.dropna().reset_index(drop=True)
df.to_pickle("data/penguins.csv")

#train test
features = ["bill_length_mm","bill_depth_mm","flipper_length_mm", "body_mass_g"]
x = df[features]
y = df["species"]

x_train, x_test, y_train, y_test = train_test_split(
    x,y,
    test_size=0.2,
    stratify=y,
    random_state=42
)
#학습
m = RandomForestClassifier(n_estimators=100, max_depth=3 ,random_state=3)
m.fit(x_train, y_train)
#예측
y_pred = m.predict(x_test)
print(y_pred)

