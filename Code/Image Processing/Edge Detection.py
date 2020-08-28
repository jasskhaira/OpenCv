import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

while True:

    ret, frame = cap.read()

    edges = cv.Canny(frame,100,400)
    cv.imshow("Original",frame)
    cv.imshow("Edge Detecation", edges)
    print(edges)

    if cv.waitKey(1) == ord('q'):
        break


cap.release()
cv.destroyAllWindows()