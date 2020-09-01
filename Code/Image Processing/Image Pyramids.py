import cv2 as cv


cap = cv.VideoCapture(0)

while True:

    _,frame = cap.read(0)
    lowRes = cv.pyrDown(frame)
    hiRes = cv.pyrUp(frame)
    _,th1 = cv.threshold(frame,130,0,cv.THRESH_MASK)

    cv.imshow("Original", frame)
    cv.imshow("Low res", lowRes)
    cv.imshow("High Res", th1)
    if cv.waitKey(1) == ord('q'):
        break


cap.release()
cv.destroyAllWindows()
