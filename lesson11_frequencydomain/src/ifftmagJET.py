import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('../img/messi5.jpg',0)
cv2.imshow('Imagem Original', img)

f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
magnitude_spectrum = 20*np.log(np.abs(fshift))
rows, cols = img.shape
crow,ccol = rows/2 , cols/2
fshift[crow-30:crow+30, ccol-30:ccol+30] = 0
f_ishift = np.fft.ifftshift(fshift)
img_back = np.fft.ifft2(f_ishift)
img_back = np.abs(img_back)
plt.subplot(131),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(132),plt.imshow(img_back, cmap = 'gray')
plt.title('Image Filtro Passa Alta'), plt.xticks([]), plt.yticks([])
plt.subplot(133),plt.imshow(img_back)
plt.title('Result in fftnumpy-lpf-jet'), plt.xticks([]), plt.yticks([])

plt.savefig('../img/fftnumpy-lpf-jet.jpg')
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
