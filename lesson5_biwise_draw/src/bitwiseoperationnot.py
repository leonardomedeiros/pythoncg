import cv2
import numpy as np

square = np.zeros((300, 300), np.uint8)
cv2.rectangle(square, (50, 50), (250, 250), 255, -2)

ellipse = np.zeros((300, 300), np.uint8)
cv2.ellipse(ellipse, (150, 150), (150, 150), 30, 0, 180, 255, -1)

imagenot = cv2.bitwise_not(square, ellipse)
cv2.imshow("NOT", imagenot)
cv2.imwrite('../img/bitwiseoperationnot.jpg', imagenot)
cv2.waitKey(0)

cv2.destroyAllWindows()