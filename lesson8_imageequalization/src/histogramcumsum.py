import cv2
import numpy as np
from matplotlib import pyplot as plot
img = cv2.imread('../img/vale.jpg',0)
cv2.imshow('Imagem Original', img)
hist,bins = np.histogram(img.flatten(),256,[0,256])
#cumulative distribution function
cdf = hist.cumsum()
cdf_normalized = cdf * hist.max()/cdf.max()
plot.plot(cdf_normalized, color = 'b')
plot.hist(img.flatten(),256,[0,256], color = 'r')
plot.xlim([0,256])
plot.legend(('cdf','histogram'), loc = 'upper left')
plot.savefig('../img/cumhistogram.jpg')
plot.show()
cv2.waitKey()
cv2.destroyAllWindows()
