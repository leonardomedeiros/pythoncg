import cv2
import numpy as np
from matplotlib import pyplot as plot

image = cv2.imread('../img/recife2.jpg')
#grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#hsvImage = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
#h, s, v = cv2.split(hsvImage)

cv2.imshow('Imagem Orignal', image)
plot.hist(image.ravel(),256,[0,256])
plot.show()

imageBright = image + 20
#v = v +30
#hsvImage2 = cv2.merge([h,s,v])
cv2.imshow('Imagem Com Mais Brilho', imageBright)
plot.hist(imageBright.ravel(),256,[0,256]) 
plot.show()

cv2.waitKey()
cv2.destroyAllWindows()






