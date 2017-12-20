import cv2
import numpy as np

# Carregar nossa imagem
image = cv2.imread('../img/Origin_of_Species.jpg', 0)

cv2.imshow('Original', image)
cv2.waitKey(0) 

ret,thresh1 = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
cv2.imshow('Threshold Binary', thresh1)
cv2.imwrite('../img/limiarizacaoabinariaorigin.jpg', thresh1)
cv2.waitKey(0) 

cv2.destroyAllWindows()