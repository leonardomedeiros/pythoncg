import cv2
import numpy as np

# Carrega a imagem na escala cinza 
image = cv2.imread('../img/gradient.jpg',0)
cv2.imshow('Original', image)

# Valores abaixo de 127 vao a 0, acima de 127 ficam intactos  
ret,thresh4 = cv2.threshold(image, 127, 255, cv2.THRESH_TOZERO)
cv2.imshow('4 THRESH TOZERO', thresh4)

cv2.imwrite('../img/limiariazacaobinariatreshtozero.jpg', thresh4)

cv2.waitKey(0) 
cv2.destroyAllWindows()