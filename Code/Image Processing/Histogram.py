import cv2 as cv
import numpy as np
import tkinter
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('tkAgg')

print(plt.get_backend())
img = cv.imread("opencv.jpeg")

hist = cv.calcHist(img,[0],None,[256],[0,256])

#histn , bins = np.histogram(img.ravel(),256,[0,256])
#eq =cv.equalizeHist(img)

#res = np.hstack((img,eq))


hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)

hg = cv.calcHist([hsv],[0,1],None,[180,256],[0,180,0,256])

plt.imshow(img)
plt.show()


cv.imshow("hist",hg)
cv.waitKey(0)
cv.destroyAllWindows()
