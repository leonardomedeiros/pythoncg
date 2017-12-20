import cv2
import numpy as np

square = np.zeros((300, 300), np.uint8)
cv2.rectangle(square, (50, 50), (250, 250), 255, -2)

ellipse = np.zeros((300, 300), np.uint8)
cv2.ellipse(ellipse, (150, 150), (150, 150), 30, 0, 180, 255, -1)

imageor = cv2.bitwise_or(square, ellipse)
cv2.imshow("OR", imageor)
cv2.imwrite('../img/bitwiseoperationor.jpg', imageor)
cv2.waitKey(0)

cv2.destroyAllWindows()