import cv2
import numpy as np
image = cv2.imread('../img/babuino2.jpg')

# OpenCV's 'split' function splites the 
#image into each color index
B, G, R = cv2.split(image)

# Let's amplify the blue color
merged = cv2.merge([B+100, G, R])
cv2.imshow("Merged with Blue Amplified", merged) 

cv2.waitKey(0)
cv2.destroyAllWindows()