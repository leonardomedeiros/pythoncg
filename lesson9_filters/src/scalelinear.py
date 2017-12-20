import cv2
import numpy as np

# load our input image
image = cv2.imread('../img/louvre.jpg')

# Let's make our image 3/4 of it's original size
image_scaled = cv2.resize(image, None, fx=0.75, fy=0.75)
cv2.imshow('Scaling - Linear Interpolation', image_scaled) 
cv2.imwrite('../img/imglinear.jpg', image_scaled)
cv2.waitKey()

cv2.destroyAllWindows()