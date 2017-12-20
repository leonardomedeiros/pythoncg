import cv2
import numpy as np

image = cv2.imread('../img/babuino2.jpg')
grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imwrite('../img/babuino2gray.jpg', grayImage)
cv2.imshow('Imagem Cinza', grayImage)
cv2.waitKey()
cv2.destroyAllWindows()