import cv2
import numpy as np
from matplotlib import pyplot as plot
img = cv2.imread('../img/imagemchleoriginal.png',0)

# create a CLAHE object (Arguments are optional).
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
cl1 = clahe.apply(img)
cv2.imwrite('../img/imagemcomclaheequalizada.png',cl1)

cv2.imshow('Imagem Original', img)
cv2.imshow('Imagem Equalizada com CLAHE', cl1)

cv2.waitKey()
cv2.destroyAllWindows()

