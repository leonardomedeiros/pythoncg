import cv2
import numpy as np

imgrectangle = cv2.imread('../img/rectangle.jpg')
imgcircle = cv2.imread('../img/circle.jpg')
imgtext = cv2.imread('../img/text.jpg')

image = imgcircle + imgrectangle - imgtext

cv2.imshow("Imagem", image)
cv2.imwrite('../img/operacaosubtracao.jpg', image)

cv2.waitKey(0)
cv2.destroyAllWindows()