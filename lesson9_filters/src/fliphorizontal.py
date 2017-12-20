import cv2
import numpy as np

image = cv2.imread('../img/louvre.jpg',0)

# Let's now to a horizontal flip.
flipped = cv2.flip(image, 1)
cv2.imshow('Horizontal Flip', flipped) 
cv2.imwrite('../img/horizontalflip.jpg', flipped)
cv2.waitKey()
cv2.destroyAllWindows()