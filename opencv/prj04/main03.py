# mask=np.zeros((500,800),dtype="uint8")
# cv2.circle(mask,(400,250),250,255,-1)#동그라미
# cv2.rectangle(mask,(100,100),(700,400),255,-1)#네모 -1은 안쪽을 다 채워라
#
# result=cv2.bitwise_and(a,a,mask=mask)
# cv2.imshow("a",a)
# cv2.imshow("mask",mask)
# cv2.imshow("mask",result)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
import cv2
import numpy as np

#연습

img_bgr=cv2.imread("./image/31.jpg")
red=cv2.imread("./image/red.png")
img_bgr=cv2.resize(img_bgr,(800,500))
red=cv2.resize(red,(800,500))
h,w=img_bgr.shape[:2]

img_hsv=cv2.cvtColor(img_bgr,cv2.COLOR_BGR2HSV)

mask=mask1 = cv2.inRange(img_hsv, (92,41,0), (110,255,255))
mask_inv=cv2.bitwise_not(mask)
result=cv2.bitwise_and(img_hsv,img_hsv,mask=mask_inv)
result=cv2.cvtColor(result,cv2.COLOR_HSV2BGR)
red_hair=cv2.bitwise_and(red,red,mask=mask)

img_red_hair =cv2.bitwise_or(result,red_hair)
cv2.imshow("img_bgr",img_bgr)
cv2.imshow("red",red)
cv2.imshow("mask",mask)
cv2.imshow("result",result)
cv2.imshow("red_hair",red_hair)
cv2.imshow("img_red_hair",img_red_hair)

cv2.waitKey(0)
cv2.destroyAllWindows()