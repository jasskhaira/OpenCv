import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('j.png')

kernel = np.ones((5,5),np.float32)/50

print("Kernel is" ,kernel)
dst = cv.filter2D(img,-1,kernel)
blur = cv.blur(img,(5,5))
box = cv.boxFilter(img,-1,(5,5),normalize=False)
gblur = cv.GaussianBlur(img,(5,5),0)
cv.imshow('Origninal',img)
cv.imshow('Dub',dst)
cv.imshow('Blur',blur)
cv.imshow("box",box)
cv.imshow("Gaussian Blur", gblur)
cv.waitKey()
cv.destroyAllWindows()