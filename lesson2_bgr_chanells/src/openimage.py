import cv2
import numpy as np

image = cv2.imread('../img/babuino.jpg')
cv2.imshow('Figura', image)
cv2.waitKey()
cv2.destroyAllWindows()