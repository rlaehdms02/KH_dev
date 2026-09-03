#지도학습 -회귀(선형,다항,규제)
import numpy as np
from sklearn.linear_model import LinearRegression
#y=3x+2
X= np.linspace(1,100,100)
y= X *3 + 2
X=X.reshape(-1,1)
m= LinearRegression()
m.fit(X,y)

print("m.coef_",m.coef_)
print("m.intercept_",m.intercept_)