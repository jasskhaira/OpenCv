import cv2
import numpy as np

img = np.zeros((4,4),dtype=np.uint8)

"print(img)"

img  = cv2.cvtColor(img,cv2.COLOR_GRAY2RGB)

"print(img)"

image = cv2.imread("lion.jpg")

bytearr = bytearray(image)




cv2.imshow("Loin",image)
cv2.waitKey()