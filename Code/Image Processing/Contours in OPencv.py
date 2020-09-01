import cv2 as cv
import numpy as np

img = cv.imread("trtangle.jpg",0)
img = cv.resize(img,(400,500),cv.INTER_AREA)

ret, thresh = cv.threshold(img,127,255,0)
contor, hierarchy = cv.findContours(thresh,1,2)

cnt = contor[0]
M = cv.moments(cnt)
print(M)
cv.imshow("Thresh",thresh)
area = cv.contourArea(cnt)
perimeter = cv.arcLength(cnt,True)

epsilon = 0.1*cv.arcLength(cnt,True)
approx = cv.approxPolyDP(cnt,epsilon,True)

print(epsilon)

rect = cv.minAreaRect(cnt)
box = cv.boxPoints(rect)
box = np.int0(box)

draw = cv.drawContours(thresh,[box],0,(0,0,255),2)

eclipse = cv.fitEllipse(cnt)
ne = cv.ellipse(img,eclipse,(0,255,0),2)
cv.imshow("box",ne)




print("Area", area )
print("Perimeter",perimeter)
cv.waitKey(0)
cv.destroyAllWindows()
