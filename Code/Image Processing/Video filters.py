import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)



while(1):
    ret,frame = cap.read()

    if not ret:
        print("Can't recieve frame ")

    laplac = cv.Laplacian(frame,cv.CV_64FC1)
    slobex = cv.Sobel(frame,cv.CV_64F,1,0,ksize=5)



    cv.imshow("Main Video",frame)
    cv.imshow("Laplac" , laplac)
    cv.imshow("Sobel x",slobex)
    if cv.waitKey(1) == ord('q'):
        break


cap.release()
cv.destroyAllWindows()
