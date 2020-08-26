import numpy as np
import cv2 as cv

img = cv.imread('10-13.jpg')

px = img[100,100]
print(px)


#accessing blue pixels
0
blue = img[0,100,0]
print(blue)

item = img.item(10,10,2)
print(item)

img.itemset((10,10,2),200)
item = img.item(10,10,2)

print(item)

print(img.shape)
print(img.dtype)
