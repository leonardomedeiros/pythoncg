# coding=cp1252
import cv2
import numpy as np

image = np.zeros((512,512,3), np.uint8)

cv2.putText(image, 'Alo IFAL', (75,290), cv2.FONT_HERSHEY_COMPLEX, 2, (100,170,0), 3)
cv2.imshow("Alo IFAL Titulo", image)
cv2.imwrite('../img/text.jpg', image)
cv2.waitKey(0)
cv2.destroyAllWindows()









