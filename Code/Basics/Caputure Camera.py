import cv2

clik = False
def onMouse(event, x , y, flags, param ):
    global clik
    if event == cv2.EVENT_LBUTTONUP:
        clik = True

Cameracap = cv2.VideoCapture(0)
cv2.namedWindow("Live Feed")
cv2.setMouseCallback('Live Feed', onMouse)

print('Showing Camra feed')
s
uccess , frame = Cameracap.read()
while success and cv2.waitKey(1) == -1 and not clik:
    cv2.imshow('Window', frame)
    success ,frame = Cameracap.read()


cv2.destroyAllWindows()
Cameracap.release()
