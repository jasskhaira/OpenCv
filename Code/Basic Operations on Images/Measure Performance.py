import cv2 as cv
img = cv.imread('../Image Processing/guillaume-de-germain-mrL7QWWkciE-unsplash.jpg')
e1 =cv.getTickCount()
res = cv.resize(img,(400,500),interpolation=cv.INTER_AREA)
cv.imshow("iq",res)
for i in range(5,49,2):
    res=cv.medianBlur(res,i)

e2= cv.getTickCount()
time = (e2-e1)/cv.getTickFrequency()
print(time)

cv.imshow('img',res)
cv.waitKey()
cv.destroyAllWindows()

