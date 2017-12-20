import cv2
import numpy as np

# Load our new image
image = cv2.imread('../img/booksonthetable.jpeg', 0 )

cv2.imshow('Original', image)
cv2.waitKey(0) 

_, th2 = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
cv2.imshow("Otsu's Thresholding", th2) 
cv2.imwrite('../img/limiarizacaoadaptativaotsu.jpg', th2)
cv2.waitKey(0) 

cv2.destroyAllWindows()