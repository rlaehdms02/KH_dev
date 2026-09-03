#지도학습
#분류/학습

#====로지스틱 회귀===
# import numpy as np
from sklearn.datasets import load_breast_cancer, load_iris,load_wine
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC

# # X,y=load_breast_cancer(return_X_y=True)
# X,y = load_iris(return_X_y=True)
# X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
#
# scaler=StandardScaler()
# scaler.fit(X_train)
# X_train_s=scaler.transform(X_train)
# X_test_s=scaler.transform(X_test)
# m=LogisticRegression(max_iter=500)
# m.fit(X_train_s,y_train)
# y_pred=m.predict(X_test_s)
#
# acc_score =accuracy_score(y_test,y_pred)
# print("acc_score:",acc_score)
#
# proba = m.predict_proba(X_test_s)
# print("proba:",np.round(proba,3))
# print("proba:",type(proba))



#   ====KNN=====
#k는 홀수로 하는게 좋다

##거리에  비해
# X,y =load_wine (return_X_y=True)
#
# X_train,X_test,y_train,y_test=train_test_split(X,y,
#                                                test_size=0.2,random_state=42)
# scaler = StandardScaler()
# scaler.fit(X_train)
# X_train_s = scaler.transform(X_train)
# X_test_s = scaler.transform(X_test)
#
# m=KNeighborsClassifier(n_neighbors=5)
# m.fit(X_train_s,y_train)
# y_pred = m.predict(X_test_s)
#
# acc_score = accuracy_score(y_test,y_pred)
# print(acc_score)

#=====SVM===
# X,y = load_wine(return_X_y=True)
# X_train,X_test,y_train,y_test=train_test_split(X,y,
#                                                test_size=0.2,random_state=42)
# scaler = StandardScaler()
# scaler.fit(X_train)
# X_train_s = scaler.transform(X_train)
# X_test_s = scaler.transform(X_test)
#
# m=SVC()#차원을 살짝 올려서 공간 휘어지게 만들어서 다시 돌리는 rdf
# m.fit(X_train_s,y_train)
# y_pred = m.predict(X_test_s)
# acc_score = accuracy_score(y_test,y_pred)
# print(acc_score)


#모델별 성능 비교
# X,y =load_iris(return_X_y=True)
X,y =load_breast_cancer(return_X_y=True)
X_train, X_test, y_train, y_test = (train_test_split
                                    (X, y, test_size = 0.2, random_state = 42))

models= {
    "로지스틱":make_pipeline(StandardScaler(),LogisticRegression(max_iter=1000)),
    "KNN":make_pipeline(StandardScaler(),KNeighborsClassifier(n_neighbors=5)),
    "SVM":make_pipeline(StandardScaler(),SVC())
}
for modelname ,model_pipeline in models.items():
    model_pipeline.fit(X_train, y_train)
    y_pred = model_pipeline.predict(X_test)
    acc_score = accuracy_score(y_test,y_pred)
    print(modelname+" acc_score:",acc_score)