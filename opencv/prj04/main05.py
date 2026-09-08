#밝기, 대비
import cv2
import numpy as np
from pyparsing import alphas
from matplotlib import pyplot as plt
# img=cv2.imread("image/45.png")
# img_gray=cv2.imread("image/45.png",cv2.IMREAD_GRAYSCALE)
#
# img_resized=cv2.resize(img,None,fx=0.5,fy=0.5)
# img_gray_resized=cv2.resize(img_gray,None,fx=0.5,fy=0.5)
#
#
# result=cv2.convertScaleAbs(img_resized,alpha=1,beta=-50)
# img_gray_resized_eq=cv2.equalizeHist(img_gray_resized)
#
# hist=cv2.calcHist([img_gray_resized_eq],[0],None,[256],[0,256])
#
#
#
# cv2.imshow("img_resize",img_resized)
# cv2.imshow("img_gray_resized",img_gray_resized)
# cv2.imshow("img_gray_resized_eq",img_gray_resized_eq)
# cv2.imshow("result",result)
# cv2.waitKey(0)
# cv2.destroyAllWindows()



##################################

#컬러 이미지 밝기 조절
# img = cv2.imread("./image/45.png")
# img_ycrcb=cv2.cvtColor(img,cv2.COLOR_BGR2YCrCb)
# img_ycrcb[:,:,0] =cv2.equalizeHist(img_ycrcb[:,:,0])
# result =cv2.cvtColor(img_ycrcb,cv2.COLOR_YCrCb2BGR)
# cv2.imshow("img_ycrcb",result)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


#####################################################
#CLAME
gray=np.random.randint(90,160,(300,300),dtype="uint8")
gray[:,0:150]=gray[:,0:150]*0.5
clahe =cv2.createCLAHE(clipLimit=2,tileGridSize=(8,8))
result=clahe.apply(gray)
cv2.imshow("gray",gray)
cv2.imshow("result",result)
cv2.waitKey(0)
cv2.destroyAllWindows()