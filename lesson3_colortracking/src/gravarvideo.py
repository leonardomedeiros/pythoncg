import cv2

cap = cv2.VideoCapture(0)

out = cv2.VideoWriter('../video/videotenis.avi', -1 , 22, (640,480))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        out.write(frame)
        cv2.imshow('frame',frame)  

        # Press ESC to close windows      
        k = cv2.waitKey(5) & 0xFF
        if k == 27:
          break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()