import cv2
import numpy as np

image = cv2.imread('../img/babuino2.jpg')
grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Imagem Cinza', grayImage)
histogram = cv2.calcHist([grayImage], [0], None, [256], [0,256])
print(histogram)
cv2.waitKey()
cv2.destroyAllWindows()