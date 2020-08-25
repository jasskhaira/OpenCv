import  cv2 as cv
import numpy as np




# mouse click to draw a circle

def draw_circle(event,x,y,flags,param):
    if event == cv.EVENT_FLAG_MBUTTON:
        cv.circle(img,(x,y), 100, (255,0,0), -1)


# create a black image

img = np.zeros((512,512,3),np.uint8)
cv.namedWindow("Image")
cv.setMouseCallback("Image",draw_circle)

while(1):
    cv.imshow("Image",img)
    if cv.waitKey(20) & 0xFF == 27:
        break

cv.destroyAllWindows()
