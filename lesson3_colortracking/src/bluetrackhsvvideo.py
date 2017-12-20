import cv2
import numpy as np

cap = cv2.VideoCapture('../video/videoazul.avi')
while(cap.grab()):
    _, frame = cap.retrieve()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    res = cv2.bitwise_and(frame,frame, mask= mask)
    cv2.imshow('res',res)

    # Press ESC to close windows
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows