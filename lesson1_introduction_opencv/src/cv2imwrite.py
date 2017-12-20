
import cv2 

input = cv2.imread('input.jpg')

cv2.imshow('Hello World', input)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Simply use 'imwrite' specificing the file name and the image to be saved
cv2.imwrite('output.jpg', input)
cv2.imwrite('output.png', input)