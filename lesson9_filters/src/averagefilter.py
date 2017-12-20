import cv2
import numpy as np

imagemruido = cv2.imread('../img/imgruido.jpg')
kernel = np.ones((3,3),np.float32)/9
#ddepth - the output image depth (-1 to use src.depth()).
filteredimage = cv2.filter2D(imagemruido,-1,kernel)
cv2.imshow('Imagem Original com Ruido', imagemruido)
cv2.imshow('Imagem Filtrada Por Media', filteredimage)
cv2.imwrite('../img/filteredimage.jpg', filteredimage)
originalimage = cv2.imread('../img/imgoriginal.jpg')
cv2.imshow('Imagem Original', originalimage)
cv2.waitKey(0) 
cv2.destroyAllWindows()