import cv2
import numpy as np

square = np.zeros((300, 300), np.uint8)
cv2.rectangle(square, (50, 50), (250, 250), 255, -2)

ellipse = np.zeros((300, 300), np.uint8)
cv2.ellipse(ellipse, (150, 150), (150, 150), 30, 0, 180, 255, -1)

imageand = cv2.bitwise_and(square, ellipse)
cv2.imshow("AND", imageand)
cv2.imwrite('../img/bitwiseoperationand.jpg', imageand)
cv2.waitKey(0)

cv2.destroyAllWindows()