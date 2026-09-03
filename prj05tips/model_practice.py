import numpy as np
import seaborn as sns
from sklearn.model_selection  import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score, mean_absolute_error, r2_score

df = sns.load_dataset("tips")

X = df[["total_bill"]]
y = df["tip"]

X_train, X_test, y_train, y_test = train_test_split(
    X,y, test_size = 0.2, random_state = 42
)

m = LinearRegression()
m.fit(X_train, y_train)

y_prt = m.predict(X_test)
mae = mean_absolute_error(y_test, y_prt)
rmse = np.sqrt(mean_absolute_error(y_test, y_prt))
r2 = r2_score(y_test, y_prt)
print(mae)
print(rmse)
print(r2)