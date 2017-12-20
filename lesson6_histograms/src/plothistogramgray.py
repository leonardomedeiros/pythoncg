import cv2
import numpy as np
from matplotlib import pyplot as plot

image = cv2.imread('../img/lena.jpg')
grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Imagem Cinza', grayImage)
plot.hist(grayImage.ravel(),256,[0,256]); 
plot.savefig('../img/histogramgray.jpg')
plot.show()
cv2.waitKey()
cv2.destroyAllWindows()


