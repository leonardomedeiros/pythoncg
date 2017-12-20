import cv2
import numpy as np
image = cv2.imread('../img/babuino2.jpg')

# OpenCV's 'split' function splites the image 
#into each color index
B, G, R = cv2.split(image)

cv2.imshow("Original", image)
cv2.imshow("Red", R)
cv2.imshow("Green", G)
cv2.imshow("Blue", B)
cv2.waitKey(0)
cv2.destroyAllWindows()
