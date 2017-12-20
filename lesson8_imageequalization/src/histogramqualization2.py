import cv2
import numpy as np
from matplotlib import pyplot as plot
img = cv2.imread('../img/vale.jpg',0)
cv2.imshow('Imagem Original', img)
#cumulative distribution function
hist,bins = np.histogram(img.flatten(),256,[0,256])
cdf = hist.cumsum()
cdf_normalized = cdf * hist.max()/cdf.max()
#Equalizacao do Histograma
cdf_m = np.ma.masked_equal(cdf,0)
cdf_m = (cdf_m - cdf_m.min())*255/(cdf_m.max()-cdf_m.min())
cdf = np.ma.filled(cdf_m,0).astype('uint8')
img_equalized = cdf[img]
cv2.imshow('Imagem Equalizada', img_equalized)
cv2.imwrite('../img/imagemequalizada.jpg', img_equalized)
#Calculate cumulative distribution function of equalized image
hist,bins = np.histogram(img_equalized.flatten(),256,[0,256])
cdf_new = hist.cumsum()
cdf_normalized_new = cdf_new * hist.max()/cdf_new.max()

#Plot Equalization
plot.plot(cdf_normalized_new, color = 'b')
plot.hist(img_equalized.flatten(),256,[0,256], color = 'r')
plot.xlim([0,256])
plot.legend(('cdf','histogram'), loc = 'upper left')
plot.savefig('../img/equalizedhistogram.jpg')
plot.show()
cv2.waitKey()
cv2.destroyAllWindows()
