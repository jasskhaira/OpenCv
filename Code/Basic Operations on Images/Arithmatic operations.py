# Image Addition
import cv2 as cv
import numpy as np

x = np.uint8([240])
y = np.uint8([10])

print(cv.add(x,y))
print(x+y)


img1 = cv.imread('10-13.jpg')

dim = (int(img1.shape[1]),int(img1.shape[0]))

img2 = cv.imread('10-15-Day.jpg')

img2 = cv.resize(img2,dim,interpolation=cv.INTER_AREA)
dist = cv.addWeighted(img1,0.7,img2,0.3,0)

cv.imshow('dist',dist)

cv.waitKey()
cv.destroyAllWindows()


