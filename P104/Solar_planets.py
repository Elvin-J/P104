import cv2
import numpy as np

img = cv2.imread("solarsystem.jpg")

cv2.putText(img,
            "Sun",
            (20,300),
            cv2.FONT_HERSHEY_COMPLEX,
            fontFace=cv2.FONT_HERSHEY_SCRIPT_COMPLEX,
            fontScale = 1,
            color=(0,0,255))
cv2.imshow("Display Image", img)
print(img)
cv2.waitKey(5000)