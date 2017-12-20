import cv2
import numpy as np

image = cv2.imread('../img/babuino.jpg')

# BGR Values for the first 0,0 pixel
B, G, R = image[0, 0] 
print B, G, R

#BGR Layers
print image.shape