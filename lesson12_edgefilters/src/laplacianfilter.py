import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('../img/sudoku.jpg',0)
cv2.imshow('Imagem Original', img)
laplacian = cv2.Laplacian(img,cv2.CV_64F)
plt.subplot(1,2,1),plt.imshow(img,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(1,2,2),plt.imshow(laplacian,cmap = 'gray')
plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
plt.savefig('../img/laplacianfilter.jpg')
plt.show()
cv2.waitKey(0) 
cv2.destroyAllWindows()