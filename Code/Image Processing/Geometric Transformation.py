import cv2 as cv
import numpy as np

img =cv.imread('guillaume-de-germain-mrL7QWWkciE-unsplash.jpg',0)

res = cv.resize(img,(400,700),interpolation=cv.INTER_CUBIC)
cv.imshow('imag',img)
row,cols = img.shape
M = np.float32([[1,0,100],[0,1,50]])
dst = cv.warpAffine(res,M,(cols,row))
cv.imshow('img',dst)
cv.waitKey()
cv.destroyAllWindows()