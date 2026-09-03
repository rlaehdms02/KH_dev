import seaborn as sns
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

plt.rcParams["font.family"] = "Malgun Gothic"
plt.rcParams["axes.unicode_minus"] = False
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
m = LogisticRegression(max_iter=5000)
m.fit(x_train, y_train)
#예측
y_pred = m.predict(x_test)
#결과
acc = accuracy_score(y_test, y_pred)
print(y_pred)
t = ["Gentoo", "Chinstrap", "Adelie"]
cm = confusion_matrix(y_test, y_pred, labels=t)
fig, axes = plt.subplots(figsize= (5,5))
sns.heatmap(cm, annot=True, ax=axes,fmt="d", xticklabels=t, yticklabels=t0)
plt.xlabel("예측")
plt.ylabel("실패")
plt.show()
result = classification_report(y_test, y_pred, target_names=t)
print(result)