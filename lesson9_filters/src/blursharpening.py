import cv2
import numpy as np

imagemruido = cv2.imread('../img/imgruido.jpg')
kernel_blur = np.ones((3,3),np.float32)/9
kernel_sharpening = np.array([[-1,-1,-1], 
                              [-1,9,-1], 
                              [-1,-1,-1]])
#ddepth - the output image depth (-1 to use src.depth()).
filteredimage = cv2.filter2D(imagemruido,-1,kernel_blur)
filteredimage = cv2.filter2D(filteredimage,-1,kernel_sharpening)
cv2.imshow('Imagem Original com Ruido', imagemruido)
cv2.imshow('Imagem Filtrada Por Sharpenning', filteredimage)
cv2.imwrite('../img/blurredsharpenedimage.jpg', filteredimage)
originalimage = cv2.imread('../img/imgoriginal.jpg')
cv2.imshow('Imagem Original', originalimage)
cv2.waitKey(0) 
cv2.destroyAllWindows()