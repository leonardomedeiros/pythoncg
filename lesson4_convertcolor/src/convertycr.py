import cv2
import numpy as np
image = cv2.imread('../img/babuino2.jpg')
cv2.imshow("Original", image) 

image_cy = cv2.cvtColor(image, cv2.COLOR_BGR2YCR_CB)
cv2.imshow("Converted Image in New Color SPACE YCR", image_cy) 

cv2.waitKey(0)
cv2.destroyAllWindows()