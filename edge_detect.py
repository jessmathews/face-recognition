import numpy as np
import cv2

cam = cv2.VideoCapture(0)

while True:
    ret,img = cam.read()
    img = cv2.flip(img,1)
    # gray = img
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 30, 100)
    cv2.imshow("edges", edges)
    cv2.imshow("gray", gray)
    if cv2.waitKey(1) == ord("q"):
        break

cam.release()
cv2.destroyAllWindows()
