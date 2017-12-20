import cv2
import numpy as np

# Carrega a imagem na escala cinza 
image = cv2.imread('../img/gradient.jpg',0)
cv2.imshow('Original', image)

# Valores acima de 127 sao truncados e abaixo ficam intactos
ret,thresh3 = cv2.threshold(image, 127, 255, cv2.THRESH_TRUNC)
cv2.imshow('3 THRESH TRUNC', thresh3)

cv2.imwrite('../img/limiarizacaobinariatrunc.jpg', thresh3)

cv2.waitKey(0) 
cv2.destroyAllWindows()