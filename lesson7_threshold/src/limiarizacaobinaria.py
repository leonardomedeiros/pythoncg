import cv2
import numpy as np

# Carrega a imagem na escala cinza 
image = cv2.imread('../img/gradient.jpg',0)
cv2.imshow('Original', image)

# Valores abaixo de 127 irao para 0 (preto) o resto 1 (branco)
ret,thresh1 = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
cv2.imshow('1 Limiarizacao Binaria', thresh1)

cv2.imwrite('../img/limiarizacaobinaria.jpg', thresh1)

cv2.waitKey(0) 
cv2.destroyAllWindows()