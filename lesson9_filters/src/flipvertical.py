import cv2
import numpy as np

image = cv2.imread('../img/louvre.jpg',0)

# Let's now to a vertical flip.
flipped = cv2.flip(image, 0)
cv2.imshow('Vertical Flip', flipped) 
cv2.imwrite('../img/verticalflip.jpg', flipped)
cv2.waitKey()
cv2.destroyAllWindows()