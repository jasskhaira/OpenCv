import cv2 as cv


cap = cv.VideoCapture(0)

while True:

    _,frame = cap.read()
    lowRes = cv.pyrDown(frame)
    hiRes = cv.pyrUp(frame)

    cv.imshow("Original", frame)
    cv.imshow("Low res", lowRes)
    cv.imshow("High Res", hiRes)
    if cv.waitKey(1) == ord('q'):
        break


cap.release()
cv.destroyAllWindows()
