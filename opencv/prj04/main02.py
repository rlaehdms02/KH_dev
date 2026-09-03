#산술 ,논리 ,마스킹
import cv2
import numpy as np
#이미지 준비
#산술=====
# a = np.uint8([[250]])
# b= np.uint8([[10]])
# result= cv2.add(a,b)#overflow 방지 최댓값을 넘어가지 안도록
#
# # cv2.imshow("a",a)
# # cv2.imshow("b",b)
#
# print(a)
# print(b)
# print(result)#256=>0 257=>1 260=>4
# cv2.waitKey(0)
# cv2.destroyAllWindows()


#===블렌딩 ===
#이미지 겹치기 블렌딩 하기
# a=cv2.imread("image/19.jpg",)
# b=cv2.imread("image/20.jpg",)
# a=cv2.resize(a,(800,500))
# b=cv2.resize(b,(500,500))
#
# result=cv2.addWeighted(a,0.7,b,0.9,0)#사진1 사진 가중치 1 사진2 사진 가중치 2 ,전체 밝기 보정값
#
# cv2.imshow("result",result)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#===비트연산====
# a=cv2.imread("image/19.jpg",cv2.IMREAD_GRAYSCALE)
# b=cv2.imread("image/20.jpg",cv2.IMREAD_GRAYSCALE)
# a=cv2.resize(a,(800,500))
# b=cv2.resize(b,(500,500))
# #비트 연산자
# result_and =cv2.bitwise_and(a,b)
#
# cv2.imshow("and",result_and)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#마스킹 마스크: 값이 0또는 255인 흑백 이미지
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



#  색 마스크
img_bgr =cv2.imread("image/31.jpg")
img_bgr=cv2.resize(img_bgr,(600,600))
img_hsv=cv2.cvtColor(img_bgr,cv2.COLOR_BGR2HSV)#HSV는 RGB보다 찾기 쉽다.
lower = np.array([91,37,79])
upper = np.array([108,144,208])
mask =cv2.inRange(img_hsv,lower,upper)
mask_inv =cv2.bitwise_not(mask)
result=cv2.bitwise_and(img_bgr,img_bgr,mask=mask)


cv2.imshow("result",result)
cv2.imshow("mask",mask)
cv2.imshow("img_hsv",img_hsv)

cv2.waitKey(0)
cv2.destroyAllWindows()


