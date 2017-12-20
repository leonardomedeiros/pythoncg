mport cv2
import numpy as np

image = cv2.imread('../img/imgresize.jpg',0)
cv2.imshow('Original Image', image) 

#blur filter
kernel_blur = np.ones((3,3),np.float32)/9
filteredimage = cv2.filter2D(image,-1,kernel_blur)
cv2.imshow('Filtered Image', filteredimage) 

#remove pair rows
#imgFiltered(2:2:end,:)=[];
imgResample = np.asarray(imgFiltered, dtype='uint8' )

#imgResample(2:2:end,:)=[];
#imgResample(:,2:2:end)=[];

cv2.imshow('Image Resampled', imgResample) 



cv2.waitKey(0)
cv2.destroyAllWindows()