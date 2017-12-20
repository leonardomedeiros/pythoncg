import cv2
import numpy as np

img = cv2.imread('../img/louvre.jpg',0)
rows,cols = img.shape

M = cv2.getRotationMatrix2D((cols/2,rows/2),90,1)
rotatedImg = cv2.warpAffine(img,M,(cols,rows))

cv2.imshow('Rotacao em 90 graus',rotatedImg)
cv2.imwrite('../img/rotatedimg.jpg', rotatedImg)
cv2.waitKey(0)
cv2.destroyAllWindows()

