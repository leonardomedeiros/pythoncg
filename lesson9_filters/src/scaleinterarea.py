import cv2
import numpy as np

# load our input image
image = cv2.imread('../img/louvre.jpg')

# Let's skew the re-sizing by setting exact dimensions
img_scaled = cv2.resize(image, (900, 400), interpolation = cv2.INTER_AREA)
cv2.imshow('Scaling - Skewed Size', img_scaled) 
cv2.imwrite('../img/imginterarea.jpg', img_scaled)
cv2.waitKey()

cv2.destroyAllWindows()