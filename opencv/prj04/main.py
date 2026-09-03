import cv2
import numpy as np
# img=cv2.imread("./image/45.png",cv2.IMREAD_GRAYSCALE)#./상대 경로 /절대 경로   # 흑백으로
img=cv2.imread("image/45.png",)
# print(img.shape)
# roi2=img[0:100,0:100]=0#검정색은 0 흰색은 255
# cv2.imshow("img",img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# # print(img.shape)이미지 크기
# roi =img[0:100,0:100,:]#행에서 0~100 열에서 0~100 색상은 다
# roi[0:100,0:100]=[0,255,0]#특정 부분 색상 변경
#
# cv2.imshow("img",img)#화면을 보여준다
# cv2.waitKey(0)
# cv2.destroyAllWindows()


#이미지 잘라내기
# roi = img[570:900,490:820]#이미지 잘라내고
# img[0:330,0:330] =roi#이미지 그 위치에 붙이기 #득정위치 잘라내기?
# cv2.imshow("roi",roi)
# cv2.imshow("img",img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#기하학 변환 (이미지 크기 변환)
img=cv2.resize(img,(500,500))#크기조절
# img =cv2.resize(img,(800,500),fx=0.5,fy=0.5)#None자리에 500 500 이 들어간다면 괄호가 먼저 절대값이기 때문에
# #충돌 하더라도 먼저 되기 때문에 fx 는 무시하는 느낌이다.
# img=cv2.flip(img,1)#뒤집기
# #이동 : wrpAffine +이동행렬
# x = 100#x축을  100이동
# y= 100#
# M = np.float32([[1,0,x],[0,1,y]])
# img= cv2.warpAffine(img,M,(800,500))#이동 행렬



#회전

# img=cv2.rotate(img,cv2.ROTATE_180_COUNTERCLOCKWISE)#반 시계 방향
# img=cv2.rotate(img,cv2.ROTATE_180)#180도

#회전: 자유롭게
w=img.shape[0]
h=img.shape[1]
c= (w//2 ,h//2)
M= cv2.getRotationMatrix2D(c,30,1)
img=cv2.warpAffine(img,M,(w,h))
#사진 보여주기
cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#보간법 inter_linear