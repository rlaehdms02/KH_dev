#트리 ,앙상블
from sklearn import metrics
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.metrics import accuracy_score
# #==결정트리===
# iris = load_iris()
# X,y = iris.data, iris.target
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)
#
# m=DecisionTreeClassifier(max_depth=3,random_state=42)
# m.fit(X_train,y_train)
# y_pred = m.predict(X_train)
# acc_score = accuracy_score(y_train,y_pred)
# print("acc_score",acc_score)
#
# result =export_text(m,feature_names=iris.feature_names)
# print("aaa:",m.get_depth())
# print(result)

#=== 앙상블 :랜덤 포레스트
iris =load_iris()
X,y = iris.data, iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)

m=RandomForestClassifier(n_estimators = 100, random_state = 42)
m.fit(X_train, y_train)
y_pred = m.predict(X_test)


result= metrics.classification_report(y_test, y_pred)
print(result)