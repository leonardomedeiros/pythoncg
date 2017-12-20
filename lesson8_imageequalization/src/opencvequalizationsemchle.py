import cv2
import numpy as np
from matplotlib import pyplot as plot
img = cv2.imread('../img/imagemchleoriginal.png',0)

equ = cv2.equalizeHist(img)
cv2.imshow('Imagem Original', img)
cv2.imshow('Imagem Equalizada', equ)
cv2.imwrite('../img/imagemsemchleequalizada.png',equ)
cv2.waitKey()
cv2.destroyAllWindows()

