import cv2

#====이미지 파일 다루기======
img=cv2.imread("images/sample.png",cv2.IMREAD_COLOR)

print(img)
print(img.shape)
cv2.imshow("zzz",img)
cv2.waitKey(3000)
cv2.destroyAllWindows()

cv2.imwrite("images/result.png",img)
# === 비디오 파일 다루기 ======
cap=cv2.VideoCapture("videos/0.mp4")
fps=cap.get(cv2.CAP_PROP_FPS)
w = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
h=cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

w =int(w)
h=int(h)
fourcc=cv2.VideoWriter_fourcc(*"mp4v")
out =cv2.VideoWriter("videos/result.mp4",fourcc,fps,(w,h))

delay =int(1000/fps)
while True:
    is_read,frame =cap.read()
    if not is_read: break
    out.write(frame)
    cv2.imshow("frame",frame)
    cv2.waitKey(delay)
    cap.release()
cv2.destroyAllWindows()
