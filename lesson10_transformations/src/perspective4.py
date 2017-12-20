import cv2
import numpy as np
image = cv2.imread('../img/scan.jpg',0)
cv2.imshow('Original', image)
cv2.waitKey(0)
# Cordinates of the 4 corners of the original image
points_A = np.float32([[320,15], [700,215], [85,610], [530,780]])
# Cordinates of the 4 corners of the desired output
points_B = np.float32([[0,0], [420,0], [0,594], [420,594]]) 
M = cv2.getPerspectiveTransform(points_A, points_B) 
warped = cv2.warpPerspective(image, M, (420,594)) 
cv2.imshow('warpPerspective', warped)
cv2.imwrite('../img/imgwarped4.jpg', warped)
cv2.waitKey(0)
cv2.destroyAllWindows()
