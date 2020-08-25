import numpy as np
import cv2 as cv

img = np.zeros((512,512,3), np.uint8)



cv.line(img,(4,50),(511,50),(255,0,0),5)



cv.rectangle(img, (200,100),(350,128),(0,255,0),3)





font = cv.FONT_ITALIC

cv.putText(img,"Jass Khaira", (0,500),font,2,(255,255,255),2,cv.LINE_AA)


cv.imshow("Image", img)
cv.waitKey()
cv.destroyAllWindows()