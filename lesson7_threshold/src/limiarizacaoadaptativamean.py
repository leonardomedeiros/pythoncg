import cv2
import numpy as np

# Carregar nossa imagem
image = cv2.imread('../img/booksonthetable.jpeg', 0)
cv2.imshow('Original', image)
cv2.waitKey(0) 
# Filtro de blur para remover o ruido da imagem
image = cv2.GaussianBlur(image, (3, 3), 0)
thresh = cv2.adaptiveThreshold(image, 255, 
  cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 3, 5) 
cv2.imshow("Adaptive Mean Thresholding", thresh) 
cv2.imwrite('../img/limiarizacaoadaptativa.jpg', thresh)
cv2.waitKey(0) 

cv2.destroyAllWindows()