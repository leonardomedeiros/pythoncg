import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('../img/sudoku.jpg',0)
cv2.imshow('Imagem Original', img)
# Canny Edge Detection uses gradient values as thresholds
# The first threshold gradient
canny = cv2.Canny(img, 50, 120)
plt.subplot(1,2,1),plt.imshow(img,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(1,2,2),plt.imshow(canny,cmap = 'gray')
plt.title('Cany'), plt.xticks([]), plt.yticks([])
plt.savefig('../img/canyfilter.jpg')
plt.show()
cv2.waitKey(0) 
cv2.destroyAllWindows()

