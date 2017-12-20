import cv2
import numpy as np
image = cv2.imread('../img/babuino2.jpg')

# OpenCV's 'split' function splites the image into each color index
B, G, R = cv2.split(image)

# Let's re-make the original image, 
merged = cv2.merge([B, G, R]) 
cv2.imshow("Merged", merged) 

cv2.waitKey(0)
cv2.destroyAllWindows()