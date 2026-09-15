#이미지 특징 추출
import numpy as np
from matplotlib import pyplot as plt
from pandas.plotting import hist_frame
import cv2

img=np.zeros((256,256,3),dtype=np.uint8)
img[:,:]=(100,255,30)

hist_b =cv2.calcHist([img],[0],None,[256],[0,256])
hist_g =cv2.calcHist([img],[1],None,[256],[0,256])
hist_r =cv2.calcHist([img],[2],None,[256],[0,256])

# print(hist_b)
# print(hist_g)
# print(hist_r)

X=np.concatenate([hist_b,hist_g,hist_r])
print(X.shape)
print(X)