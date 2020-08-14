import cv2
import numpy as np
import os

randByteArray = bytearray(os.urandom(120000))
flatNpArray = np.array(randByteArray)


grayImg = flatNpArray.reshape(300,400)
cv2.imshow("GreyImage",grayImg)
cv2.waitKey()

bgrImg =  flatNpArray.reshape(100,400,3)
cv2.imshow("Bgr Image",bgrImg)
cv2.waitKey()