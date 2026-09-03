import  cv2
import numpy as np


img = cv2.imread("./images/45.png")

print(img.shape)

cv2.imshow("imgshow", img[400:900,90:550])
cv2.waitKey(0)

