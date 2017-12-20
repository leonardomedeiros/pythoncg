import cv2
import numpy as np

# load our input image
image = cv2.imread('../img/louvre.jpg')

# Let's double the size of our image
img_scaled = cv2.resize(image, None, fx=2, fy=2, interpolation = cv2.INTER_CUBIC)
cv2.imshow('Scaling - Cubic Interpolation', img_scaled)
cv2.imwrite('../img/imgscalecubic.jpg', img_scaled)
cv2.waitKey()

cv2.destroyAllWindows()