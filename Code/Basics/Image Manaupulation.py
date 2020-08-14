import cv2
import numpy as np

img = cv2.imread("lion.jpg")

img[ :,1,:] = 0

cv2.imshow("Modified",img)
cv2.waitKey()
print(img.dtype)
