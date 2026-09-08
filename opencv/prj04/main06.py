#이진화 ,,임계처리
import cv2
# 전역 임계처리=============
# import cv2
# img=cv2.imread("./image/21.jpg",cv2.IMREAD_GRAYSCALE)
# img_resized=cv2.resize(img,(300,300))
#
# # a,b=cv2.threshold(img_resized,127,250,cv2.THRESH_BINARY_INV)#INV 반전
# a,b=cv2.threshold(img_resized,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)#INV 반전
# #기준을 a=127로 했고 작으면 0 ㅁ보다 많으면 255로 처리
# print(a)
#
#
# cv2.imshow("img",img_resized)
# cv2.imshow("b",b)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#적응형 임계처리========
import cv2
img=cv2.imread("./image/21.jpg",cv2.IMREAD_GRAYSCALE)
img_resized=cv2.resize(img,(300,300))

result=cv2.adaptiveThreshold(
    img_resized,
    255,
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    cv2.THRESH_BINARY,
    11,
    0,
)#이미지,계산방식,처리방식,주변영역크기,상수
cv2.imshow("result",result)
cv2.waitKey(0)
cv2.destroyAllWindows()