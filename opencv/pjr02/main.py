import cv2
import numpy as np

pixel = [100,100,100]
row = []
col = []
matrix = np.full((300,300,3), (100,100,255),dtype=np.uint8)
#matrix[100:200,100:200] = (0,0,0)
#cv2.circle(matrix,(100,200),50,(100,100,100),5)

img = cv2.imread("imange/test2.jpg")
img = cv2.resize(img,(500,500))
img2 = cv2.circle(img,(350,270),40,(0,255,0),5)
img3 = cv2.circle(img,(350,270),30,(255,0,0),5)
img4 = cv2.circle(img,(350,270),35,(0,0,255),5)
img5 = cv2.circle(img,(350,70),140,(0,0,255),5)
img6 = cv2.circle(img,(207,258),85,(255,0,0),5)
img7 = cv2.circle(img,(174,37),80,(255,0,0),5)
cv2.imwrite("test123.jpg",img)
# cv2.imwrite("imange/result.png",matrix)
cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

