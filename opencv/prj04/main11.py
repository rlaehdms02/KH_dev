#이미지 피라미드, 템플릿 매칭

import cv2
img=cv2.imread("image/59.png")
template =cv2.imread("image/60.png")
img=cv2.resize(img,(600,600))

h=template.shape[0]
w=template.shape[1]
img_up =cv2.pyrUp(img)
img_down =cv2.pyrDown(img)

#템플릿 매칭
result=cv2.matchTemplate(img,template,cv2.TM_CCOEFF_NORMED)
min_val,max_val,min_loc,max_loc=cv2.minMaxLoc(result)

top_left=max_loc
# 튜플 형태로 명확하게 묶어줍니다.
bot_right=(top_left[0]+w, top_left[1]+h)

# [에러 수정]
# 1. top_left[0], top_left[1] 대신 튜플인 top_left와 bot_right를 전달합니다.
# 2. 매칭 기준이 된 img에 사각형을 그립니다.
cv2.rectangle(img, top_left, bot_right, (255,0,0), 2)

cv2.imshow("img",img)
cv2.imshow("img_up",img_up)
cv2.imshow("img_down",img_down)
cv2.waitKey(0)
cv2.destroyAllWindows()