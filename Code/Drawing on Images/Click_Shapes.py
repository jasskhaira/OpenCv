import numpy as np
import cv2 as cv

draw = False #true if mouse is pressed
mode = True # if true, draw rectangle. Press 'm' to toggle to curve
ix,iy = -1,-1

# mouse callback function

def draw_circle(event, x,y, flags,param):
    global  ix,iy,draw,mode

    if event == cv.EVENT_LBUTTONDOWN:
        draw = True
        ix, iy = x,y

    elif event == cv.EVENT_MOUSEMOVE:
        if draw == True:
            if mode == True:
                cv.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
            else:
                cv.circle(img,(x,y),5,(0,0,255),-1)

    elif event == cv.EVENT_LBUTTONUP:
        draw = False
        if mode == True:
            cv.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)

        else:
            cv.circle(img,(x,y),5,(0,0,255),-1)



img = np.zeros((900,900,3),np.uint8)

cv.namedWindow("Board")
cv.setMouseCallback("Board",draw_circle)

while(1):
    cv.imshow("Board",img)
    k = cv.waitKey(1) & 0xFF
    if k == ord('m'):
        mode = not mode
    elif k ==27:
        break

cv.destroyAllWindows()