import cv2 as cv
import numpy as np
import tkinter
import matplotlib as mp
from matplotlib import pyplot as plt
mp.use('tkagg')
cam = cv.VideoCapture(0)


while True:

    _,frame = cam.read()
    

    cv.imshow("Camera Feed",frame)

    if cv.waitKey(1) == ord('q'):
        break


cam.release()
cv.destroyAllWindows()