import cv2
import numpy as np
from matplotlib import pyplot as plot
image = cv2.imread('../img/babuino2.jpg')
cv2.imshow('Imagem Colorida', image)
color = ('b','g','r')
for i,col in enumerate(color):
    histr = cv2.calcHist([image],[i],None,[265],[0,256])
    plot.plot(histr,color = col)
    plot.xlim([0,256])
plot.savefig('../img/histogramcolor.jpg')
plot.show()
cv2.waitKey()
cv2.destroyAllWindows()