import cv2
red=cv2.imread("./image/red.png")
img_mini=cv2.imread("./image/mini.jpg")
img_mini=cv2.resize(img_mini,(800,500))
red=cv2.resize(red,(800,500))
h,w=img_mini.shape[:2]

img_hsv=cv2.cvtColor(img_mini,cv2.COLOR_BGR2HSV)

mask=mask1=cv2.inRange(img_hsv, (0,97,0), (34,250,255))
mask_inv=cv2.bitwise_not(mask)
result=cv2.bitwise_and(img_mini,img_mini,mask=mask_inv)
result_hsv=cv2.cvtColor(result,cv2.COLOR_HSV2BGR)
red_clothes=cv2.bitwise_and(red,red,mask=mask)

img_red_clothes=cv2.bitwise_or(result,red_clothes)

cv2.imshow("red_clothes",img_red_clothes)
cv2.waitKey(0)
cv2.destroyAllWindows()