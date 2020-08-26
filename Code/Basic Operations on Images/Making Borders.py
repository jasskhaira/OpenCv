import cv2 as cv
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('Agg')

Blue = [255,0,0]

img = cv.imread('10-13.jpg')

replicate = cv.copyMakeBorder(img,10,10,10,10,cv.BORDER_REPLICATE)
reflect = cv.copyMakeBorder(img,10,10,10,10,cv.BORDER_REFLECT_101)

ref2 = cv.copyMakeBorder(img,10,10,10,10,cv.BORDER_REFLECT101)
wrap = cv.copyMakeBorder(img,10,10,10,10,cv.BORDER_WRAP)
constant = cv.copyMakeBorder(img,10,10,10,10,cv.BORDER_CONSTANT,value=Blue)


plt.subplot(231),plt.imshow(img,'gray'),plt.title('Original')
plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('Replicate')
plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('Reflect')
plt.subplot(234),plt.imshow(ref2,'gray'),plt.title('ref2')
plt.subplot(235),plt.imshow(wrap,'gray'),plt.title('Wrap')
plt.subplot(236),plt.imshow(constant,'gray'),plt.title('Constant')

plt.show()