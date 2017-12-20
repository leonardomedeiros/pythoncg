import cv2 

input = cv2.imread('../img/input.jpg')

cv2.imshow('Hello World', input)
cv2.waitKey(0)
cv2.destroyAllWindows()