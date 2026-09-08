#그리기 ,주석
import numpy as np
import cv2
img=cv2.imread("./image/rgb.png")
# cv2.line(이미지,시작,끝,색,두께)

# cv2.line(img,(0,0),(100,100),(255,255,255),10)

# #사각형 cv2.rectangle(이미지,좌측상단,우측하단,색상,두께)
# cv2.rectangle(img,(0,0),(100,100),(0,0,0),10)

# #원 cv2.circle(이미지,중심정,반지름,색상,두께)
# cv2.circle(img,(100,100),100,255,5)

#다각형:cv2.polyline(이미지,점들,닫힘여부,색상,두께)
pts=np.array([[10,10],
              [200,50],
              [400,300],
              [50,150],
              [50,70],

              ]
             )
pts.reshape(-1,1,2)
# cv2.polylines(img,[pts],isClosed=True,color=(255,255,255),thickness=10)
# cv2.fillPoly(img,[pts],color=(255,255,255))



#텍스트 :cv2.putText(이미지,텍스트,위치,폰트,크기,색,굵기)
cv2.putText(img,"텍스트",(100,100),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)

cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()